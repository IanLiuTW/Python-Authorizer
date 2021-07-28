import config
from python_authorizer.authorizer import AuthorizerApp
from python_authorizer.email.email_sender import SendGridEmailSender
from python_authorizer.email.email_authorizer import EmailAuthorizer

if __name__ == "__main__":
    email_sender = SendGridEmailSender(from_email=config.FROM_EMAIL)
    email_authorizer = EmailAuthorizer(email_sender)
    auth = AuthorizerApp(email_authorizer)

    while True:
        command = input("Enter command: ")
        if command == "create":
            print(f"Authorizer created using {auth!s}")
            auth.create()
        elif command == "verify":
            result = auth.verify()
            print(f"Authorizer verify result: {result}")
        elif command == "status":
            print(f"Authorizer status: {auth.is_authorized()}")
        elif command == "quit":
            print("Authorizer quited.")
            quit()
        else:
            print("Authorizer command not supported.")
