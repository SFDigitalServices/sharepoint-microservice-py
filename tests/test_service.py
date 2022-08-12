# pylint: disable=redefined-outer-name
"""Tests for microservice"""
import json
from unittest.mock import patch, Mock
import jsend
import pytest
from falcon import testing
import service.microservice
from tests import mocks

# pylint: disable=unused-argument

CLIENT_HEADERS = {
    "ACCESS_KEY": "1234567"
}

@pytest.fixture()
def client():
    """ client fixture """
    return testing.TestClient(app=service.microservice.start_service(), headers=CLIENT_HEADERS)

@pytest.fixture
def mock_env_access_key(monkeypatch):
    """ mock environment access key """
    monkeypatch.setenv("ACCESS_KEY", CLIENT_HEADERS["ACCESS_KEY"])

@pytest.fixture
def mock_env_no_access_key(monkeypatch):
    """ mock environment with no access key """
    monkeypatch.delenv("ACCESS_KEY", raising=False)

def test_welcome(client, mock_env_access_key):
    # pylint: disable=unused-argument
    # mock_env_access_key is a fixture and creates a false positive for pylint
    """Test welcome message response"""
    response = client.simulate_get('/welcome')
    assert response.status_code == 200

    expected_msg = jsend.success({'message': 'Welcome'})
    assert json.loads(response.content) == expected_msg

    # Test welcome request with no ACCESS_KEY in header
    client_no_access_key = testing.TestClient(service.microservice.start_service())
    response = client_no_access_key.simulate_get('/welcome')
    assert response.status_code == 403

def test_welcome_no_access_key(client, mock_env_no_access_key):
    # pylint: disable=unused-argument
    # mock_env_no_access_key is a fixture and creates a false positive for pylint
    """Test welcome request with no ACCESS_key environment var set"""
    response = client.simulate_get('/welcome')
    assert response.status_code == 403

def test_default_error(client, mock_env_access_key):
    # pylint: disable=unused-argument
    """Test default error response"""
    response = client.simulate_get('/some_page_that_does_not_exist')

    assert response.status_code == 404

    expected_msg_error = jsend.error('404 - Not Found')
    assert json.loads(response.content) == expected_msg_error

@patch('tasks.upload_file.apply_async')
@patch('requests.head')
def test_sharepoint_file_upload(
    mock_requests_head,
    mock_upload_apply_async,
    client,
    mock_env_access_key):
    """ Test file upload endpoint """

    # happy path
    response = client.simulate_put(
        '/sharepoint/sfds_site/files',
        json={
            'source_url': 'https://sfgov.org/hello_world.pdf',
            'destination_path': 'folder1/folder2/hello_world.pdf'
        }
    )
    assert response.status_code == 200

    # missing source_url
    response = client.simulate_put(
        '/sharepoint/sfds_site/files',
        json={
            'destination_path': 'folder1/folder2/hello_world.pdf'
        }
    )
    assert response.status_code == 500

    # missing destination_path
    response = client.simulate_put(
        '/sharepoint/sfds_site/files',
        json={
            'source_url': 'https://sfgov.org/hello_world.pdf'
        }
    )
    assert response.status_code == 500

@patch('service.resources.graph.common.requests.request')
@patch('service.resources.graph.common.msal.ConfidentialClientApplication')
def test_sharepoint_add_list_item(
    mock_graph_client,
    mock_request,
    client,
    mock_env_access_key):
    """ Test endpoint to add a list item to an existing list """
    mock_graph_client.return_value.acquire_token_silent.return_value = mocks.ACCESS_TOKEN
    mock_get_site_info = Mock()
    mock_get_site_info.json.return_value = mocks.SITE_INFO
    mock_add_item = Mock()
    mock_add_item.json.return_value = mocks.ADD_ITEM_RESPONSE
    mock_request.side_effect = [
        mock_get_site_info,
        mock_add_item
    ]

    response = client.simulate_post(
        '/sharepoint/sfds_site/lists/list_name/items',
        json=mocks.LIST_ITEM
    )
    assert response.status_code == 200

@patch('service.resources.graph.common.requests.request')
@patch('service.resources.graph.common.msal.ConfidentialClientApplication')
def test_sharepoint_add_list_item_error(
    mock_graph_client,
    mock_request,
    client,
    mock_env_access_key):
    """ Test error case when adding a list item to an existing list """
    mock_graph_client.return_value.acquire_token_silent.return_value = mocks.ACCESS_TOKEN
    mock_get_site_info = Mock()
    mock_get_site_info.json.return_value = mocks.SITE_INFO
    mock_request.side_effect = [
        mock_get_site_info,
        Exception('Error')
    ]

    response = client.simulate_post(
        '/sharepoint/sfds_site/lists/list_name/items',
        json=mocks.LIST_ITEM
    )
    assert response.status_code == 500

@patch('service.resources.graph.common.requests.request')
@patch('service.resources.graph.common.msal.ConfidentialClientApplication')
def test_sharepoint_subsite_add_list_item(
    mock_graph_client,
    mock_request,
    client,
    mock_env_access_key):
    """ Test endpoint to add a list item to an existing subsite list """
    mock_graph_client.return_value.acquire_token_silent.return_value = mocks.ACCESS_TOKEN

    mock_get_site_info = Mock()
    mock_get_site_info.json.return_value = mocks.SITE_INFO
    mock_get_subsites = Mock()
    mock_get_subsites.json.return_value = mocks.SUBSITES
    mock_add_item = Mock()
    mock_add_item.json.return_value = mocks.ADD_ITEM_RESPONSE
    mock_request.side_effect = [
        mock_get_site_info,
        mock_get_subsites,
        mock_add_item
    ]

    response = client.simulate_post(
        '/sharepoint/sfds_site/sites/Team B Subsite/lists/list_name/items',
        json=mocks.LIST_ITEM
    )
    assert response.status_code == 200

@patch('service.resources.graph.common.requests.request')
@patch('service.resources.graph.common.msal.ConfidentialClientApplication')
def test_sharepoint_subsite_add_list_item_error(
    mock_graph_client,
    mock_request,
    client,
    mock_env_access_key):
    """ Test error case when adding a list item to an existing subsite list """
    mock_graph_client.return_value.acquire_token_silent.return_value = mocks.ACCESS_TOKEN

    mock_get_site_info = Mock()
    mock_get_site_info.json.return_value = mocks.SITE_INFO
    mock_get_subsites = Mock()
    mock_get_subsites.json.return_value = mocks.SUBSITES
    mock_request.side_effect = [
        mock_get_site_info,
        mock_get_subsites,
        Exception('Error')
    ]

    response = client.simulate_post(
        '/sharepoint/sfds_site/sites/Team B Subsite/lists/list_name/items',
        json=mocks.LIST_ITEM
    )
    assert response.status_code == 500

    # test subsite not found
    mock_add_item = Mock()
    mock_add_item.json.return_value = mocks.ADD_ITEM_RESPONSE
    mock_request.side_effect = [
        mock_get_site_info,
        mock_get_subsites,
        mock_add_item
    ]

    response_invalid_subsite = client.simulate_post(
        '/sharepoint/sfds_site/sites/Team Z Subsite/lists/list_name/items',
        json=mocks.LIST_ITEM
    )
    assert response_invalid_subsite.status_code == 500
