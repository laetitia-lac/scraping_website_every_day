import urllib.request
from urllib.error import URLError, HTTPError, ContentTooShortError

from utils.logger import logger


def download(url, user_agent='wswp', nb_retries=3):
    """
    Get the content of page (as bytes) or None if unsuccessful
    :param url: (str) to scrap
    :param user_agent: (str) name of the user agent
    :param nb_retries: (int) nb of times we can try to scrap the website if the error was due to the server
    :return: (bytes or None)
    """
    logger.info(f'Downloading this: {url}')
    request = urllib.request.Request(url)
    request.add_header('User-agent', user_agent)
    try:
        html = urllib.request.urlopen(request).read()
    except (URLError, HTTPError, ContentTooShortError) as e:
        logger.error(f'Downloading error: {e.reason}')
        html = None
        if nb_retries > 0:
            if hasattr(e, 'code') and 500 <= e.code < 600:
                # recursively retry 5xx HTTP errors
                return download(url, user_agent, nb_retries - 1)
    finally:
        return html


def test_download_content_websites():
    assert download(r'http://httpstat.us/500') is None
    assert download(r'http://www.meetup.com/') is not None


if __name__ == '__main__':
    test_download_content_websites()
