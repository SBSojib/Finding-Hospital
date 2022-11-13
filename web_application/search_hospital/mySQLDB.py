import mysql.connector
import xml.etree.ElementTree as ET
from .DB import DB


class MySQLDB(DB):
    def __init__(self):
        pass

    def saveOutputToXML(self, output):
        name = ''
        phone = ''
        email = ''
        nid = ''
        aircraft = ''

        for x in output:
            #print(x)
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

    def getQueryInputSelect(self):
        mytree = ET.parse('/home/sojib/PycharmProjects/Finding_Hospital/web_application/search_hospital/operation.xml')
        myroot = mytree.getroot()
        for y in myroot:
            if y.tag == "mysql":
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
        mytree = ET.parse('/home/sojib/PycharmProjects/Finding_Hospital/web_application/search_hospital/operation.xml')
        myroot = mytree.getroot()

        for y in myroot:
            if y.tag == "mysql":
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
        mytree = ET.parse('/home/sojib/PycharmProjects/Finding_Hospital/web_application/search_hospital/operation.xml')
        myroot = mytree.getroot()
        for y in myroot:
            if y.tag == "mysql":
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
        mytree = ET.parse('/home/sojib/PycharmProjects/Finding_Hospital/web_application/search_hospital/operation.xml')
        myroot = mytree.getroot()
        for y in myroot:
            if y.tag == "mysql":
                for op in y:
                    if op.tag == "delete":
                        for x in op:
                            if x.tag == 'table':
                                table = x.text
                            if x.tag == 'condition':
                                condition = x.text

        return table, condition

    def getSQLQredentials(self):
        hostDB = ''
        userDB = ''
        passwordDB = ''
        databaseDB = ''

        mytree = ET.parse('/home/sojib/PycharmProjects/Finding_Hospital/web_application/search_hospital/config.xml')
        myroot = mytree.getroot()

        for y in myroot:
            # print(y.tag)
            if y.tag == "mysql":
                for x in y:
                    if x.tag == 'host':
                        hostDB = x.text
                    if x.tag == 'user':
                        userDB = x.text
                    if x.tag == 'password':
                        passwordDB = x.text
                    if x.tag == 'database':
                        databaseDB = x.text

        return hostDB, userDB, passwordDB, databaseDB

    def select(self):
        column, table , condition = self.getQueryInputSelect()
        hostDB, userDB, passwordDB, databaseDB = self.getSQLQredentials()

        if condition != 'NULL':
            sql = 'SELECT ' + column + ' FROM ' + table + ' WHERE ' + condition
        else:
            sql = 'SELECT ' + column + ' FROM ' + table

        mydb = mysql.connector.connect(
            host=hostDB,
            user=userDB,
            password=passwordDB,
            database=databaseDB
        )

        my_cursor = mydb.cursor()
        my_cursor.execute(sql)
        myresult = my_cursor.fetchall()

        #self.saveOutputToXML(myresult)

        #print(myresult)

        return myresult

    def select_institution(self):
        sql = 'select * from Institution'

        mydb = mysql.connector.connect(
            host='localhost',
            user='root',
            password='Disguised',
            database='Hospital_Information'
        )

        my_cursor = mydb.cursor()
        my_cursor.execute(sql)
        myresult = my_cursor.fetchall()

        #self.saveOutputToXML(myresult)

        #print(myresult)

        return myresult

    def select_hospital(self, id):
        sql = 'select * from Hospital where id =' + id

        mydb = mysql.connector.connect(
            host='localhost',
            user='root',
            password='Disguised',
            database='Hospital_Information'
        )

        my_cursor = mydb.cursor()
        my_cursor.execute(sql)
        myresult = my_cursor.fetchall()

        #self.saveOutputToXML(myresult)

        #print(myresult)

        return myresult

    def select_specialist_type(self):
        sql = "select Specialist_Of from Specialist_Doctor"

        mydb = mysql.connector.connect(
            host='localhost',
            user='root',
            password='Disguised',
            database='Hospital_Information'
        )

        my_cursor = mydb.cursor()
        my_cursor.execute(sql)
        myresult = my_cursor.fetchall()

        #self.saveOutputToXML(myresult)

        #print(myresult)

        return myresult

    def select_specialist(self, name):
        sql = "select * from Specialist_Doctor where Specialist_Of ='" + name +"'"

        mydb = mysql.connector.connect(
            host='localhost',
            user='root',
            password='Disguised',
            database='Hospital_Information'
        )

        my_cursor = mydb.cursor()
        my_cursor.execute(sql)
        myresult = my_cursor.fetchall()

        #self.saveOutputToXML(myresult)

        #print(myresult)

        return myresult

    def select_surgery_type(self):
        sql = "select Surgery_Name from Surgery"

        mydb = mysql.connector.connect(
            host='localhost',
            user='root',
            password='Disguised',
            database='Hospital_Information'
        )

        my_cursor = mydb.cursor()
        my_cursor.execute(sql)
        myresult = my_cursor.fetchall()

        #self.saveOutputToXML(myresult)

        #print(myresult)

        return myresult

    def select_surgery(self, name):
        sql = "select * from Surgery where Surgery_Name ='" + name +"'"

        mydb = mysql.connector.connect(
            host='localhost',
            user='root',
            password='Disguised',
            database='Hospital_Information'
        )

        my_cursor = mydb.cursor()
        my_cursor.execute(sql)
        myresult = my_cursor.fetchall()

        #self.saveOutputToXML(myresult)

        #print(myresult)

        return myresult

    def select_diagonosis_type(self):
        sql = "select Diagonosis_Name from Diagonosis"

        mydb = mysql.connector.connect(
            host='localhost',
            user='root',
            password='Disguised',
            database='Hospital_Information'
        )

        my_cursor = mydb.cursor()
        my_cursor.execute(sql)
        myresult = my_cursor.fetchall()

        #self.saveOutputToXML(myresult)

        #print(myresult)

        return myresult

    def select_diagonosis(self, name):
        sql = "select * from Diagonosis where Diagonosis_Name ='" + name +"'"

        mydb = mysql.connector.connect(
            host='localhost',
            user='root',
            password='Disguised',
            database='Hospital_Information'
        )

        my_cursor = mydb.cursor()
        my_cursor.execute(sql)
        myresult = my_cursor.fetchall()

        #self.saveOutputToXML(myresult)

        #print(myresult)

        return myresult

    def select_doctor(self, id):
        sql = "select * from Doctor where Doctor_ID ='" + id +"'"

        mydb = mysql.connector.connect(
            host='localhost',
            user='root',
            password='Disguised',
            database='Hospital_Information'
        )

        my_cursor = mydb.cursor()
        my_cursor.execute(sql)
        myresult = my_cursor.fetchall()

        #self.saveOutputToXML(myresult)

        #print(myresult)

        return myresult

    def insert(self):
        table, columnName, value = self.getQueryInputInsert()
        hostDB, userDB, passwordDB, databaseDB = self.getSQLQredentials()

        sql = "INSERT INTO " + table + " " + columnName + " values " + value

        mydb = mysql.connector.connect(
            host=hostDB,
            user=userDB,
            password=passwordDB,
            database=databaseDB
        )

        my_cursor = mydb.cursor()
        my_cursor.execute(sql)
        mydb.commit()

    def update(self):
        table, condition, newValue = self.getQueryInputUpdate()
        hostDB, userDB, passwordDB, databaseDB = self.getSQLQredentials()

        sql = "UPDATE " + table + " SET " + newValue + " WHERE " + condition

        mydb = mysql.connector.connect(
            host=hostDB,
            user=userDB,
            password=passwordDB,
            database=databaseDB
        )

        my_cursor = mydb.cursor()
        my_cursor.execute(sql)
        mydb.commit()

    def delete(self):
        hostDB, userDB, passwordDB, databaseDB = self.getSQLQredentials()
        table, condition = self.getQueryInputDelete()

        sql = "DELETE FROM " + table + " WHERE " + condition

        mydb = mysql.connector.connect(
            host=hostDB,
            user=userDB,
            password=passwordDB,
            database=databaseDB
        )

        my_cursor = mydb.cursor()
        my_cursor.execute(sql)
        mydb.commit()





