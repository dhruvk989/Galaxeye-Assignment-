# Simulate payload (imaging) operations
import time
from datetime import datetime
from .models import Image
from . import db

def capture_image(mission_id):
    # Simulate the delay for capturing an image
    time.sleep(2)  # Simulating processing delay
    image_path = f'/images/mission_{mission_id}_{datetime.utcnow().timestamp()}.jpg'
    image = Image(mission_id=mission_id, image_path=image_path)
    db.session.add(image)
    db.session.commit()
    return image_path
