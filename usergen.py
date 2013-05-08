from connections import AlchemyConnection
import uuid

class FeedbackSubscriber(object):

    def __init__(self, **kwargs):
        """
        Constructor for FeedbackSubscriber. Defaults for values are the 2nd argument to .get(), and
        these are only used if the key-value pair is missing from the dictionary passed to the
        constructor (kwargs in this namespace).
        """
        self.subscriberid = None   # kwargs.get('subscriberid', str(uuid.uuid4()))
        self.email = kwargs['email']
        self.first_name = kwargs.get('first_name', "Feedback")
        self.last_name = kwargs.get('last_name', "Test")
        self.company = kwargs.get('company', "SmartBrief")
        self.title = kwargs.get('title', "Selenium Tester")
        self.city = kwargs.get('city', "Washington")
        self.state = kwargs.get('state', "DC")
        self.country = kwargs.get('country', "United States")
        self.zipcode = kwargs.get('zipcode', "20004")
        self.mail_format_id = 1
        self.marketing_message = 'true'
        # self.position_level = kwargs.get('positionLevel')
        # etc

