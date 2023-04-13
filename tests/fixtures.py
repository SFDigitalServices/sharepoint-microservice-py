""" Test fixtures """

import pytest

@pytest.fixture
def env_vars(monkeypatch):
    """ mock environment variables """
    monkeypatch.setenv("CLOUDSTORAGE_DOMAIN", "the.cloud.com")
    monkeypatch.setenv("CLOUDSTORAGE_URL", "https://the.cloud.com")
    monkeypatch.setenv("CLOUDSTORAGE_API_KEY", "abc123")
    monkeypatch.setenv("SHAREPOINT_HOST_NAME", "foo.sharepoint.com")
    monkeypatch.setenv("SHAREPOINT_CLIENT_ID", "123-456-789")
    monkeypatch.setenv("SHAREPOINT_CLIENT_SECRET", "xxxwrtasdfjkl")
    monkeypatch.setenv("SHAREPOINT_TENANT_ID", "abc-def")
