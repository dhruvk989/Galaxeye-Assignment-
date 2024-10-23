from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Initialize SQLAlchemy object
db = SQLAlchemy()

# Mission Model
class Mission(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    mission_name = db.Column(db.String(50))
    mission_status = db.Column(db.String(20))
    images = db.relationship('Image', backref='mission', lazy=True)

    def __repr__(self):
        return f"<Mission {self.mission_name}>"

# Image Model
class Image(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    image_filename = db.Column(db.String(100), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    mission_id = db.Column(db.Integer, db.ForeignKey('mission.id'), nullable=False)

    def __repr__(self):
        return f"<Image {self.image_filename} from Mission {self.mission_id}>"
