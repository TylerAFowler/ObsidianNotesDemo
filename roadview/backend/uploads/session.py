from dataclasses import dataclass, field
from datetime import datetime, timezone

@dataclass
class UploadSession:
    clip_id: str
    route: str
    upload_id: str                 # object-store multipart upload id
    parts: dict[int, str] = field(default_factory=dict)   # part number -> etag
    started: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
