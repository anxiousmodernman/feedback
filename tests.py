import unittest
from connections import *


class AlchemyConnectionTest(unittest.TestCase):

    def testCreateConnection(self):
        test_conn = AlchemyConnection()
        cur = test_conn.getCursor()
        cur.execute('SELECT brief_name, full_brief_name from brief where brief_name = \'AAAA\'')
        results = []  # will be list of
        for row in cur:
            results.append(row['brief_name'])
        cur.close()
        test_conn.close()
        self.assertListEqual(results, ['AAAA'], "Connection to database failed")


def main():
    unittest.main()

if __name__ == '__main__':
    main()