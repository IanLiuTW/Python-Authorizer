import config
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from dataclasses import dataclass
from abc import ABC, abstractmethod


@dataclass
class EmailSender(ABC):
    from_email: str
    to_emails: str

    @abstractmethod
    def send_mail():
        pass


@dataclass
class SendGridEmailSender(EmailSender):
    API_KEY = config.SENDGRID_API_KEY

    def send_mail(self, subject, html_content):
        message = Mail(
            from_email=self.from_email,
            to_emails=self.to_emails,
            subject=subject,
            html_content=html_content)
        try:
            sg = SendGridAPIClient(self.API_KEY)
            response = sg.send(message)
            print(response.status_code)
            print(response.body)
            print(response.headers)
        except Exception as e:
            print(e.message)
