import abc
from typing import Union


class DataLayer(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return (
            hasattr(subclass, "get")
            and callable(subclass.get)
            and hasattr(subclass, "update")
            and callable(subclass.update)
            and hasattr(subclass, "create")
            and callable(subclass.create)
            and hasattr(subclass, "delete")
            and callable(subclass.delete)
            or NotImplemented
        )

    @abc.abstractclassmethod
    def get(self, short_url: str) -> dict:
        """Get full url and data by shortened url"""
        raise NotImplementedError

    @abc.abstractclassmethod
    def delete(self, short_url: str) -> bool:
        """Delete full url and data for shortened url"""
        raise NotImplementedError

    @abc.abstractclassmethod
    def update(self, short_url: str, datafield: str, data: Union[str, int]) -> bool:
        """Updates full url data by shortened url"""
        raise NotImplementedError

    @abc.abstractclassmethod
    def create(self, short_url: str, long_url: str) -> bool:
        """Creates a new entry by short url"""
        raise NotImplementedError
