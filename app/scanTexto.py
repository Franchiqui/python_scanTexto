from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:/Archivos de programa/Tesseract-OCR/tesseract.exe'


def scan_text_from_image(image_path):
    try:
        # Abre la imagen usando PIL
        print(f"Abriendo la imagen desde {image_path}")
        img = Image.open(image_path)
        print("Imagen abierta correctamente")
        
        # Configura la ruta del ejecutable de Tesseract si es necesario
        # pytesseract.pytesseract.tesseract_cmd = r'C:/Archivos de programa/Tesseract-OCR/tesseract.exe'
        
        # Extrae el texto de la imagen
        print("Extrayendo texto de la imagen...")
        text = pytesseract.image_to_string(img, lang='spa')
        print("Texto extraído:")
        print(text)
        
        return text
    except Exception as e:
        print(f"Ocurrió un error: {e}")
        return ""

# Ruta de la imagen
image_path = 'D:/python_ScanTexto/data/routing.PNG'

# Extrae el texto
texto_extraido = scan_text_from_image(image_path)
print("Texto extraído final:")
print(texto_extraido)
