# Suponiendo que ya tienes el objeto 'service' autenticado
import base64
import quopri

def get_email_content(service, email_id):
    # Obtener el mensaje en formato 'full' para acceder al cuerpo y los encabezados
    message = service.users().messages().get(userId='me', id=email_id, format='full').execute()
    
    # Acceder al payload del mensaje
    payload = message.get('payload', {})
    headers = payload.get('headers', [])
    
    # Extraer el asunto del correo
    subject = ''
    for header in headers:
        if header['name'] == 'Subject':
            subject = header['value']
            break
    
    # Función auxiliar para decodificar el cuerpo del mensaje
    

    # Obtener el cuerpo del mensaje
    body = get_body(payload)

    return subject, body

def decode_message(message_body, encoding):
    if encoding == 'BASE64':
        return base64.urlsafe_b64decode(message_body).decode('utf-8')
    elif encoding == 'QUOTED-PRINTABLE':
        return quopri.decodestring(message_body).decode('utf-8')
    else:
        return message_body

# Función recursiva para extraer el cuerpo del mensaje
def get_body(payload):
    body = ''
    if 'parts' in payload:
        for part in payload['parts']:
            if part['mimeType'] == 'text/plain':
                data = part['body']['data']
                body += decode_message(data, 'BASE64')
            elif part['mimeType'] == 'text/html':
                pass  # Si deseas también procesar el HTML
            elif 'parts' in part:
                body += get_body(part)
    elif payload.get('body', {}).get('data'):
        data = payload['body']['data']
        body += decode_message(data, 'BASE64')
    return body