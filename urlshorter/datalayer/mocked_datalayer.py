from .interface import DataLayer
from typing import Union


class MockedDatalayer(DataLayer):
    def __init__(self):
        self.db = {}

    def get(self, short_url: str) -> dict:
        return self.db.get(short_url, None)

    def delete(self, short_url: str) -> bool:
        deleted_item = self.db.pop(short_url, None)
        return True if deleted_item else False

    def update(self, short_url: str, datafield: str, data: Union[str, int]) -> bool:
        if self.db.get(short_url, None) and self.db.get(short_url, None).get(datafield, None):
            self.db[short_url][datafield] = data
            return True
        else:
            return False

    def create(self, short_url: str, long_url: str) -> bool:
        if short_url not in self.db:
            self.db[short_url] = {"long_url": long_url, "clicked": 1}
            return True
        else:
            return False
