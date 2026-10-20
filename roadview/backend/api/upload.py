from fastapi import APIRouter, UploadFile
from ..storage import s3, BUCKET

router = APIRouter()

@router.put("/{route}/{clip_id}")
async def upload(route: str, clip_id: str, file: UploadFile):
    s3.upload_fileobj(file.file, BUCKET, f"clips/{route}/{clip_id}.mp4")
    return {"ok": True}
