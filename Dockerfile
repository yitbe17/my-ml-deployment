# Use the same Python version we've been using
FROM python:3.9-slim

# Create a folder inside the container for our project
WORKDIR /app

# Copy EVERYTHING from your Windows folder into the container /app folder
COPY . .

# If your project needs specific libraries, you would add them here
# RUN pip install pandas matplotlib

# Tell Docker which file to run when the container starts
CMD ["python", "app.py"]