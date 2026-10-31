import os
import shutil

def organize_files(folder_path):
    if not os.path.exists(folder_path):
        print("Folder does not exist.")
        return
        
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        
        # Check if it's a file
        if os.path.isfile(file_path):
            # Get file extension (e.g., 'txt', 'jpg')
            ext = filename.split('.')[-1].lower()
            dest_folder = os.path.join(folder_path, f"{ext}_files")
            
            # Create destination folder if it doesn't exist
            if not os.path.exists(dest_folder):
                os.makedirs(dest_folder)
                
            # Move the file
            shutil.move(file_path, os.path.join(dest_folder, filename))
            print(f"Moved {filename} to {ext}_files folder.")

# To test: Create a folder named "TestDir" and put some .txt and .png files in it.
# organize_files("TestDir")