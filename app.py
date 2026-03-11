import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    # This keeps the 'website' active so Render stays happy
    return "<h1>Analysis Complete!</h1><p>Cloud Deployment is Successful.</p>"

if __name__ == "__main__":
    # Your analysis prints will still show up in the Logs
    print("--- Starting Assignment Analysis ---")
    print("System Status: Cloud Deployment Successful.")
    
    # This line tells the app to listen for Render's connection
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)    
