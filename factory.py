from tests import *
import logging

def id_generator(size=6, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))

def testMergeSubscriber():
    """
    feedback-merge-livelookup@smartbrief.com into feedback-profiletest@smartbrief.com
    """
    logging.info("BEGINNING MERGE TEST")

    change_this_subscriber = {
        'email': 'changesubscriber' + id_generator() + '@smartbrief.com',
        'first_name': 'ChangeThis',
        'last_name': 'Subscriber',
        'title': 'Giver',
        'city': 'Mexico City',
        'country': 'Mexico'
    }

    change_this_subscriber = usergen.FeedbackSubscriber(**change_this_subscriber)
    change_this_subscriber = change_this_subscriber.__dict__
    createAAAASubscriberViaWeb(**change_this_subscriber)
    #change_this_subscriber.__setattr__(self, 'subscriberid', getSubscriberId(**change_this_subscriber))
    change_this_subscriber['subscriberid'] = getSubscriberId(**change_this_subscriber)  # set subscriberid

    logging.info("""[new subscriber] email = {email}\
                     """.format(email=change_this_subscriber['email']))

    merge_into_subscriber = {
        'email': 'mergeinto' + id_generator() + '@smartbrief.com',
        'first_name': 'MergeIntoThis',
        'last_name': 'Subscriber',
        'title': 'Receiver',
        'city': 'Mexico City',
        'country': 'Mexico'
    }

    merge_into_subscriber = usergen.FeedbackSubscriber(**merge_into_subscriber)
    merge_into_subscriber = merge_into_subscriber.__dict__
    createCIASubscriberViaWeb(**merge_into_subscriber)
    merge_into_subscriber['subscriberid'] = getSubscriberId(**merge_into_subscriber)  # set subscriberid
    logging.info("""[new subscriber] email = {email}\
                     """.format(email=merge_into_subscriber['email']))
    addSubscription(BRIEF_IDS['CIA10/8/2007'], **change_this_subscriber)
    addSubscription(BRIEF_IDS['AAAA10/3/2006'], **merge_into_subscriber)
    addSubscription(BRIEF_IDS['AAAA1/21/2009'], **merge_into_subscriber)


def main():
    print datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    logging.basicConfig(filename='feedback_test.log', level=logging.INFO)
    logging.info("""========STARTING TEST========
                 """ + datetime.datetime.now().strftime("%Y-%m-%d %H:%M"))
    cycles = 50
    while cycles > 0:
        testMergeSubscriber()
        cycles -= 1
    print 'Ending...'

if __name__ == '__main__':
    main()
