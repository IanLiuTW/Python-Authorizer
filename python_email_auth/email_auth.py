from python_email_auth.email_sender import EmailSender
from dataclasses import dataclass
import random
import string


@dataclass
class EmailAuthor:
    email_sender: EmailSender
    authorized: bool = False
    code: str = None

    def generate_code(self):
        self.code = ''.join(random.choices(string.digits, k=6))

    def send_code(self):
        self.email_sender.send_mail(
            f"Authorization Code",
            f"This is your code: <strong>{self.code}</strong>"
        )

    def verify_code(self, code):
        self.authorized = code == self.code
        return self.authorized

    def is_authorized(self):
        return self.authorized
