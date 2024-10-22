# Gmail Labeling Project

Este es un script de Python que utiliza la API de Gmail para leer, clasificar y etiquetar automáticamente correos electrónicos. La clasificación se realiza según las palabras clave definidas y se asignan etiquetas específicas a cada correo en tu bandeja de entrada.

## Características

- Autenticación segura con la API de Gmail utilizando OAuth 2.0.
- Clasificación de correos electrónicos basada en palabras clave.
- Etiquetado automático de correos según su contenido.
- Fácil personalización de criterios de clasificación.

## Requisitos

- Python 3.12
- Una cuenta de Google con acceso a Gmail.
- Acceso a la consola de Google Cloud para obtener credenciales.

## Instalación

1. Clona este repositorio:

   ```bash
   git clone https://github.com/tu-usuario/gmail-labeling.git
   cd gmail-labeling
   ```

2. Crea y activa un entorno virtual (asegúrate de usar Python 3.12):

   ```bash
   python3.12 -m venv venv
   # En macOS/Linux
   source venv/bin/activate
   # En Windows
   venv\Scripts\activate
   ```

3. Instala las dependencias:

   ```bash
   pip install -r requirements.txt
   ```

4. Obtén las credenciales de la API de Gmail:

   - Ve a [Google Cloud Console](https://console.developers.google.com/).
   - Crea un proyecto y habilita la API de Gmail.
   - Configura la pantalla de consentimiento OAuth y crea credenciales de "Desktop app".
   - Descarga el archivo `credentials.json` y colócalo en la raíz de este proyecto.

5. Configura `.gitignore` para excluir archivos sensibles:

   ```text
   venv/
   credentials.json
   token.json
   __pycache__/
   *.pyc
   *.pyo
   *.pyd
   .DS_Store
   .env
   ```

## Uso

1. Ejecuta el script principal:

   ```bash
   python3 main.py
   ```

2. La primera vez que ejecutes el script, se abrirá una ventana en el navegador para que inicies sesión con tu cuenta de Google y otorgues los permisos necesarios. Esto generará un archivo `token.json` para futuras conexiones.

3. El script analizará los correos electrónicos no leídos y los etiquetará según las palabras clave definidas en `email_classifier.py`.

## Personalización

### Añadir o modificar etiquetas y palabras clave

1. Abre `email_classifier.py`.
2. Modifica el diccionario `LABELS` para añadir nuevas categorías o palabras clave:

   ```python
   LABELS = {
       'FACTURAS': ['factura', 'recibo', 'pago'],
       'OCIO/PROGRAMACIÓN': ['leetcode', 'programming', 'code', 'challenge'],
       'PENDIENTE': ['seguridad', 'alerta', 'confirmar'],
       'GOOGLE_CLOUD': ['google cloud', 'consola', 'crédito', 'servicio'],
       'DESECHO': ['promoción', 'regalo', 'ganar', 'premio']
   }
   ```

### Manejar errores

- La función `handle_api_errors` en `utils.py` proporciona una forma de gestionar los errores de la API. Personaliza esta función según tus necesidades.

## Estructura del Proyecto

- `main.py`: Archivo principal para ejecutar el programa.
- `gmail_auth.py`: Módulo para la autenticación con la API de Gmail.
- `email_classifier.py`: Módulo para la clasificación de correos electrónicos.
- `email_labeler.py`: Módulo para procesar y etiquetar los correos electrónicos.
- `utils.py`: Funciones auxiliares para extraer contenido y manejar errores.

## Contribuir

1. Haz un fork de este repositorio.
2. Crea una rama con tus cambios:

   ```bash
   git checkout -b mi-rama-nueva
   ```

3. Haz commit de tus cambios:

   ```bash
   git commit -m "Descripción de los cambios"
   ```

4. Sube tus cambios:

   ```bash
   git push origin mi-rama-nueva
   ```

5. Abre un Pull Request en GitHub.

## Notas de Seguridad

- **No compartas** tu archivo `credentials.json` ni el `token.json`. Contienen información sensible que puede comprometer tu cuenta de Gmail.
- Asegúrate de añadir `credentials.json` y `token.json` a `.gitignore` para evitar que se suban al repositorio.

## Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo `LICENSE` para más detalles.
