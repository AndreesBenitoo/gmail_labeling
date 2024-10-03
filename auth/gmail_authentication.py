from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import os.path
from googleapiclient.discovery import build
from dotenv import load_dotenv
load_dotenv()

# Scopes necesarios
SCOPES = ['https://www.googleapis.com/auth/gmail.modify']

def authenticate_gmail():
    creds = None
    if os.path.exists(os.getenv('GMAIL_TOKEN')):
        creds = Credentials.from_authorized_user_file(os.getenv('GMAIL_TOKEN'), SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('GMAIL_CLIENT_SECRET_PATH', SCOPES)
            creds = flow.run_local_server(port=0)
        with open(os.getenv('GMAIL_TOKEN'), 'w') as token:
            token.write(creds.to_json())
    return build('gmail', 'v1', credentials=creds)
