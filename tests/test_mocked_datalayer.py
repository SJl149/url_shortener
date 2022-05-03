import pytest

from urlshorter.datalayer.mocked_datalayer import MockedDatalayer


@pytest.fixture
def short_url():
    return "short_url.com"


@pytest.fixture
def long_url():
    return "a_very_long_url.com"


@pytest.fixture(scope="function")
def mocked_datalayer():
    return MockedDatalayer()


@pytest.fixture(scope="function")
def mocked_datalayer_with_entry(mocked_datalayer, short_url, long_url):
    mocked_datalayer.create(short_url, long_url)
    return mocked_datalayer


def test_initialize_mocked_datalayer(mocked_datalayer):
    assert len(mocked_datalayer.db) == 0, "MockedDatalayer failed to initialize an empty dict"


def test_create_new_entry_successfully(mocked_datalayer, short_url, long_url):
    db = mocked_datalayer
    response = db.create(short_url, long_url)
    assert response == True, f"Failed to create a new entry for {long_url} with short_url: {short_url}"


def test_create_new_entry_unsuccessfully_with_existing_entry(mocked_datalayer_with_entry, short_url, long_url):
    db = mocked_datalayer_with_entry
    response = db.create(short_url, long_url)
    assert response == False, "Expected duplicate entry to fail on creation"


def test_get_entry_successfully(mocked_datalayer_with_entry, short_url, long_url):
    db = mocked_datalayer_with_entry
    response = db.get(short_url)
    assert (
        response["long_url"] == long_url
    ), f"Expected response to include long_url == {long_url}, actual response: {response}"


def test_get_entry_unsuccessfully_with_empty_dict(mocked_datalayer, short_url, long_url):
    db = mocked_datalayer
    response = db.get(short_url)
    assert response == None, f"Expected GET response to be None, Actual: {response}"


def test_update_entry_successfully(mocked_datalayer_with_entry, short_url, long_url):
    db = mocked_datalayer_with_entry
    update_response = db.update(short_url, "clicked", 2)
    assert update_response == True, f"Failed to update {short_url}"
    get_response = db.get(short_url)
    assert get_response["clicked"] == 2, f"Expected clicked == 2, Actual response: {get_response}"


def test_update_entry_unsuccessfully_with_empty_dict(mocked_datalayer, short_url, long_url):
    db = mocked_datalayer
    update_response = db.update(short_url, "clicked", 2)
    assert update_response == False, f"Updated {short_url} when expected to fail"


def test_delete_entry_successfully(mocked_datalayer_with_entry, short_url):
    db = mocked_datalayer_with_entry
    delete_response = db.delete(short_url)
    assert delete_response == True, f"Failed to delete {short_url}"
    get_response = db.get(short_url)
    assert get_response == None, f"Expected GET response to be None, Actual: {get_response}"


def test_delete_entry_unsuccessfully_with_empty_dict(mocked_datalayer, short_url):
    db = mocked_datalayer
    delete_response = db.delete(short_url)
    assert delete_response == False, f"Expected response == False to delete {short_url}, Actual: True"
