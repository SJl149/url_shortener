from typing import Optional, Union

from .interface import DataLayer


class MockedDatalayer(DataLayer):
    def __init__(self):
        self.db = {}

    def get(self, key: str) -> Optional[dict]:
        return self.db.get(key, None)

    def delete(self, key: str) -> bool:
        deleted_item = self.db.pop(key, None)
        return True if deleted_item else False

    def update(self, key: str, datafield: str, data: Union[str, int]) -> bool:
        if self.db.get(key, None) and self.db.get(key, None).get(datafield, None):
            self.db[key][datafield] = data
            return True
        else:
            return False

    def create(self, key: str, long_url: str) -> bool:
        if key not in self.db:
            self.db[key] = {"long_url": long_url, "clicked": 1}
            return True
        else:
            return False
