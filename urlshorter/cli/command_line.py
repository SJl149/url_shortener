import helpers

from urlshorter.datalayer.mocked_datalayer import MockedDatalayer
from urlshorter.shortener.urlshorter_engine import URLShorterEngine


def add_url(engine: URLShorterEngine) -> None:
    long_url, custom_key = helpers.enter_new_url()
    if custom_key:
        added_key = engine.add_with_custom_key(custom_key, long_url)
    else:
        added_key = engine.add_with_random_key(long_url)

    if added_key:
        print(f"\n{long_url} can be accessed with urlshorter/{added_key}")
    else:
        print(f"\n    Error trying to add {long_url}!!! Please try again")


def find_long_url(engine: URLShorterEngine) -> None:
    key, long_url = None, None
    while key is None and long_url is None:
        key = helpers.enter_short_url_key()
        long_url = engine.get_long_url(key)
    if long_url:
        print(f"The short URL urlshorter/{key} corresponds to {long_url}")
    else:
        print(f"Could not find URL with key: {key}")


def get_stats(engine: URLShorterEngine) -> None:
    key = helpers.enter_short_url_key()
    response = engine.get_clicked_stats(key)
    if response:
        print(f"\nurlshorter/{key} has been clicked {response} times")
    else:
        print(f"     Could not find short url: urlshorter/{key}")


def delete_url(engine: URLShorterEngine):
    key = helpers.enter_short_url_key()
    response = engine.delete_url(key)
    if response:
        print(f"urlshorter/{key} was deleted successfully!")
    else:
        print(f"There was a problem deleting urlshorter/{key}")


def menu_actions(action: str, engine: URLShorterEngine):
    if action == "1":
        add_url(engine)
    elif action == "2":
        find_long_url(engine)
    elif action == "3":
        get_stats(engine)
    elif action == "4":
        delete_url(engine)
    else:
        helpers.quit_program()


if __name__ == "__main__":
    helpers.greeting()
    cont = True
    datalayer = MockedDatalayer()
    engine = URLShorterEngine(datalayer)

    while cont:
        helpers.print_menu()
        action = helpers.get_menu_choice()
        menu_actions(action, engine)
        cont = helpers.ask_to_continue()

    helpers.quit_program()
