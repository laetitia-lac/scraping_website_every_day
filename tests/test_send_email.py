#!/usr/bin/python3
from utils.email_management import send_debug_email, send_production_email

message = """From: From Person <from@fromdomain.com>
To: To Person <to@todomain.com>
Subject: SMTP e-mail test

This is a test e-mail message.
"""


def test_send_debug_email():
    send_debug_email(message)


def test_send_production_email():
    send_production_email('Production email test')


if __name__ == '__main__':
    test_send_debug_email()
    test_send_production_email()
