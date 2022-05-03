import pytest

from urlshorter.datalayer.mocked_datalayer import MockedDatalayer
from urlshorter.shortener.urlshorter_engine import URLShorterEngine


@pytest.fixture
def key():
    return "abc123"


@pytest.fixture
def custom_key():
    return "myurl1"


@pytest.fixture
def long_url():
    return "www.myverylongcompanyname.com"


@pytest.fixture(scope="function")
def mocked_datalayer():
    return MockedDatalayer()


@pytest.fixture(scope="function")
def mocked_datalayer_with_entry(mocked_datalayer, key, long_url):
    mocked_datalayer.create(key, long_url)
    return mocked_datalayer


@pytest.fixture(scope="function")
def url_shorter_engine(mocked_datalayer):
    return URLShorterEngine(datalayer=mocked_datalayer)


@pytest.fixture(scope="function")
def engine_with_existing_entry(mocked_datalayer, key, long_url):
    mocked_datalayer = MockedDatalayer()
    mocked_datalayer.create(key, long_url)
    return URLShorterEngine(datalayer=mocked_datalayer)
