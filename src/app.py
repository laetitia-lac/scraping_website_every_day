#!/usr/bin/python3
from utils.email_management import send_email

message = """From: From Person <from@fromdomain.com>
To: To Person <to@todomain.com>
Subject: SMTP e-mail test

This is a test e-mail message.
"""

if __name__ == '__main__':
    send_email(message)
