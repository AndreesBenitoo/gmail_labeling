import sys
import os

# Añadir el directorio raíz del proyecto al sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from labeling.auth import authenticate_gmail
from labeling.core import process_emails, categorize_email

if __name__ == '__main__':
    service = authenticate_gmail()
    process_emails(service, categorize_email)  