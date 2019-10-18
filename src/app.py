import datetime

from core.scraping import get_content_list_projects
from utils.email_management import send_email
from utils.logger import logger

if __name__ == '__main__':
    content_list_projects = get_content_list_projects()

    if content_list_projects != "Il n'y a pas de projet à traiter pour le moment.":
        content_email = f'List of projects is not empty, first project: {content_list_projects}'
        logger.debug(content_email)
        send_email(content_email)
    else:
        logger.debug(f'No project available at: {datetime.datetime.now()}')
