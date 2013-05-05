import unittest
from connections import *

# building tests from the pymssql connection examples here:
# https://code.google.com/p/pymssql/wiki/PymssqlExamples

# Collect test briefid in a dictionary for easy access
BRIEFIDS = {'AAAA': '7325D171-85C1-4A99-9773-4FE6659490B5'}

class AlchemyConnectionTest(unittest.TestCase):

    def testCreateConnection(self):
        test_conn = AlchemyConnection()
        cur = test_conn.getCursor()
        cur.execute('SELECT brief_name, full_brief_name from brief where briefid = %s', BRIEFIDS['AAAA'])
        # cur.execute('SELECT brief_name, full_brief_name from brief where briefid = \'7325D171-85C1-4A99-9773-4FE6659490B5\'') # TODO remove
        results = []  # will be list of
        for row in cur:
            results.append(row['brief_name'])
        cur.close()
        test_conn.close()
        self.assertListEqual(results, ['AAAA'], "Connection to database failed") # TODO better asserts case

class testCreateUser(unittest.TestCase):
    """
    Create a user and subscribe them to AAAA
    """
    pass





def main():
    unittest.main()

if __name__ == '__main__':
    main()