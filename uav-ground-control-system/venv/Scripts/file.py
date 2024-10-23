import os

# Directory structure to be created
structure = {
    "uav-ground-control-system/app": ["__init__.py", "routes.py", "payload.py", "models.py", "utils.py", "config.py"],
    "uav-ground-control-system/tests": ["test_api.py", "test_payload.py"],
    "uav-ground-control-system/.github/workflows": ["ci-cd.yml"],
    "uav-ground-control-system": ["README.md", "Dockerfile", "docker-compose.yml", "requirements.txt", "app.py"]
}

# Create directories and files
for directory, files in structure.items():
    # Create directory if it doesn't exist
    os.makedirs(directory, exist_ok=True)
    
    # Create each file in the directory
    for file in files:
        file_path = os.path.join(directory, file)
        with open(file_path, 'w') as f:
            # Add content based on file type
            if file == "__init__.py":
                f.write("# Initialize Flask app and database\n")
            elif file == "routes.py":
                f.write("# Define the REST API routes\n")
            elif file == "payload.py":
                f.write("# Simulate payload (imaging) operations\n")
            elif file == "models.py":
                f.write("# Define the database models (Mission, Image)\n")
            elif file == "utils.py":
                f.write("# Helper functions for scheduling, etc.\n")
            elif file == "config.py":
                f.write("# Store configuration values like database URI and paths\n")
            elif file == "test_api.py":
                f.write("# Unit tests for the API\n")
            elif file == "test_payload.py":
                f.write("# Unit tests for payload operations\n")
            elif file == "README.md":
                f.write(
                    "# UAV GCS Project\n\n"
                    "This is a Ground Control Software (GCS) prototype for UAVs.\n"
                    "It manages UAV commands, payload operations (imaging), and stores logs and metadata.\n\n"
                    "## Setup Instructions\n"
                    "1. Create a virtual environment: `python3 -m venv venv`\n"
                    "2. Activate the environment: `source venv/bin/activate`\n"
                    "3. Install dependencies: `pip install -r requirements.txt`\n"
                    "4. Run the Flask app: `python app.py`\n\n"
                    "## API Endpoints\n"
                    "- `/start_mission`: Start a new mission\n"
                    "- `/capture_image`: Capture an image\n"
                    "- `/stop_mission`: Stop the mission\n\n"
                    "## CI/CD\n"
                    "CI/CD pipeline is set up using GitHub Actions.\n"
                )
            elif file == "Dockerfile":
                f.write(
                    "# Dockerfile for UAV GCS project\n\n"
                    "FROM python:3.8-slim-buster\n"
                    "WORKDIR /uav-gcs\n"
                    "COPY requirements.txt requirements.txt\n"
                    "RUN pip install -r requirements.txt\n"
                    "COPY . .\n"
                    "CMD [\"python\", \"app.py\"]\n"
                )
            elif file == "docker-compose.yml":
                f.write(
                    "# docker-compose.yml configuration\n\n"
                    "version: '3.8'\n"
                    "services:\n"
                    "  app:\n"
                    "    build: .\n"
                    "    ports:\n"
                    "      - \"5000:5000\"\n"
                    "    environment:\n"
                    "      - FLASK_ENV=development\n"
                )
            elif file == "ci-cd.yml":
                f.write(
                    "# GitHub Actions workflow for CI/CD\n\n"
                    "name: CI/CD Pipeline\n\n"
                    "on:\n"
                    "  push:\n"
                    "    branches:\n"
                    "      - main\n"
                    "  pull_request:\n"
                    "    branches:\n"
                    "      - main\n\n"
                    "jobs:\n"
                    "  build:\n"
                    "    runs-on: ubuntu-latest\n\n"
                    "    steps:\n"
                    "      - name: Checkout code\n"
                    "        uses: actions/checkout@v2\n\n"
                    "      - name: Set up Python\n"
                    "        uses: actions/setup-python@v2\n"
                    "        with:\n"
                    "          python-version: '3.8'\n\n"
                    "      - name: Install dependencies\n"
                    "        run: |\n"
                    "          python -m venv venv\n"
                    "          source venv/bin/activate\n"
                    "          pip install -r requirements.txt\n\n"
                    "      - name: Run tests\n"
                    "        run: |\n"
                    "          source venv/bin/activate\n"
                    "          pytest\n"
                )
            elif file == "requirements.txt":
                f.write("flask\nflask_sqlalchemy\npytest\nrequests\ngunicorn\n")
            elif file == "app.py":
                f.write(
                    "# Entry point of the Flask app\n\n"
                    "from app import app, db\n\n"
                    "if __name__ == '__main__':\n"
                    "    db.create_all()  # Create tables if they don't exist\n"
                    "    app.run(host='0.0.0.0', port=5000)\n"
                )

print("Directory structure and files created successfully!")
