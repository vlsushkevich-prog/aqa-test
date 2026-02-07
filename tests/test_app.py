import pytest
from src.app import process_files, read_config, generate_password


def test_process_files(mocker):
    mock_sleep = mocker.patch('src.app.time.sleep')
    mock_sleep.return_value = 0

    assert process_files() == 'processed'
    mock_sleep.assert_called_once_with(3)

def test_read_config(mocker):
    mock_file = mocker.patch('src.app.open', mocker.mock_open(read_data="host=localhost"))

    assert read_config('config.txt') == 'host=localhost'
    mock_file.assert_called_once_with('config.txt', 'r')

def test_generate_password(mocker):
    mock_random = mocker.patch('src.app.random.choice', side_effect='aaaabbbb')

    assert generate_password() == 'aaaabbbb'
    assert mock_random.call_count == 8