def read_file_safely(filename):
    try:
        # 'with' ensures the file is closed automatically
        with open(filename, 'r') as file:
            print(f"--- Reading {filename} ---")
            for line_number, line in enumerate(file, 1):
                # strip() removes extra newline characters
                print(f"Line {line_number}: {line.strip()}")
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")

# Create a dummy file to test
with open("test.txt", "w") as f:
    f.write("Hello\nThis is a test file.\nPython is fun.")

read_file_safely("test.txt")
read_file_safely("missing.txt") # Testing the error handling