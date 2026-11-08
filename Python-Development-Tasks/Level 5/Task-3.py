import os
import shutil

print("--- Starting Backup Process ---")

# Define folder names
source_folder = "MyProject"
backup_folder = "Backup_MyProject"

# 1. Check if source folder exists
if not os.path.exists(source_folder):
    print(f"Error: '{source_folder}' does not exist.")
    print("Please create a 'MyProject' folder and add some files to it.")
else:
    print(f"Found source folder: {source_folder}")
    
    # 2. If an old backup exists , remove it to create a fresh one
    if os.path.exists(backup_folder):
        shutil.rmtree(backup_folder)
        print("Old backup removed.")
        
    # 3. Copy the entire dirctory
    shutil.copytree(source_folder, backup_folder)
    print(f"Success! '{source_folder}' has been successfully backed up to '{backup_folder}'.")
    print("Check the Explorer panel on the left to verify.")

print("--- Backup Process Finished ---")
