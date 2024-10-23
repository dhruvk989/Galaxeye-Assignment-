# UAV GCS Project

This is a Ground Control Software (GCS) prototype for UAVs.
It manages UAV commands, payload operations (imaging), and stores logs and metadata.

## Setup Instructions
1. Create a virtual environment: `python3 -m venv venv`
2. Activate the environment: `source venv/bin/activate`
3. Install dependencies: `pip install -r requirements.txt`
4. Run the Flask app: `python app.py`

## API Endpoints
- `/start_mission`: Start a new mission
- `/capture_image`: Capture an image
- `/stop_mission`: Stop the mission

## CI/CD
CI/CD pipeline is set up using GitHub Actions.
