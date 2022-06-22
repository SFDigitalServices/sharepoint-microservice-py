""" unit tests for graph_api functions """
# pylint: disable=unused-argument,unused-import,redefined-outer-name

from unittest.mock import patch
from tests.fixtures import env_vars
from tests import mocks
import service.resources.graph_api as graph

@patch('service.resources.graph_api.requests.request')
def test_list_drive_items(
    mock_get,
    env_vars):
    """ test list_drive_items function """
    mock_get.return_value.json.return_value = mocks.DRIVE_ITEMS

    items = graph.list_drive_items('drive_id', 'access_token')

    assert 'items' in items
    assert len(items['items']) > 0

@patch('service.resources.graph_api.requests.request')
def test_list_folder_items(
    mock_get,
    env_vars):
    """ test list_folder_items function """
    mock_get.return_value.json.return_value = mocks.DRIVE_ITEMS

    items = graph.list_folder_items('drive_id', 'folder_name/', 'access_token')

    assert 'items' in items
    assert len(items['items']) > 0

@patch('service.resources.graph_api.requests.request')
def test_get_item_info(
    mock_get,
    env_vars):
    """ test get_item_info function """
    mock_get.return_value.json.return_value = mocks.FILE_INFO

    info = graph.get_item_info('drive_id', 'folder_name/', 'access_token')

    assert 'id' in info
    assert  'webUrl' in info
