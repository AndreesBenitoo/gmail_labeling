import openai
import os
from dotenv import load_dotenv

load_dotenv('config/.env')
openai.api_key = os.getenv('OPENAI_API_KEY')


def categorize_func(title, content, labels):
    # Construir el prompt
    prompt = f"""
Dado el siguiente correo electrónico:

Título: {title}

Mensaje:
{content}

Etiquetas disponibles: {labels}

Determina cuál de estas etiquetas es la más adecuada para clasificar este correo electrónico. Solo responde con el nombre de la etiqueta más relevante.
"""
    try:
        # Llamar a la API de OpenAI
        response = openai.chat.completions.create(
            model="gpt-4o",
            messages=[
                {
                "role": "user",
                "content": [
                    {
                    "type": "text",
                    "text": prompt
                    }
                ]
                }
            ],
            temperature=1,
            max_tokens=2048,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
            response_format={
                "type": "text"
            }
            )
        # Extraer la etiqueta de la respuesta
        label = response.choices[0].message.content.strip()
        # Verificar que la etiqueta esté en la lista de etiquetas disponibles
        if label in labels:
            return label
        else:
            print(f"La etiqueta '{label}' no está en la lista de etiquetas disponibles.")
            return None
    except Exception as e:
        print(f"Error al llamar a la API de OpenAI: {e}")
        return None