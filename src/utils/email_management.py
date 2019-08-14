#!/usr/bin/python3
import smtplib

from utils.config_management import config
from utils.logger import logger


def send_email(message: str):
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
