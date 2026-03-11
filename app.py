import os

print("--- Starting Assignment Analysis ---")

# 1. Check Result Images
# We just look for the folder 'result_images' in the current directory
image_folder = 'result_images'
if os.path.exists(image_folder):
    images = [f for f in os.listdir(image_folder) if f.endswith(('.png', '.jpg', '.jpeg'))]
    print(f"Success! I found {len(images)} result images.")
else:
    print("Error: 'result_images' folder not found.")

# 2. Check Simulation Data
data_folder = 'simulation_data'
if os.path.exists(data_folder):
    folders = [f for f in os.listdir(data_folder) if os.path.isdir(os.path.join(data_folder, f))]
    print(f"I found {len(folders)} simulation data folders.")
else:
    print("Error: 'simulation_data' folder not found.")

# 3. Check Election Results
csv_file = 'election_results.csv'
if os.path.exists(csv_file):
    print("Confirmed: Election results are present.")
else:
    print("Error: 'election_results.csv' not found.")

print("--- Analysis Complete! ---")
