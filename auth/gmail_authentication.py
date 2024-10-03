from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import os
from googleapiclient.discovery import build
from dotenv import load_dotenv

# Scopes necesarios
SCOPES = ['https://www.googleapis.com/auth/gmail.modify']

# Cargar variables de entorno
load_dotenv('config/.env')
token_path = os.getenv('GMAIL_TOKEN')
user_path = os.getenv('GMAIL_CLIENT_SECRET_PATH')


def authenticate_gmail():
    creds = None
    try:
        if os.path.exists(token_path):
            creds = Credentials.from_authorized_user_file(token_path, SCOPES)
        
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(user_path, SCOPES)
                creds = flow.run_local_server(port=0)
            # Guardar las credenciales para el futuro
            with open(token_path, 'w') as token:
                token.write(creds.to_json())
        
        return build('gmail', 'v1', credentials=creds)
    except Exception as e:
        print(f"Error durante la autenticación: {e}")
        return None