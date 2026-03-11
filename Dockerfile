# Use a lightweight Python image
FROM python:3.9-slim

# Create a folder called 'app' and move inside it
WORKDIR /app

# Copy your requirements list first (better for speed)
COPY requirements.txt .

# Install the libraries
RUN pip install --no-cache-dir -r requirements.txt

# Copy everything else (your app.py and data folders)
COPY . .

# THE MISSION: Run the script when the container starts
CMD ["python", "app.py"]
