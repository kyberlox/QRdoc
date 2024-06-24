from fastapi import FastAPI, Body, Response, Cookie
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import RedirectResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles

import qrcode


app = FastAPI()

origins = [
    "http://127.0.0.1:8000",
    "http://localhost:8000",
    "qr.doc"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST"],#, "OPTIONS", "DELETE", "PATH", "PUT"],
    allow_headers=["Content-Type", "Accept", "Location", "Allow", "Content-Disposition", "Sec-Fetch-Dest"],
)

app.mount("/public", StaticFiles(directory="public"), name="public")
 
@app.get("/")
def read_root():
    return FileResponse("public/index.html")

@app.get("/QR/{num}", response_class = FileResponse)
def getQR(num):
    img = qrcode.make(f'ТУ-{num}...')
    img.save(f"./public/QR_{num}.png")
    return f"./public/QR_{num}.png"