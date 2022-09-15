""" unit tests for graph_api functions """
# pylint: disable=unused-argument,unused-import,redefined-outer-name

from unittest.mock import patch
import requests
from requests import Response
from tests.fixtures import env_vars
from tests import mocks
from service.resources.graph import file, list as sharepoint_list

@patch('service.resources.graph.file.requests.request')
def test_list_drive_items(
    mock_get,
    env_vars):
    """ test list_drive_items function """
    mock_get.return_value.json.return_value = mocks.DRIVE_ITEMS

    items = file.list_drive_items('drive_id', 'access_token')

    assert 'items' in items
    assert len(items['items']) > 0

@patch('service.resources.graph.file.requests.request')
def test_list_folder_items(
    mock_get,
    env_vars):
    """ test list_folder_items function """
    mock_get.return_value.json.return_value = mocks.DRIVE_ITEMS

    items = file.list_folder_items('drive_id', 'folder_name/', 'access_token')

    assert 'items' in items
    assert len(items['items']) > 0

@patch('service.resources.graph.file.requests.request')
def test_get_item_info(
    mock_get,
    env_vars):
    """ test get_item_info function """
    mock_get.return_value.json.return_value = mocks.FILE_INFO

    info = file.get_item_info('drive_id', 'folder_name/', 'access_token')

    assert 'id' in info
    assert  'webUrl' in info

@patch('service.resources.graph.file.requests.request')
def test_get_site_lists(
    mock_request,
    env_vars):
    """ test get_site_lists function """
    mock_request.return_value.json.return_value = mocks.GET_LISTS_RESPONSE

    lists = sharepoint_list.get_site_lists('site_id', 'access_token')

    assert len(lists) > 0

@patch('service.resources.graph.file.requests.request')
def test_create_site_list(
    mock_request,
    env_vars):
    """ test create_site_list function """
    mock_request.return_value.json.return_value = mocks.CREATE_LIST_RESPONSE

    resp = sharepoint_list.create_site_list('site_id', mocks.LIST_DEFINITION, 'access_token')
    assert resp["id"]

@patch('service.resources.graph.file.requests.request')
def test_get_list_items(
    mock_request,
    env_vars):
    """ test retrieval of list items function"""
    mock_request.return_value.json.return_value = mocks.GET_LIST_ITEMS_RESPONSE

    items = sharepoint_list.get_list_items('site_id', 'list_identifier', 'access_token')
    assert len(items) > 0

@patch('service.resources.graph.file.requests.request')
def test_get_list_item(
    mock_request,
    env_vars):
    """ test retrieval of list item function"""
    mock_request.return_value.json.return_value = mocks.GET_SINGLE_ITEM_RESPONSE

    item = sharepoint_list.get_list_item('site_id', 'list_identifier', 'access_token', 50)
    assert item['id'] == "50"

@patch('service.resources.graph.file.requests.request')
def test_get_list_columns(
    mock_request,
    env_vars):
    """ test retrieval of list columns function """
    mock_request.return_value.json.return_value = mocks.GET_LIST_COLUMNS_RESPONSE

    columns = sharepoint_list.get_list_columns('site_id', 'list_identifier', 'access_token')
    assert len(columns) > 0

@patch('service.resources.graph.file.requests.request')
def test_update_list_item(
    mock_request,
    env_vars):
    """ test update_list_item function """
    mock_request.return_value.json.return_value = mocks.UPDATE_ITEM_RESPONSE

    update_response = sharepoint_list.update_list_item(
        'site_id',
        'list_identifier',
        'item_id',
        mocks.UPDATE_ITEM_REQUEST, 'access_token'
    )

    assert 'id' in update_response
    for prop, val in mocks.UPDATE_ITEM_REQUEST.items():
        assert update_response[prop] == val

@patch('service.resources.graph.file.requests.request')
def test_delete_list_item(
    mock_request,
    env_vars):
    """ test delete_list_item function """
    empty_resp = Response()
    empty_resp.status_code = requests.codes['no_content']
    mock_request.return_value = empty_resp

    sharepoint_list.delete_list_item('site_id', 'list_identifier', 'item_id', 'access_token')
