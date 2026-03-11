import os
import time

def run_analysis():
    print("--- Starting Assignment Analysis ---")
    time.sleep(1) # Adds a little dramatic effect
    
    # Look at the files in the current folder
    files = os.listdir('.')
    
    # Count the images and data files
    images = [f for f in files if f.endswith('.png')]
    data_folders = [f for f in files if 'simulation_data' in f]
    
    print(f"Success! I found {len(images)} result images.")
    print(f"I found {len(data_folders)} simulation data folders.")
    
    if 'election_result.png' in images:
        print("Confirmed: Election results are present.")
    
    print("--- Analysis Complete! ---")

if __name__ == "__main__":
    run_analysis()
