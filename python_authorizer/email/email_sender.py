import config
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from dataclasses import dataclass
from abc import ABC, abstractmethod


@dataclass
class EmailSender(ABC):
    from_email: str

    @abstractmethod
    def send_mail():
        pass


@dataclass
class SendGridEmailSender(EmailSender):
    API_KEY = config.SENDGRID_API_KEY

    def send_mail(self, subject, html_content):
        to_emails = input("To email: ")

        message = Mail(
            from_email=self.from_email,
            to_emails=to_emails,
            subject=subject,
            html_content=html_content)
        try:
            sg = SendGridAPIClient(self.API_KEY)
            sg.send(message)
        except Exception as e:
            print(e.message)
