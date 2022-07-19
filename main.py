from fastapi import FastAPI, Request, Body
from fastapi.staticfiles import StaticFiles
from starlette.responses import RedirectResponse, FileResponse
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
from typing import List


app = FastAPI()

app.mount("/svelte", StaticFiles(directory="svelte/public", html=True), name="build")


@app.get("/{full_path:path}")
def render_svelte(request: Request, full_path: str):
    return FileResponse("svelte/public/index.html")