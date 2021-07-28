import config
from python_authorizer.email_sender import SendGridEmailSender
from python_authorizer.authorizer import EmailAuthorizer
from python_authorizer.authorization_app import AuthorizationApp

if __name__ == "__main__":
    email_sender = SendGridEmailSender(from_email=config.FROM_EMAIL)
    email_authorizer = EmailAuthorizer(email_sender)
    auth = AuthorizationApp(email_authorizer)

    while True:
        command = input("Command: ")
        if command == "create":
            auth.create()
        elif command == "verify":
            auth.verify()
        elif command == "status":
            print(auth.is_authorized())
        else:
            print("NA")
