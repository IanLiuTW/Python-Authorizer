from python_authorizer.authorizer import Authorizer
from python_authorizer.email.email_sender import EmailSender
from dataclasses import dataclass
import random
import string


@dataclass
class EmailAuthorizer(Authorizer):
    email_sender: EmailSender
    code: str = None

    def __str__(self):
        return f"{self.__class__.__name__}"

    def create(self):
        self._generate_code()
        self._send_code()

    def verify(self):
        code = input("Code: ")
        self.authorized = code == self.code
        return self.authorized

    def is_authorized(self):
        return self.authorized

    def _generate_code(self):
        self.code = ''.join(random.choices(string.digits, k=6))

    def _send_code(self):
        self.email_sender.send_mail(
            f"Authorization Code",
            f"This is your code: <strong>{self.code}</strong>"
        )

    def _verify_code(self, code):
        self.authorized = code == self.code
        return self.authorized
