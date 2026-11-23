from roadview.backend.uploads.session import UploadSession
from roadview.backend.uploads.resume import next_part

def test_resume_after_gap():
    s = UploadSession("c1", "I-79", "u1", parts={1: "a", 2: "b"})
    assert next_part(s) == 3
