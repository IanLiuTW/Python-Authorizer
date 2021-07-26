from python_email_auth.email_auth import EmailAuthor


class EmailAuthApp:
    def __init__(self, email_auth: EmailAuthor) -> None:
        self.email_auth = email_auth

    def create_code(self):
        self.email_auth.generate_code()
        self.email_auth.send_code()

    def verify_code(self, code):
        return self.email_auth.verify_code(code)

    def is_authorized(self):
        return self.email_auth.is_authorized()
