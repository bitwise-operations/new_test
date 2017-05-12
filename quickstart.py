
from __future__ import print_function
import httplib2
import os

import datetime
import re

from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage

try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

# If modifying these scopes, delete your previously saved credentials
# at ~/.credentials/gmail-python-quickstart.json
SCOPES = 'https://www.googleapis.com/auth/gmail.readonly'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'Gmail API Python Quickstart'


def get_credentials():
    """Gets valid user credentials from storage.

    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.

    Returns:
        Credentials, the obtained credential.
    """
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir,
                                   'gmail-python-quickstart.json')

    store = Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else: # Needed only for compatibility with Python 2.6
            credentials = tools.run(flow, store)
        print('Storing credentials to ' + credential_path)
    return credentials

def main():
    """Shows basic usage of the Gmail API.

    Creates a Gmail API service object and outputs a list of label names
    of the user's Gmail account.
    """
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('gmail', 'v1', http=http)
    query='from:noreply@level.travel'

    response = service.users().messages().list(userId='me',
                                              q=query).execute()
    
    for i in range(len(response['messages'])):
        a = response['messages'][i]['id']        
        message = service.users().messages().get(userId='me', id=a,
                                                 format='full').execute()
        timestamp = int(message['internalDate']) / 1000
        datetimemessage = datetime.datetime.fromtimestamp(timestamp)
        today = datetime.date.today()
        datemessade = datetimemessage.date()
        timemessage = datetimemessage.time()
        start = datetime.time(9, 00, 00)
        end = datetime.time(10, 00, 00)
        if datemessade == today and start < timemessage < end:
            bodymessage = message['snippet']
            check_text = 'Есть выгодные предложения по турам в'
            re.search(check_text, bodymessage)
            p = re.compile(r'^(.*)Есть выгодные предложения по турам в(.*)')
            search_text = p.search(bodymessage)
            print(search_text.group())


if __name__ == '__main__':
    main()