from abc import ABC, abstractmethod


class AbstractRepository(ABC):

    @abstractmethod
    def find_all(self):
        raise NotImplementedError

    @abstractmethod
    def get_one(self, id, userid):
        raise NotImplementedError

    @abstractmethod
    def add_one(self, **kwargs):
        raise NotImplementedError

    @abstractmethod
    def delete_one(self, data):
        return NotImplementedError


class SQLRepository(AbstractRepository):

    def find_all(self):
        pass

    def get_one(self, id, userid):
        pass

    def add_one(self, **kwargs):
        pass

    def delete_one(self, data):
        pass
