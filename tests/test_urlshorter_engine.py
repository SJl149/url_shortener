def test_urlshorter_generate_random_key(url_shorter_engine):
    random_key = url_shorter_engine._generate_random_key()
    assert len(random_key) == 6, "Expected random key to have length = 6"
    assert random_key.isalnum(), "Expected random key to be alphanumeric"


def test_add_with_custom_key_successful(url_shorter_engine, custom_key, long_url):
    engine = url_shorter_engine
    response = engine.add_with_custom_key(custom_key, long_url)
    assert response == custom_key, "Expected custom key to be added to datalayer"


def test_add_with_custom_key_unsuccessful_with_existing_key(engine_with_existing_entry, key, long_url):
    engine = engine_with_existing_entry
    response = engine.add_with_custom_key(key, long_url)
    assert response is None, "Expected creating entry for url with existing key to fail"


def test_add_with_custom_key_unsuccessful_with_incorrect_key_length(url_shorter_engine, long_url):
    engine = url_shorter_engine
    response = engine.add_with_custom_key(custom_key="thisurlistoolong", long_url=long_url)
    assert response is None, "Expected creating entry for custom key with length greater than 6 to fail"


def test_urlshorter_get_unique_random_key_returns_random_key(url_shorter_engine):
    key = url_shorter_engine._get_unique_random_key()
    assert len(key) == 6, "Expected random key to return"


def test_add_with_random_key_successful(url_shorter_engine, long_url):
    engine = url_shorter_engine
    random_key = engine.add_with_random_key(long_url)
    assert len(random_key) == 6, "Expected add_with_random_key to be successful"
    get_response = engine.datalayer.get(random_key)
    assert get_response.get("long_url", None) == long_url, f"Expected GET to return long_url: {long_url}"


def test_delete_url_successful(engine_with_existing_entry, key):
    engine = engine_with_existing_entry
    delete_response = engine.delete_url(key)
    assert delete_response is True, "Expected url entry to be deleted"
    get_response = engine.datalayer.get(key)
    assert get_response is None, f"Expected url entry with key: {key} to not exist"


def test_get_long_url_successful(engine_with_existing_entry, key, long_url):
    engine = engine_with_existing_entry
    response = engine.get_long_url(key)
    assert response == long_url, "Expected response to equal long_url"
    get_response = engine.datalayer.get(key)
    assert get_response.get("clicked", None) == 2


def test_get_long_url_unsuccessful_with_nonexistent_key(url_shorter_engine, key):
    engine = url_shorter_engine
    response = engine.get_long_url(key)
    assert response is None, "Expected response for nonexistent key to be None"


def test_get_clicked_stats_successful(engine_with_existing_entry, key):
    engine = engine_with_existing_entry
    response = engine.get_clicked_stats(key)
    assert response == 1, "Expected clicked stats to equal 1"


def test_get_clicked_stats_unsuccessful_for_nonexistent_key(url_shorter_engine, key):
    engine = url_shorter_engine
    response = engine.get_clicked_stats(key)
    assert response is None, "Expected get_clicked_stats to return None for nonexistent entry"
