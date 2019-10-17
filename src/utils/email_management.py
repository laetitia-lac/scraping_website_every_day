#!/usr/bin/python3
import os
import os.path
import pickle
import smtplib
from base64 import urlsafe_b64encode
from email.mime.text import MIMEText

from apiclient import errors
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

from utils.config_management import config
from utils.logger import logger


def send_email(message: str):
    if config['ENVIRONMENT']['MODE'] == 'debug':
        return send_debug_email(message)
    elif config['ENVIRONMENT']['MODE'] == 'production':
        return send_production_email(message)


def send_debug_email(message: str):
    """
    Simulate the sending of an email via a local SMTP debugging server
    :param message: (str)
    :return: (None)
    """
    try:
        with smtplib.SMTP(config['EMAIL']['HOST'], config['EMAIL']['PORT']) as server:
            sender = config['EMAIL']['SENDER_ADDRESS']
            receivers = [config['EMAIL']['RECEIVER_ADDRESS']]
            server.sendmail(sender, receivers, message)
            logger.debug('Successfully sent email')
    except smtplib.SMTPException:
        logger.exception('Unable to send the email')
    except ConnectionRefusedError:
        logger.exception('Unable server')


def send_production_email(message: str):
    """
    Send an email via Google API.
    :param message: (str) content of the email
    :return:
    """
    # If modifying these scopes, delete the file token.pickle.
    scopes = ['https://www.googleapis.com/auth/gmail.send']
    creds = None

    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', scopes)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    # get the service
    service = build('gmail', 'v1', credentials=creds, cache_discovery=False)
    # call the gmail API
    message_to_send = create_message_object(config['EMAIL']['SENDER_ADDRESS'], config['EMAIL']['RECEIVER_ADDRESS'],
                                            'Scraping Website', message)
    try:
        message = (service.users().messages().send(userId='me', body=message_to_send).execute())
        logger.debug(f"Message Id: {message['id']}")
    except errors.HttpError as error:
        logger.error(f"An error occurred: {error}")


def create_message_object(sender: str, receiver: str, subject: str, message_text: str) -> dict:
    """
    Create a message object to provide to Google API
    :param sender: (str) email address
    :param receiver: (str) email address
    :param subject: (str)
    :param message_text: (str)
    :return: (dict)
    """
    message = MIMEText(message_text)
    message['to'] = receiver
    message['from'] = sender
    message['subject'] = subject
    encoded_message = urlsafe_b64encode(message.as_bytes())
    return {'raw': encoded_message.decode()}


if __name__ == '__main__':
    send_email('Test this message')
