import re
# esto me da una lista de etiquetas
def get_gmail_labels(service):
    try:
        results = service.users().labels().list(userId='me').execute()
        first_labels = results.get('labels', [])
        
        if not first_labels:
            print('no se han encontrado etiquetas')
            return []
        
        
        filtered_labels = filter_labels(first_labels)
        
        labels = extract_label_names_and_ids(filtered_labels)
        # print('Etiquetas en la cuenta de Gmail: ')
        # print(labels)
        return labels
        
    except Exception as error:
        print(f'Ha ocurrido un error: {error}')
        

def filter_labels(labels):
    # Expresión regular para el formato 'Label_xxxxxxxxxxxxxxxxxxx'
    pattern = re.compile(r'^Label_\d{15,}$')
    
    # Filtrar las etiquetas que coinciden con el patrón de 'id'
    filtered_labels = [label for label in labels if pattern.match(label['id'])]
    
    return filtered_labels


def extract_label_names_and_ids(labels):
    # Crear una nueva lista con solo el 'name' de cada etiqueta
    simplified_labels = [{'name': label['name']} for label in labels]
    return simplified_labels