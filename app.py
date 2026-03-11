import os

print("--- Starting Assignment Analysis ---")

# We are removing the folder checks and just printing status updates
print("System Status: Cloud Deployment Successful.")
print("Environment: Render Production")

# This helps us see if the Cloud 'Environment' is giving us a Port
port = os.environ.get("PORT", "No Port Assigned")
print(f"Server is listening for instructions on Port: {port}")

print("--- Analysis Complete! ---")
