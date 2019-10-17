import requests
from bs4 import BeautifulSoup
from lxml.html import fromstring

from utils.logger import logger
from utils.config_management import config


def parse_form(html: bytes) -> dict:
    """
    Extract all the input tag details of a form.
    :param html: (bytes)
    :return: (dict)
    """
    tree = fromstring(html)
    data = {}
    # iterate over input tags
    for e in tree.cssselect('form input'):
        if e.get('name'):
            data[e.get('name')] = e.get('value')
    return data


def login(session=None) -> (requests.models.Response, requests.sessions.Session):
    """
    Log in to the website.
    :param session: (request lib session object or None)
    :return: (response, session)
    """
    # get the login form
    if session is None:
        html = requests.get(config['WEBSITE']['LOGIN_URL'])
    else:
        html = session.get(config['WEBSITE']['LOGIN_URL'])

    # build the form to send for logging
    data = parse_form(html.content)
    data['Email'] = config['WEBSITE']['USER']
    data['Password'] = config['WEBSITE']['PASSWORD']

    # log in
    if session is None:
        response = requests.post(config['WEBSITE']['LOGIN_URL'], data, cookies=html.cookies)
    else:
        response = session.post(config['WEBSITE']['LOGIN_URL'], data)

    # check login successful
    assert 'login' not in response.url.lower()
    return response, session


def get_content_list_projects():
    """
    Get the content of the list of projects
    :return: (str which is the content of the first row of 'tab-content' or None)
    """
    session = requests.Session()
    try:
        # log in
        _, session = login(session)
        # get content of list projects
        page_html = session.get(config['WEBSITE']['PROJECTS_INDEX_URL'])
        soup = BeautifulSoup(page_html.text, 'html5lib')
        first_row_tab_content = soup.find(attrs={'class': 'tab-content'}).find(attrs={'class': 'row'})
        return first_row_tab_content.text.strip()
    except AssertionError:
        logger.error('Login unsuccessful')


if __name__ == '__main__':
    assert get_content_list_projects() == "Il n'y a pas de projet à traiter pour le moment."
