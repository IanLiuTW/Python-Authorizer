from python_authorizer.authorizer import Authorizer


class AuthorizationApp:
    def __init__(self, authorizer: Authorizer) -> None:
        self.authorizer = authorizer

    def create(self):
        self.authorizer.create()

    def verify(self):
        return self.authorizer.verify()

    def is_authorized(self):
        return self.authorizer.is_authorized()
