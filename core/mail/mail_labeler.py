import base64
from bs4 import BeautifulSoup
from .mail_filter import filter_content

def process_emails(service, categorize_func, labels):
    messages = get_unread_emails(service)
    for message in messages:
        msg = service.users().messages().get(userId='me', id=message['id'], format='full').execute()
        
        subject = get_email_subject(msg)
        # Obtener el cuerpo del correo en texto plano
        content = get_plain_text(msg['payload'])
        
        #filtrar contenido para eliminar espacios, link y correos electronicos del texto
        content = filter_content(content)
        # Clasificar el correo - chatgpt
        label = categorize_func(subject,content,labels)
        # Aplicar la etiqueta
        label_email(service, message['id'], label.lower())

def get_plain_text(payload):
    if 'parts' in payload:
        for part in payload['parts']:
            if part['mimeType'] == 'text/plain':
                data = part['body']['data']
                text = base64.urlsafe_b64decode(data).decode('utf-8')
                return text
            elif part['mimeType'] == 'text/html':
                data = part['body']['data']
                html = base64.urlsafe_b64decode(data).decode('utf-8')
                soup = BeautifulSoup(html, 'html.parser')
                text = soup.get_text()
                return text
            elif part['mimeType'].startswith('multipart/'):
                text = get_plain_text(part)
                if text:
                    return text
    elif payload['mimeType'] == 'text/plain':
        data = payload['body']['data']
        text = base64.urlsafe_b64decode(data).decode('utf-8')
        return text
    elif payload['mimeType'] == 'text/html':
        data = payload['body']['data']
        html = base64.urlsafe_b64decode(data).decode('utf-8')
        soup = BeautifulSoup(html, 'html.parser')
        text = soup.get_text()
        return text
    return ''

def get_unread_emails(service):
    results = service.users().messages().list(userId='me', labelIds=['INBOX'], q='is:unread').execute()
    messages = results.get('messages', [])
    return messages

def label_email(service, msg_id, label):
    # Obtener el ID de la etiqueta de Gmail
    labels_list = service.users().labels().list(userId='me').execute()
    label_id = None
    for lbl in labels_list['labels']:
        if lbl['name'].lower() == label.lower():
            label_id = lbl['id']
            break
    
    if label_id:
        labels = {
            'addLabelIds': [label_id],
            'removeLabelIds': []
        }
        service.users().messages().modify(userId='me', id=msg_id, body=labels).execute()
        print(f'Correo {msg_id} etiquetado como {label}')
    else:
        print(f'Etiqueta "{label}" no encontrada. Asegúrate de que exista en Gmail.')
        
import email
import email.header

def get_email_subject(msg):
    headers = msg['payload'].get('headers', [])
    subject = ''
    for header in headers:
        if header['name'].lower() == 'subject':
            subject = header['value']
            break

    # Decodificar el asunto si es necesario
    subject_parts = email.header.decode_header(subject)
    subject_decoded = ''
    for part, encoding in subject_parts:
        if isinstance(part, bytes):
            if encoding:
                subject_decoded += part.decode(encoding)
            else:
                subject_decoded += part.decode('utf-8')
        else:
            subject_decoded += part
    return subject_decoded