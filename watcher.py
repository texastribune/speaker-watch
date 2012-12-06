import os
import time
import sys

from pyquery import PyQuery as pq
from twilio.rest import TwilioRestClient

client = TwilioRestClient(os.environ['TWILIO_ACCOUNT_SID'],
        os.environ['TWILIO_AUTH_TOKEN'])

SPEAKER_URL = 'http://www.ethics.state.tx.us/dfs/spk_lists.htm'
FROM_PHONE_NUMBER = os.environ.get('FROM_NUMBER', '+14155992671')
NUMBERS_TO_NOTIFY = ["+1%s" % a for a in
        os.environ['NUMBERS_TO_NOTIFY'].split(',')]

def send(body):
    for a in NUMBERS_TO_NOTIFY:
        client.sms.messages.create(to=a, from_=FROM_PHONE_NUMBER, body=body)


def main():
    try:
        found = []
        while True:
            doc = pq(url=SPEAKER_URL)
            new_speaker_names = [a.text for a in
                    doc.find('#content blockquote h3')]

            if found == []:
                found = new_speaker_names
                print("Currently {0} speakers running".format(len(found)))
            elif new_speaker_names != found:
                found = new_speaker_names
                print "New Speakers Found!!!!"
                print "%s" % "; ".join(new_speaker_names)
                send("New Speakers: %s" % "; ".join(new_speaker_names))
            sys.stdout.write('.')
            sys.stdout.flush()
            time.sleep(15)
    except KeyboardInterrupt:
        print "Stopping..."



if __name__ == '__main__':
    main()
