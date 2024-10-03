import openai
import os
from dotenv import load_dotenv
# Configuración de OpenAI
load_dotenv('config/.env')
openai.api_key = os.getenv('OPENAI_API_KEY')


def classify_email(subject, body, labels):
    
    # Clasifica un correo electrónico utilizando la API de OpenAI.

    # Parámetros:
    # - subject: Asunto del correo electrónico.
    # - body: Cuerpo del correo electrónico.
    # - labels: Lista de nombres de etiquetas disponibles para clasificar.

    # Retorna:
    # - label: La etiqueta sugerida por el modelo.
    
    # Construir el prompt para la clasificación
    label_names = ', '.join(labels)
    prompt = (
        f"Clasifica el siguiente correo en una de las siguientes etiquetas: {label_names}.\n\n"
        f"Asunto: {subject}\n"
        f"Contenido: {body}\n\n"
        f"Etiqueta:"
    )

    try:
        # Llamar a la API de OpenAI
        response = openai.Completion.create(
            engine='text-davinci-003',  # Puedes cambiar el motor si lo deseas
            prompt=prompt,
            max_tokens=10,
            n=1,
            stop=None,
            temperature=0.3,
        )

        # Extraer la etiqueta sugerida por OpenAI
        label = response.choices[0].text.strip()
        return label
    except Exception as e:
        print(f"Error al clasificar el correo: {e}")
        return None
