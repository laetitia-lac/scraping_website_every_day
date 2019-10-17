from pprint import pprint

import requests
from bs4 import BeautifulSoup

from core.scraping import parse_form, login
from utils.config_management import config
from utils.logger import logger


def test_parse_broken_html():
    broken_html = '<ul class=grocery_list><li>Noodles<li>Bread</ul>'
    soup = BeautifulSoup(broken_html, 'html5lib')
    fixed_html = soup.prettify()
    pprint(fixed_html)


def test_get_required_fields_for_login_form():
    html = requests.get(config['WEBSITE']['LOGIN_URL'])
    form = parse_form(html.content)

    assert_response = form == {'Email': '', 'Password': None}
    logger.debug(f"form == {{'Email': '', 'Password': None}} : {assert_response}")
    assert assert_response


def test_succeed_identification():
    session = requests.Session()
    response, session = login(session)

    assert_response = response.url == config['WEBSITE']['HOMEPAGE_URL']
    logger.debug(f"response.url == config['WEBSITE']['HOMEPAGE_URL']: {assert_response}")
    assert assert_response


def test_get_content_inside_projects_index():
    session = requests.Session()
    _, session = login(session)
    response_html = session.get(config['WEBSITE']['PROJECTS_INDEX_URL'])
    soup = BeautifulSoup(response_html.text, 'html5lib')
    tr_first_row = soup.find(attrs={'class': 'tab-content'}).find(attrs={'class': 'row'})

    assert_response = tr_first_row.text.strip()
    logger.debug(f"content of the first row: {assert_response}")
    assert assert_response


if __name__ == '__main__':
    test_get_required_fields_for_login_form()
    test_succeed_identification()
    test_get_content_inside_projects_index()
