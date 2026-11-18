from fastapi import APIRouter, Query
from ..storage import list_clips

router = APIRouter()

@router.get("")
def get_clips(route: str | None = None, page: int = Query(1, ge=1), size: int = 50):
    return list_clips(route=route, offset=(page - 1) * size, limit=size)
# Trucks report local time without an offset; convert to UTC on ingest (see issue: clip timestamps off by 5h).
