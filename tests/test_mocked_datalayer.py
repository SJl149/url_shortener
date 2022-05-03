import pytest

from urlshorter.datalayer.mocked_datalayer import MockedDatalayer


@pytest.fixture
def key():
    return "abc123"


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


def test_initialize_mocked_datalayer(mocked_datalayer):
    assert len(mocked_datalayer.db) == 0, "MockedDatalayer failed to initialize an empty dict"


def test_create_new_entry_successfully(mocked_datalayer, key, long_url):
    db = mocked_datalayer
    response = db.create(key, long_url)
    assert response == True, f"Failed to create a new entry for {long_url} with key: {key}"


def test_create_new_entry_unsuccessfully_with_existing_entry(mocked_datalayer_with_entry, key, long_url):
    db = mocked_datalayer_with_entry
    response = db.create(key, long_url)
    assert response == False, "Expected duplicate entry to fail on creation"


def test_get_entry_successfully(mocked_datalayer_with_entry, key, long_url):
    db = mocked_datalayer_with_entry
    response = db.get(key)
    assert (
        response["long_url"] == long_url
    ), f"Expected response to include long_url == {long_url}, actual response: {response}"


def test_get_entry_unsuccessfully_with_empty_dict(mocked_datalayer, key, long_url):
    db = mocked_datalayer
    response = db.get(key)
    assert response == None, f"Expected GET response to be None, Actual: {response}"


def test_update_entry_successfully(mocked_datalayer_with_entry, key, long_url):
    db = mocked_datalayer_with_entry
    update_response = db.update(key, "clicked", 2)
    assert update_response == True, f"Failed to update {key}"
    get_response = db.get(key)
    assert get_response["clicked"] == 2, f"Expected clicked == 2, Actual response: {get_response}"


def test_update_entry_unsuccessfully_with_empty_dict(mocked_datalayer, key, long_url):
    db = mocked_datalayer
    update_response = db.update(key, "clicked", 2)
    assert update_response == False, f"Updated {key} when expected to fail"


def test_delete_entry_successfully(mocked_datalayer_with_entry, key):
    db = mocked_datalayer_with_entry
    delete_response = db.delete(key)
    assert delete_response == True, f"Failed to delete {key}"
    get_response = db.get(key)
    assert get_response == None, f"Expected GET response to be None, Actual: {get_response}"


def test_delete_entry_unsuccessfully_with_empty_dict(mocked_datalayer, key):
    db = mocked_datalayer
    delete_response = db.delete(key)
    assert delete_response == False, f"Expected response == False to delete {key}, Actual: True"
