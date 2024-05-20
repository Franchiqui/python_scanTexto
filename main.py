from fastapi import FastAPI, Request
from pydantic import BaseModel
from app.traductor import traductor_func
from app.scanTexto import scanTexto_func

app = FastAPI()

    
class ScanTexto(BaseModel):
    image_path: str
    

@app.get("/")
def index():
    return {"message" : "Hola, Pythonianos"}


    
@app.post("/scanTexto")
async def scanTexto_endpoint(request: Request, scanTexto_data: ScanTexto):
    image_path = scanTexto_data.image_path

    try:
        escaner = scanTexto_func(image_path)
        return {"data": escaner}
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

