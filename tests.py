import unittest
from connections import *
import logging
import string
import random
import usergen
import sst.actions


# pymssql connection examples here: https://code.google.com/p/pymssql/wiki/PymssqlExamples

# Collect test briefid in a dictionary for easy access
BRIEF_IDS = {'AAAA': '7325D171-85C1-4A99-9773-4FE6659490B5'}


def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))

# NOTE this will only work with new-style signup pages
def createAAAASubscriberViaWeb(**kwargs):
    sst.actions.start()
    sst.actions.go_to('https://www2.qa.smartbrief.com/aaaa')
    first_email_box = sst.actions.get_element_by_xpath('//*[@id="signupForm"]/div[5]/div[2]/input')
    confirm_email_box = sst.actions.get_element_by_xpath('//*[@id="signupForm"]/div[6]/div[2]/input')
    # use sst.actions function to 'type' into text box
    sst.actions.write_textfield(first_email_box, kwargs['email'])
    sst.actions.write_textfield(confirm_email_box, kwargs['email'])
    # get signup button element and click submit
    submit_button_page1 = sst.actions.get_element_by_css('#SignupDiv')
    sst.actions.click_element(submit_button_page1)
    # complete page 2: first get the elements
    sst.actions.sleep(10)
    sst.actions.stop()

def createWorkforceSubscriberViaWeb(**kwargs):
    sst.actions.start()
    sst.actions.go_to('https://www2.qa.smartbrief.com/aaaa')
    first_email_box = sst.actions.get_element_by_xpath('//*[@id="signupForm"]/div[5]/div[2]/input')
    confirm_email_box = sst.actions.get_element_by_xpath('//*[@id="signupForm"]/div[6]/div[2]/input')
    # use sst.actions function to 'type' into text box
    sst.actions.write_textfield(first_email_box, kwargs['email'])
    sst.actions.write_textfield(confirm_email_box, kwargs['email'])
    # get signup button element and click submit
    submit_button_page1 = sst.actions.get_element_by_css('#SignupDiv')
    sst.actions.click_element(submit_button_page1)
    # complete page 2: first get the elements
    sst.actions.sleep(10)
    first_name_field = sst.actions.get_element_by_xpath('//input[@name="firstName"]')
    last_name_field = sst.actions.get_element_by_xpath('//input[@name="lastName"]')
    company_field = sst.actions.get_element_by_xpath('//input[@name="company"]')
    title_field = sst.actions.get_element_by_xpath('//input[@name="title"]')
    zipcode_field = sst.actions.get_element_by_xpath('//input[@name="zipcode"]')
    country_field = sst.actions.get_element_by_xpath('//select[@name="country"]')
    position_level_field = sst.actions.get_element_by_xpath('//select[@name="positionLevel"]')
    position_function_field = sst.actions.get_element_by_xpath('(//*[@name="positionFunction"])[1]')  # surround w paren
    company_type_field = sst.actions.get_element_by_xpath('(//select[@name="companyType"])[1]')       # and add index[n]
    company_size_field = sst.actions.get_element_by_xpath('//select[@name="companySize"]')
    employees_field = sst.actions.get_element_by_xpath('//select[@name="employees"]')
    aaaa_custom_field_exists = sst.actions.exists_element(id="9C3D46B6-D106-49F5-9D01-661D9A5D566F")  # boolean
    submit_button_page2 = sst.actions.get_element_by_css("#SignupDiv")
    # complete page 2: now, write the fields
    sst.actions.write_textfield(first_name_field, kwargs['first_name'])
    sst.actions.write_textfield(last_name_field, kwargs['last_name'])
    sst.actions.write_textfield(company_field, kwargs['company'])
    sst.actions.write_textfield(title_field, kwargs['title'])
    sst.actions.write_textfield(zipcode_field, kwargs['zipcode'])
    sst.actions.set_dropdown_value(country_field, kwargs['country'])
    sst.actions.set_dropdown_value(position_level_field, "Staff")
    sst.actions.set_dropdown_value(position_function_field, "Sales")
    sst.actions.set_dropdown_value(company_type_field, "Agency: Full-service")
    sst.actions.set_dropdown_value(company_size_field, "N/A")
    sst.actions.set_dropdown_value(employees_field, "Less than 10")
    if aaaa_custom_field_exists:
        aaaa_custom_field = sst.actions.get_element_by_xpath('//select[@name="memberCategory"]')
        sst.actions.set_dropdown_value(aaaa_custom_field, "Not applicable")
        # Click submit button
    sst.actions.click_element(submit_button_page2)
    sst.actions.stop()

class AlchemyConnectionTest(unittest.TestCase):

    def testCreateConnection(self):
        test_conn = AlchemyConnection()
        cur = test_conn.getCursor()
        cur.execute('SELECT brief_name, full_brief_name from brief where briefid = %s', BRIEF_IDS['AAAA'])
        results = []  # will be list of
        for row in cur:
            results.append(row['brief_name'])
        cur.close()
        test_conn.close()
        self.assertListEqual(results, ['AAAA'], "Connection to database failed")  # TODO better asserts case

class SubscriberTest(unittest.TestCase):
    """
    Create a user and subscribe them to AAAA
    """
    def testCreateSubscriber(self):
        """
        Test the function of saving a subscriber. Test verifies that subscriber
        was saved by looking at the value for the 'first_name' key
        in the Python dictionary named data. In this case the value should be
        'Save'. This test will fail of the subscriber is modified after the fact.
        """

        data = {
            'email': 'save_subscriber_' + id_generator() + '@smartbrief.com',
            'first_name': 'Save',
            'last_name': 'Subscriber',
            'title': 'Selenium Tester',
        }

        subscriber = usergen.FeedbackSubscriber(**data)
        subscriber = subscriber.__dict__
        createAAAASubscriberViaWeb(**subscriber)
        test_conn = AlchemyConnection()
        cur = test_conn.getCursor()
        sql = 'SELECT top 250 * from subscriber where email = \'%s\'' % subscriber['email']
        cur.execute(sql)
        logging.info("""[new subscriber] email = {email}
                     """.format(email=subscriber['email']))
        results = []  # will be list of
        for row in cur:
            results.append(row['email'])
        cur.close()
        test_conn.close()
        self.assertListEqual(results, [subscriber['email']], "Test failure. Is there one row for email = " + subscriber['email'])

    # def testMergeSubscriber(self):
    #     """
    #     feedback-merge-livelookup@smartbrief.com into feedback-profiletest@smartbrief.com
    #     """
    #     feedback_merge_livelookup = {
    #         'subscriberid': 'DD0911EB-660A-4DBA-9475-1EC4B0306A24',
    #         'email': 'feedback-merge-livelookup@smartbrief.com',
    #     }
    #
    #     feedback_profiletest = {
    #         'subscriberid': '',
    #
    #     }




def main():
    logging.basicConfig(filename='feedback_test.log', level=logging.INFO)
    logging.info('Starting feedback test.')
    unittest.main()
    logging.info('Finished')


if __name__ == '__main__':
    main()