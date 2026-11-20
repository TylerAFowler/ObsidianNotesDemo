from datetime import datetime, timedelta, timezone

MAX_AGE = timedelta(hours=48)

def expired(sessions, now=None):
    now = now or datetime.now(timezone.utc)
    return [s for s in sessions if now - s.started > MAX_AGE]
