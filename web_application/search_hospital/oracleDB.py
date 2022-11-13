import cx_Oracle
from .DB import DB
import config as cfg
import xml.etree.ElementTree as ET


class OracleDB(DB):

    def __init__(self):
        pass

    def saveOutputToXML(self, output):
        name = ''
        phone = ''
        email = ''
        nid = ''
        aircraft = ''

        for x in output:
            name = x[0]
            phone = str(x[1])
            email = x[2]
            nid = str(x[3])
            aircraft = x[4]

            data = ET.Element('database')
            element1 = ET.SubElement(data, 'table1')

            s_elem1 = ET.SubElement(element1, 'name')
            s_elem2 = ET.SubElement(element1, 'phone')
            s_elem3 = ET.SubElement(element1, 'email')
            s_elem4 = ET.SubElement(element1, 'nid')
            s_elem5 = ET.SubElement(element1, 'aircraft')

            s_elem1.text = name
            s_elem2.text = phone
            s_elem3.text = email
            s_elem4.text = nid
            s_elem5.text = aircraft

            b_xml = ET.tostring(data)

            with open("result.xml", "wb") as f:
                f.write(b_xml)

    def getDatabaseCredentials(self):
        mytree = ET.parse('config.xml')
        myroot = mytree.getroot()

        for y in myroot:
            # print(y.tag)
            if y.tag == "oracle":
                for x in y:
                    if x.tag == 'user':
                        userDB = x.text
                    if x.tag == 'password':
                        passwordDB = x.text
                    if x.tag == 'database':
                        databaseDB = x.text

        return userDB, passwordDB, databaseDB

    def getQueryInputSelect(self):
        mytree = ET.parse('operation.xml')
        myroot = mytree.getroot()
        for y in myroot:
            if y.tag == "oracle":
                for op in y:
                    # print(op.tag)
                    if op.tag == "select":
                        for x in op:
                            if x.tag == 'column':
                                column = x.text
                            if x.tag == 'table':
                                table = x.text
                            if x.tag == 'condition':
                                condition = x.text

        return column, table, condition

    def getQueryInputInsert(self):
        mytree = ET.parse('operation.xml')
        myroot = mytree.getroot()

        for y in myroot:
            if y.tag == "oracle":
                # print(myroot[1].tag)
                for op in y:
                    if op.tag == "insert":
                        for x in op:
                            # print(x.tag)
                            if x.tag == 'table':
                                table = x.text
                            if x.tag == 'columnName':
                                columnName = x.text
                            if x.tag == 'value':
                                value = x.text

        return table, columnName, value

    def getQueryInputUpdate(self):
        mytree = ET.parse('operation.xml')
        myroot = mytree.getroot()
        for y in myroot:
            if y.tag == "oracle":
                # print(myroot[1].tag)
                for op in y:
                    if op.tag == "update":
                        for x in op:
                            # print(x.tag)
                            if x.tag == 'table':
                                table = x.text
                            if x.tag == 'condition':
                                condition = x.text
                            if x.tag == 'newValue':
                                newValue = x.text

        return table, condition, newValue

    def getQueryInputDelete(self):
        mytree = ET.parse('operation.xml')
        myroot = mytree.getroot()
        for y in myroot:
            if y.tag == "oracle":
                for op in y:
                    if op.tag == "delete":
                        for x in op:
                            if x.tag == 'table':
                                table = x.text
                            if x.tag == 'condition':
                                condition = x.text

        return table, condition

    def select(self):
        userDB, passwordDB, databaseDB = self.getDatabaseCredentials()
        column, table, condition = self.getQueryInputSelect()

        if condition != 'NULL':
            sql = 'SELECT ' + column + ' FROM ' + table + ' WHERE ' + condition
        else:
            sql = 'SELECT ' + column + ' FROM ' + table

        try:
            # establish a new connection
            with cx_Oracle.connect(userDB,
                                   passwordDB,
                                   databaseDB,
                                   encoding=cfg.encoding) as connection:
                # create a cursor
                with connection.cursor() as cursor:
                    # execute the insert statement
                    cursor.execute(sql)
                    rows = cursor.fetchone()
                    self.saveOutputToXML(rows)

        except cx_Oracle.Error as error:
            print('Error occurred:')
            print(error)

    def insert(self):
        userDB, passwordDB, databaseDB = self.getDatabaseCredentials()
        table, columnName, value = self.getQueryInputInsert()

        sql = "INSERT INTO " + table + " " + columnName + " values " + value

        try:
            # establish a new connection
            with cx_Oracle.connect(userDB,
                                   passwordDB,
                                   databaseDB,
                                   encoding=cfg.encoding) as connection:
                # create a cursor
                with connection.cursor() as cursor:
                    # execute the insert statement
                    cursor.execute(sql)
                    # commit work
                    connection.commit()
        except cx_Oracle.Error as error:
            print('Error occurred:')
            print(error)

    def update(self):
        userDB, passwordDB, databaseDB = self.getDatabaseCredentials()
        table, condition, newValue = self.getQueryInputUpdate()

        sql = "UPDATE " + table + " SET " + newValue + " WHERE " + condition

        try:
            # establish a new connection
            with cx_Oracle.connect(userDB,
                                   passwordDB,
                                   databaseDB,
                                   encoding=cfg.encoding) as connection:
                # create a cursor
                with connection.cursor() as cursor:
                    # execute the insert statement
                    cursor.execute(sql)
                    # commit work
                    connection.commit()
        except cx_Oracle.Error as error:
            print('Error occurred:')
            print(error)

    def delete(self):
        userDB, passwordDB, databaseDB = self.getDatabaseCredentials()
        table, condition = self.getQueryInputDelete()

        sql = "DELETE FROM " + table + " WHERE " + condition

        try:
            # establish a new connection
            with cx_Oracle.connect(userDB,
                                   passwordDB,
                                   databaseDB,
                                   encoding=cfg.encoding) as connection:
                # create a cursor
                with connection.cursor() as cursor:
                    # execute the insert statement
                    cursor.execute(sql)
                    # commit work
                    connection.commit()
        except cx_Oracle.Error as error:
            print('Error occurred:')
            print(error)




