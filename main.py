from fastapi import FastAPI, Request
from pydantic import BaseModel
import pytesseract
from PIL import Image
from app.traductor import traductor_func
from app.scanTexto import scan_text_from_image

app = FastAPI()

class ScanTexto(BaseModel):
    image_path: str
    
@app.get("/")
def index():
    return {"message" : "Hola, Pythonianos"}

def scan_text_from_image(image_path):
    try:
        # Abre la imagen usando PIL
        print(f"Abriendo la imagen desde {image_path}")
        img = Image.open(image_path)
        print("Imagen abierta correctamente")
        
        # Configura la ruta del ejecutable de Tesseract si es necesario
        pytesseract.pytesseract.tesseract_cmd = r'C:/Archivos de programa/Tesseract-OCR/tesseract.exe'
        
        # Extrae el texto de la imagen
        print("Extrayendo texto de la imagen...")
        text = pytesseract.image_to_string(img, lang='spa')
        print("Texto extraído:")
        print(text)
        
        return text
    except Exception as e:
        print(f"Ocurrió un error: {e}")
        return ""

@app.post("/scanTexto")
async def scanTexto_endpoint(scanTexto_data: ScanTexto):
    image_path = scanTexto_data.image_path

    try:
        texto_extraido = scan_text_from_image(image_path)
        return {"data": texto_extraido}
    except Exception as e:
        print(f"Error extracting text: {e}")
        return {"error": str(e)}
    
class TraductorRequest(BaseModel):
    translate_text: str
    target_lang: str


@app.post("/traductor")
async def traductor_endpoint(request: Request, traductor_data: TraductorRequest):
    translate_text = traductor_data.translate_text
    target_lang = traductor_data.target_lang
    traduccion = traductor_func(translate_text, target_lang)
    return {"data": traduccion}

    

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
