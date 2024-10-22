from auth import authenticate_gmail
from core.mail import process_emails, categorize_func, get_gmail_labels

def main():
    service = authenticate_gmail()
    labels = get_gmail_labels(service)
    label_names = [label['name'] for label in labels]
    process_emails(service, categorize_func,label_names)


if __name__ == '__main__':
    main()