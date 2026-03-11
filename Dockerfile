# Use a lightweight Python image
FROM python:3.9-slim

# Create a folder called 'app' and move inside it
WORKDIR /app

# Copy your requirements list first (better for speed)
COPY requirements.txt .

# Install the libraries
RUN pip install -r requirements.txt

# Copy everything else (your app.py and data folders)
COPY . .

# THE MISSION: Run the script when the container starts
CMD ["gunicorn", "-b", "0.0.0.0:10000", "app:app"]





