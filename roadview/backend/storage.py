import os
import boto3

BUCKET = os.environ.get("CLIP_BUCKET", "roadview-clips")
s3 = boto3.client("s3", endpoint_url=os.environ.get("OBJECT_STORE_URL"))

def list_clips(route=None, offset=0, limit=50):
    prefix = f"clips/{route}/" if route else "clips/"
    keys = [o["Key"] for o in s3.list_objects_v2(Bucket=BUCKET, Prefix=prefix).get("Contents", [])]
    return keys[offset:offset + limit]
