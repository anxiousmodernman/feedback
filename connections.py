

import pymssql
from dbconnect.py import CONNECTION_DICT


class Connection(object):
    """
    Connection class to database. Don't forget to close your connection.
    """
    def createConnection(self):

        self.con = pymssql.connect(CONNECTION_DICT)


#    sqlserver://sqlclust1.smartbrief.com/alchemy;SendStringParametersAsUnicode=false
