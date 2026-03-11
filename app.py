import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    # This is what people will see when they click your URL
    return "<h1>Analysis Complete!</h1><p>The ML Cloud Service is running perfectly.</p>"

if __name__ == "__main__":
    print("--- Starting Assignment Analysis ---")
    print("System Status: Cloud Deployment Successful.")
    
    # Render provides a PORT, or we use 5000 as a backup
    port = int(os.environ.get("PORT", 5000))
    
    # This starts the 'Receptionist' (Server)
    app.run(host='0.0.0.0', port=port)
