from PIL import Image, ImageDraw, ImageFont
import torch
import numpy as np
import random
from ultralytics import YOLO

# Muat model YOLOv8 
model = YOLO('yolov8n')

# Fungsi untuk hasil deteksi dan gambar anotasi
def deteksi_objek(img_pil):
    img_np = np.array(img_pil)

    # Lakukan deteksi
    results = model(img_np)
    deteksi = results[0].boxes

    hasil = []
    img_draw = img_pil.convert("RGB").copy()
    draw = ImageDraw.Draw(img_draw)

    try:
        font = ImageFont.truetype("arial.ttf", 14)
    except:
        font = ImageFont.load_default()

    if deteksi is not None:
        for i in range(len(deteksi)):
            box = deteksi[i]
            cls_id = int(box.cls[0].item())
            nama = model.names[cls_id]
            akurasi = round(box.conf[0].item() * 100, 2)

            hasil.append({"nama": nama, "akurasi": akurasi})

            # Koordinat bounding box
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            draw.rectangle([x1, y1, x2, y2], outline="red", width=2)
            label = f"{nama} ({akurasi}%)"
            draw.text((x1 + 4, y1 + 4), label, fill="red", font=font)

    return hasil, img_draw
