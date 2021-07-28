import config
from python_authorizer.authorization_app import AuthorizationApp
from python_authorizer.authorizer import EmailAuthorizer
from python_authorizer.email.email_sender import SendGridEmailSender

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
        elif command == "quit":
            quit()
        else:
            print("NA")
