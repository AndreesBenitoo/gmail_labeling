from auth import authenticate_gmail
from core.mail import process_emails, categorize_email


if __name__ == '__main__':
    service = authenticate_gmail()
    process_emails(service, categorize_email)