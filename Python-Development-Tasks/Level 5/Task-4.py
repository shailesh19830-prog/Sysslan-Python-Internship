import os

def file_analyzer_tool(filename):
    print(f"--- Analyzing '{filename}' ---")
    
    # Step 1: Check if file exists. If not, create a dummy file automatically.
    if not os.path.exists(filename):
        print(f"File '{filename}' not found. Creating a new test file...")
        with open(filename, 'w') as f:
            f.write("This is a sample text file for the utility tool. It calculates size and word count.")
            
    try:
        # Step 2: Get file size in bytes
        size_in_bytes = os.path.getsize(filename)
        
        # Step 3: Read content and count words
        with open(filename, 'r') as file:
            content = file.read()
            word_count = len(content.split())
            
        # Step 4: Display results
        print(f"File Size: {size_in_bytes} bytes")
        print(f"Word Count: {word_count} words")
        print("-----------------------------")
        
    except Exception as e:
        print(f"An error occurred: {e}")

# Run the tool
file_analyzer_tool("my_notes.txt")
