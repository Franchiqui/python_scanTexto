from PIL import Image
import pytesseract
import cv2

def scanTexto_func(image_path):
    """
    Extrae texto de una imagen y lo devuelve como cadena.

    Argumentos:
        imagePath (str): Ruta al archivo de imagen a escanear.

    Retorno:
        str: El texto extraído de la imagen.
    """

    # Cargar la imagen usando OpenCV
    img = cv2.imread(image_path)

    # Compruebe si la imagen se leyó correctamente.
    if img is None:
        raise Exception("Error loading image: {}".format(image_path))

    # Convertir la imagen a escala de grises
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Aplicar umbrales para convertir a una imagen binaria
    threshold_img = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

    # Convertir la imagen de OpenCV a un objeto PIL
    pil_image = Image.fromarray(threshold_img)

    # Establecer la ruta de Tesseract
    pytesseract.pytesseract.tesseract_cmd = r'C:/Archivos de programa/Tesseract-OCR/tesseract.exe'

    # Extraer texto usando pytesseract
    text = pytesseract.image_to_string(pil_image, config='--psm 10 lang=es')

    # Devolver el texto extraído
    return text
