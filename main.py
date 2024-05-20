from fastapi import FastAPI, Request, UploadFile
from pydantic import BaseModel
from app.traductor import traductor_func
from app.scanTexto import scan_text_from_image
from app.scanTexto2 import scan_text2_func

app = FastAPI()

    
class ScanTexto(BaseModel):
    image_path: str
    
class ScanTexto2(BaseModel):
    image: UploadFile

@app.get("/")
def index():
    return {"message" : "Hola, Pythonianos"}


    
@app.post("/scanTexto")
async def scanTexto_endpoint(request: Request, scanTexto_data: ScanTexto):
    image_path = scanTexto_data.image_path
    texto_extraido = scan_text_from_image(image_path)
    return {"data": texto_extraido}

@app.post("/scanTexto2")
async def scanTexto2_endpoint(request: Request, scanTexto2_data: ScanTexto2):
    UploadFile = scanTexto2_data.UploadFile
    texto_extraido = scan_text2_func(UploadFile)
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

