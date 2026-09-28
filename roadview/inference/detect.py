"""Runs the sign/guardrail detector over new clips and writes detections to the API."""
import sys
from ultralytics import YOLO

MODEL = YOLO("models/signs-v8.pt")

def detect(path, conf=0.35):
    for r in MODEL.predict(path, conf=conf, stream=True):
        for b in r.boxes:
            yield {"frame": r.path, "cls": MODEL.names[int(b.cls)], "conf": float(b.conf)}

if __name__ == "__main__":
    for d in detect(sys.argv[1]):
        print(d)
