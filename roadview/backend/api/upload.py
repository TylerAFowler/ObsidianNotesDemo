from fastapi import APIRouter, UploadFile
from ..storage import s3, BUCKET

router = APIRouter()

@router.put("/{route}/{clip_id}")
async def upload(route: str, clip_id: str, file: UploadFile):
    s3.upload_fileobj(file.file, BUCKET, f"clips/{route}/{clip_id}.mp4")
    return {"ok": True}
CHUNK = 64 * 1024 * 1024   # 64 MB parts

@router.post("/{route}/{clip_id}/start")
def start(route: str, clip_id: str): ...

@router.put("/{route}/{clip_id}/part/{n}")
async def part(route: str, clip_id: str, n: int, file: UploadFile): ...

@router.post("/{route}/{clip_id}/complete")
def complete(route: str, clip_id: str): ...
