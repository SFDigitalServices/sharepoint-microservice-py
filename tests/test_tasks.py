"""Tests for tasks.py"""
# pylint: disable=redefined-outer-name,unused-import,unused-argument

import json
from unittest.mock import patch
import jsend
import pytest
from falcon import testing
from tests import mocks
from tests.fixtures import env_vars
from tasks import upload_file

TEST_PDF = 'tests/resources/fake_file.pdf'

@patch('service.resources.graph.file.requests.request')
@patch('service.resources.graph.file.requests.get')
@patch('service.resources.graph.common.requests.request')
@patch('service.resources.graph.common.msal.ConfidentialClientApplication')
def test_upload_file_silent_success(
    mock_graph_client,
    mock_request,
    mock_get,
    mock_put,
    env_vars):
    """ test file upload with successful retrieval of access token via acquire_token_silent """
    mock_graph_client.return_value.acquire_token_silent.return_value = mocks.ACCESS_TOKEN
    mock_request.side_effect = [
        mocks.SITE_INFO,
        mocks.DRIVE_INFO,
        mocks.UPLOAD_SESSION
    ]
    with open(TEST_PDF, 'rb') as f: # pylint:disable=invalid-name
        mock_get.return_value.content = f.read()

        upload_file.s(
            site_name="foo",
            source_url="http://foo.com/file.pdf",
            destination_path="http://final.destination.com/file.pdf"
        ).apply()

@patch('service.resources.graph.file.requests.request')
@patch('service.resources.graph.file.requests.get')
@patch('service.resources.graph.common.requests.request')
@patch('service.resources.graph.common.msal.ConfidentialClientApplication')
def test_upload_file_success(
    mock_graph_client,
    mock_request,
    mock_get,
    mock_put,
    env_vars):
    """ test file upload with successful retrieval of access token via acquire_token_for_client """
    mock_graph_client.return_value.acquire_token_silent.return_value = None
    mock_graph_client.return_value.acquire_token_for_client.return_value = mocks.ACCESS_TOKEN
    mock_request.side_effect = [
        mocks.SITE_INFO,
        mocks.DRIVE_INFO,
        mocks.UPLOAD_SESSION
    ]
    with open(TEST_PDF, 'rb') as f: # pylint:disable=invalid-name
        mock_get.return_value.content = f.read()

        upload_file.s(
            site_name="foo",
            source_url="http://foo.com/file.pdf",
            destination_path="http://final.destination.com/file.pdf"
        ).apply()

@patch('service.resources.graph.file.requests.request')
@patch('service.resources.graph.file.requests.get')
@patch('service.resources.graph.common.requests.request')
@patch('service.resources.graph.common.msal.ConfidentialClientApplication')
def test_upload_file_error(
    mock_graph_client,
    mock_request,
    mock_get,
    mock_put,
    env_vars):
    """ test file upload error with failure in retrieving access token """
    mock_graph_client.return_value.acquire_token_silent.return_value = None
    mock_graph_client.return_value.acquire_token_for_client.side_effect = Exception("error")
    mock_request.side_effect = [
        mocks.SITE_INFO,
        mocks.DRIVE_INFO,
        mocks.UPLOAD_SESSION
    ]
    with open(TEST_PDF, 'rb') as f: # pylint:disable=invalid-name
        mock_get.return_value.content = f.read()

        upload_file.s(
            site_name="foo",
            source_url="http://foo.com/file.pdf",
            destination_path="http://final.destination.com/file.pdf"
        ).apply()

@patch('service.resources.graph.file.requests.request')
@patch('service.resources.graph.file.requests.get')
@patch('service.resources.graph.common.requests.request')
@patch('service.resources.graph.common.msal.ConfidentialClientApplication')
def test_upload_auth_error(
    mock_graph_client,
    mock_request,
    mock_get,
    mock_put,
    env_vars):
    """ test file upload error with failure in authentication """
    mock_graph_client.return_value.acquire_token_silent.return_value = None
    bad_access_token = mocks.ACCESS_TOKEN.copy()
    bad_access_token.pop('access_token')
    print(f"bad token: {bad_access_token}")
    mock_graph_client.return_value.acquire_token_for_client.return_value = bad_access_token
    mock_request.side_effect = [
        mocks.SITE_INFO,
        mocks.DRIVE_INFO,
        mocks.UPLOAD_SESSION
    ]
    with open(TEST_PDF, 'rb') as f: # pylint:disable=invalid-name
        mock_get.return_value.content = f.read()

        upload_file.s(
            site_name="foo",
            source_url="http://foo.com/file.pdf",
            destination_path="http://final.destination.com/file.pdf"
        ).apply()

@patch('service.resources.graph.file.requests.request')
@patch('service.resources.graph.file.requests.get')
@patch('service.resources.graph.common.requests.request')
@patch('service.resources.graph.common.msal.ConfidentialClientApplication')
def test_upload_file_cloud(
    mock_graph_client,
    mock_request,
    mock_get,
    mock_put,
    env_vars):
    """ test file upload via cloudstorage """

    mock_graph_client.return_value.acquire_token_silent.return_value = mocks.ACCESS_TOKEN
    mock_request.side_effect = [
        mocks.SITE_INFO,
        mocks.DRIVE_INFO,
        mocks.UPLOAD_SESSION
    ]
    with open(TEST_PDF, 'rb') as f: # pylint:disable=invalid-name
        mock_get.return_value.content = f.read()

        upload_file.s(
            site_name="foo",
            source_url="http://the.cloud.com/file.pdf",
            destination_path="http://final.destination.com/file.pdf"
        ).apply()
