

import pymssql
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
            self.con = pymssql.connect(dbconfig.host, dbconfig.user, dbconfig.password, dbconfig.database, as_dict=True)
            print '[AlchemyConnection] Connection successful for user %s to database %s' % (dbconfig.user,
                                                                                            dbconfig.database)
        except pymssql.DatabaseError as e:
            pass

    def close(self):

        self.con.close()

    def getCursor(self):
        self.cursor = self.con.cursor()
        return self.cursor  # returns pymmssql cursor object

    def commit(self):

        self.con.commit()







