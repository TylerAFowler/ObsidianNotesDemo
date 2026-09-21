from fastapi import FastAPI
from .clips import router as clips

app = FastAPI(title="RoadView API")
app.include_router(clips, prefix="/clips")
