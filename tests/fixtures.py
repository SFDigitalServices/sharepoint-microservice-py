""" Test fixtures """

import pytest

@pytest.fixture
def env_vars(monkeypatch):
    """ mock environment variables """
    monkeypatch.setenv("CLOUDSTORAGE_DOMAIN", "the.cloud.com")
    monkeypatch.setenv("CLOUDSTORAGE_URL", "https://the.cloud.com")
    monkeypatch.setenv("CLOUDSTORAGE_API_KEY", "abc123")
