import shutil
import os

def backup_folder(source_folder, backup_folder):
    try:
        # Check if source exists
        if not os.path.exists(source_folder):
            print("Source folder does not exist.")
            return

        # If backup exists, remove it to create a fresh one
        if os.path.exists(backup_folder):
            shutil.rmtree(backup_folder)
            
        # Copy the entire directory
        shutil.copytree(source_folder, backup_folder)
        print(f"Successfully backed up '{source_folder}' to '{backup_folder}'.")
        
    except Exception as e:
        print(f"Backup failed: {e}")

# To test: Create a folder named "MyProject" in your directory.
# backup_folder("MyProject", "MyProject_Backup")