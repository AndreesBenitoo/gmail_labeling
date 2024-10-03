import base64
import quopri
    
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