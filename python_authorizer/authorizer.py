from dataclasses import dataclass, field
from abc import ABC, abstractmethod


@dataclass
class Authorizer(ABC):
    authorized: bool = field(default=False, init=False)

    @abstractmethod
    def create(self):
        pass

    @abstractmethod
    def verify(self):
        pass

    @abstractmethod
    def is_authorized(self):
        pass


@dataclass
class AuthorizerApp:
    authorizer: Authorizer

    def __str__(self):
        return f"{self.authorizer!s}"

    def create(self):
        self.authorizer.create()

    def verify(self):
        return self.authorizer.verify()

    def is_authorized(self):
        return self.authorizer.is_authorized()
