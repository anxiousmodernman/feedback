__author__ = 'coleman'

from connections import AlchemyConnection
import uuid

class FeedbackSubscriber(object):

    def __init__(self, conn, mail_format_id=1, marketing_message='true', **kwargs):
        self.subscriberid = str(uuid.uuid4)
        self.email = kwargs['email']
        self.first_name = kwargs.get('first_name', "null")
        self.last_name = kwargs.get('last_name', "null")
        self.company = kwargs.get('company', "null")
        self.title = kwargs.get('title', "null")
        self.city = kwargs.get('city', "null")
        self.state = kwargs.get('state', "null")
        self.country = kwargs.get('country', "null")
        self.zipcode = kwargs.get('zipcode', "null")
        self.mail_format_id = mail_format_id
        self.marketing_message = marketing_message
        self.conn = conn
        # etc

    def saveSubscriber(self):
        self.cur = self.conn.cursor()
        self.cur.execute("""update {table_name}

        """.format(table_name="feedback"))

    def logSubscriber(self):
        pass

# executemany() takes