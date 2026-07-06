import os
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

app = FastAPI()

@app.get('/api/health')
def health_check():
    return {"status": "ok"}

@app.get('/api/test')
def test_endpoint():
    return {"message": "This is a test response."}

if os.path.isdir("frontend/build"):
    app.mount("/static", StaticFiles(directory="frontend/build/static"), name="static")

    @app.get("/{*path}")
    def serve_frontend(path: str):
        from fastapi.responses import FileResponse
        return FileResponse("frontend/build/index.html")
