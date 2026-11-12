import os
import shutil

def organize_files(folder_path):
    print(f"--- Organizing files in: {folder_path} ---")
    
    # Step 1: Check if the folder exists. If not, create it and add sample files.
    if not os.path.exists(folder_path):
        print(f"Folder '{folder_path}' not found. Creating a test folder with sample files...")
        os.makedirs(folder_path)
        
        # Creating dummy files for testing
        with open(os.path.join(folder_path, "document.txt"), "w") as f:
            f.write("This is a text file.")
        with open(os.path.join(folder_path, "script.py"), "w") as f:
            f.write("print('Hello World')")
        with open(os.path.join(folder_path, "image.jpg"), "w") as f:
            f.write("dummy image data")
    
    # Step 2: Organize the files
    files_moved = 0
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        
        # Check if it is a file (not a folder)
        if os.path.isfile(file_path):
            # Get the file extension (e.g., 'txt', 'py', 'jpg')
            extension = filename.split('.')[-1].lower()
            
            # Create a new folder name based on the extension (e.g., 'txt_files')
            destination_folder = os.path.join(folder_path, f"{extension}_files")
            
            # Create the destination folder if it doesn't exist
            if not os.path.exists(destination_folder):
                os.makedirs(destination_folder)
                
            # Move the file to the destination folder
            shutil.move(file_path, os.path.join(destination_folder, filename))
            print(f"Moved: {filename} -> {extension}_files/")
            files_moved += 1
            
    print(f"\nTotal {files_moved} files organized successfully!")
    print("---------------------------------")

# Run the function
organize_files("Test_Downloads_Folder")
