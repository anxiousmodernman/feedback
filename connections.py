

import pyodbc
import sys
import dbconfig
# sys.path.append("/home/coleman/Code/")




class AlchemyConnection(object):
    """
    Connection to database.
    """
    def __init__(self):

        self.createConnection()

    def createConnection(self):

        try:
            self.con = pyodbc.connect('DSN=%s;UID=%s;PWD=%s' % (dbconfig.dsn, dbconfig.user, dbconfig.password))
            print '[AlchemyConnection] Connection successful for user %s to database %s' % (dbconfig.user,
                                                                                            dbconfig.database)
        except pyodbc.DatabaseError as e:
            pass

    def close(self):

        self.con.close()

    def getCursor(self):
        self.cursor = self.con.cursor()
        return self.cursor  # returns pyodbc cursor object

    def commit(self):

        self.con.commit()







