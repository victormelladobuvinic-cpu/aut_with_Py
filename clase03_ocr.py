import pytesseract
from PIL import Image
import os

# 1. Configura la ruta del ejecutable de Tesseract (Asegúrate que sea esta)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# 2. Nombre de tu foto (asegúrate de que esté en la misma carpeta que el script)
archivo_foto = 'caja_ejemplo2.jpeg' # <--- CAMBIA ESTO

# 3. Verificamos si el archivo existe para evitar errores
if os.path.exists(archivo_foto):
    # Cargamos la imagen
    imagen = Image.open(archivo_foto)
    
    # --- EL DESAFÍO ---
    # Usa el método de pytesseract para convertir la imagen a texto (String)
    # Pista: se llama image_to_string
    
    resultado = pytesseract.image_to_string(imagen)
    
    print("-" * 30)
    print("LECTURA DE LA FOTO:")
    print(resultado)
    print("-" * 30)
    
else:
    print(f"Error: No encontré el archivo {archivo_foto}")