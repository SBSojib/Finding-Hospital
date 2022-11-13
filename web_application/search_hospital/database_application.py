from .databaseCreator import DatabaseCreator
import xml.etree.ElementTree as ET


class Application:

    def getDatabaseName(self):
        mytree = ET.parse('/home/sojib/PycharmProjects/Finding_Hospital/web_application/search_hospital/config.xml')
        myroot = mytree.getroot()

        for y in myroot:
            if y.tag == "db":
                for x in y:
                    if x.tag == 'dbName':
                        database = x.text
        return database

    def operate(self, database):
        db = DatabaseCreator.getDatabase(database)
        return db


app = Application()
dbName = app.getDatabaseName()
db = app.operate(dbName)

#db.insert()
#db.update()
#db.delete()
#db.select()

