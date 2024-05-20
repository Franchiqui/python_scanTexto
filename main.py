from fastapi import FastAPI, Request
from pydantic import BaseModel
from app.traductor import traductor_func
from app.scanTexto import scan_text_from_image

app = FastAPI()

    
class ScanTexto(BaseModel):
    image_path: str
    

@app.get("/")
def index():
    return {"message" : "Hola, Pythonianos"}


    
@app.post("/scanTexto")
async def scanTexto_endpoint(request: Request, scanTexto_data: ScanTexto):
    image_path = scanTexto_data.image_path
    texto_extraido = scan_text_from_image(image_path)
    return {"data": texto_extraido}




class TraductorRequest(BaseModel):
    translate_text: str
    target_lang: str


@app.post("/traductor")
async def traductor_endpoint(request: Request, traductor_data: TraductorRequest):
    translate_text = traductor_data.translate_text
    target_lang = traductor_data.target_lang
    traduccion = traductor_func(translate_text, target_lang)
    return {"data": traduccion}

