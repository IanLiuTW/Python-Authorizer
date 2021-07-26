import config
from python_email_auth.email_sender import SendGridEmailSender
from python_email_auth.email_auth import EmailAuthor
from python_email_auth.email_auth_app import EmailAuthApp

if __name__ == "__main__":
    email_sender = SendGridEmailSender(from_email=config.FROM_EMAIL,
                                       to_emails=config.TO_EMAILS)
    email_auth = EmailAuthor(email_sender)
    auth = EmailAuthApp(email_auth)

    while True:
        command = input("Input: ")
        if command == "create":
            auth.create_code()
            print("code created and sent")
        elif command == "verify":
            code = input("Code: ")
            print(auth.verify_code(code))
        elif command == "auth":
            print(auth.is_authorized())
        else:
            print("NA")
