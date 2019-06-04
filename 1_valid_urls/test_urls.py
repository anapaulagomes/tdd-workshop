from urls import is_valid

import pytest


@pytest.mark.parametrize("url", ["http://anapaulagomes.me", "https://anapaulagomes.me"])
def test_url_is_valid(url):
    assert is_valid(url) is True, url


@pytest.mark.parametrize("url", ["anapaulagomes.me", "i-am-not-an-url"])
def test_url_is_invalid(url):
    assert is_valid(url) is False, url
