import os

def file_analyzer_tool(filename):
    print(f"Analyzing '{filename}'...")
    try:
        # Get file size
        size_in_bytes = os.path.getsize(filename)
        
        # Read content to count words
        with open(filename, 'r') as file:
            content = file.read()
            word_count = len(content.split())
            
        print("-" * 20)
        print(f"File Size: {size_in_bytes} bytes")
        print(f"Word Count: {word_count}")
        print("-" * 20)
        
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")

# Create a file to test
with open("my_notes.txt", "w") as f:
    f.write("This is a simple note for testing the utility tool. It counts words.")

file_analyzer_tool("my_notes.txt")