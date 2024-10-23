from flask import Blueprint, jsonify, request
from app.models import db, Mission, Image
from datetime import datetime

app = Blueprint('app', __name__)

# New route for the home page
@app.route('/')
def home():
    return "Welcome to the UAV GCS API!", 200

@app.route('/capture_image', methods=['POST'])
def capture_image():
    mission_id = request.json.get('mission_id')
    image_filename = f"image_{mission_id}_{int(datetime.now().timestamp())}.jpg"
    
    new_image = Image(image_filename=image_filename, mission_id=mission_id)
    db.session.add(new_image)
    db.session.commit()
    
    return jsonify({"message": "Image captured successfully", "image_filename": image_filename}), 200
