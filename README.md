# Ground Control Software (GCS) for UAV Imaging

This project implements a prototype for a Ground Control Software (GCS) that automates basic operations for a UAV imaging payload. The system provides a backend to manage UAV commands, payload operations (imaging), and basic analytics. This software is designed to run on a local machine and interact with simulated UAV operations.

## Features
- **Command and Control Interface**: RESTful API to start/stop missions and capture images.
- **Payload Operations**: Simulated payload imaging using background processes.
- **Data Storage and Retrieval**: Store mission logs and captured image metadata in a database.
- **CI/CD Automation**: GitHub Actions for automated testing and deployment.
- **Scalability Considerations**: Discussed in the documentation for supporting multiple UAVs.
  
---

## Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/gcs-uav.git
cd gcs-uav
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

Run the Application

python app.py
