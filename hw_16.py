import logging
import requests
from requests.exceptions import HTTPError

# Задание 1
# logging.basicConfig(
#     level=logging.INFO,
#     format='%(asctime)s - %(filename)s - %(levelname)s -  %(message)s - %(lineno)d',
#     datefmt='%Y-%m-%d %H:%M:%S'
# )
#
# logging.info('hello world')

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler('test_results.log', encoding='utf-8')
file_handler.setLevel(logging.DEBUG)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

logger.addHandler(file_handler)
logger.addHandler(console_handler)

def log_status_code(url):
    logger.info('Sending requests')
    expected_status_code = 200

    try:
        response = requests.get(url)
        logger.debug(f'URL: {url}. Status: {response.status_code}. Expected: {expected_status_code}')
        assert response.status_code == expected_status_code, (f'Expected {expected_status_code}, '
                                             f'got {response.status_code}')
    except AssertionError:
        logger.exception('Тест FAILED')
        raise

    try:
        response = requests.post(url)
        response.raise_for_status()
        logger.debug(f'URL: {url}. Status: {response.status_code}. Expected: {expected_status_code}')

    except HTTPError:
        logger.exception('Тест FAILED')

log_status_code('https://www.google.com/')


