import io
from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from generate_picture import GeneratePicture

app = FastAPI()

@app.get("/api/image")
@app.get("/image")
def get_image(width: int = 800, height: int = 600):
    generator = GeneratePicture(width, height)
    img = generator.generate_picture()
    img_byte_arr = io.BytesIO()
    img.save(img_byte_arr, format='PNG')
    img_byte_arr.seek(0)
    return StreamingResponse(img_byte_arr, media_type="image/png")

@app.get("/api/health")
@app.get("/health")
def health_check():
    return {"status": "ok"}
