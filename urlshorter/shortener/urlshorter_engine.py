import random
import string
from typing import Optional

from urlshorter.datalayer.interface import DataLayer


class URLShorterEngine:
    def __init__(self, datalayer: DataLayer) -> None:
        self.datalayer = datalayer
        self.size = 6

    def _generate_random_key(self) -> str:
        characters = string.ascii_letters + string.digits
        return "".join(random.choice(characters) for _ in range(self.size))

    def _get_unique_random_key(self) -> str:
        random_key = self._generate_random_key()
        while self.datalayer.get(random_key) is not None:
            random_key = self._generate_random_key()
        return random_key

    def add_with_custom_key(self, custom_key: str, long_url: str) -> Optional[str]:
        response = None
        if len(custom_key) == 6 and self.datalayer.get(key=custom_key) is None:
            response = self.datalayer.create(key=custom_key, long_url=long_url)
        return custom_key if response else None

    def add_with_random_key(self, long_url: str) -> Optional[str]:
        random_key = self._get_unique_random_key()
        response = self.datalayer.create(key=random_key, long_url=long_url)
        return random_key if response else None

    def delete_url(self, key: str) -> bool:
        if self.datalayer.get(key):
            return self.datalayer.delete(key)
        else:
            return True

    def get_long_url(self, key: str) -> Optional[str]:
        url_entry = self.datalayer.get(key)
        if url_entry:
            clicked_count = int(url_entry["clicked"]) + 1
            update_response = self.datalayer.update(key, datafield="clicked", data=clicked_count)
            if update_response:
                return url_entry["long_url"]
        return None

    def get_clicked_stats(self, key: str) -> Optional[int]:
        url_entry = self.datalayer.get(key)
        if url_entry:
            return url_entry["clicked"]
        else:
            return None
