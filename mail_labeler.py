import base64
from email import message_from_bytes

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

def process_emails(service, categorize_func):
    messages = get_unread_emails(service)
    for message in messages:
        msg = service.users().messages().get(userId='me', id=message['id'], format='raw').execute()
        msg_str = base64.urlsafe_b64decode(msg['raw'].encode('ASCII'))
        mime_msg = message_from_bytes(msg_str)
        
        # Obtener el cuerpo del correo
        if mime_msg.is_multipart():
            content = ''
            for part in mime_msg.walk():
                if part.get_content_type() == 'text/plain':
                    content += part.get_payload(decode=True).decode()
        else:
            content = mime_msg.get_payload(decode=True).decode()
        
        # Clasificar el correo
        label = categorize_func(content)
        
        # Aplicar la etiqueta
        label_email(service, message['id'], label)
