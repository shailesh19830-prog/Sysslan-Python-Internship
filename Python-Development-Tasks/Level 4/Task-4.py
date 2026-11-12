def analyze_numerical_data(filename):
    print(f"--- Processing file: {filename} ---")
    
    # Step 1: Check if file exists. If not, create a test file.
    try:
        with open(filename, 'r') as file:
            pass
    except FileNotFoundError:
        print(f"File '{filename}' not found. Creating a sample file for testing...")
        with open(filename, 'w') as file:
            file.write("10\n20\n30\n40\n50\n") # Sample numbers

    # Step 2: Read data and calculate Total, Average, and Max
    try:
        with open(filename, 'r') as file:
            # Read lines, remove spaces, and convert to integers
            numbers = [int(line.strip()) for line in file if line.strip()]
            
            if not numbers:
                print("The file is empty or does not contain valid numbers.")
                return

            total = sum(numbers)
            average = total / len(numbers)
            maximum = max(numbers)
            
            # Step 3: Display the results
            print(f"Data read from file: {numbers}")
            print(f"Total Sum: {total}")
            print(f"Average: {average}")
            print(f"Maximum Number: {maximum}")
            print("---------------------------------")
            
    except ValueError:
        print("Error: The file contains non-numerical data. Please ensure it only has numbers.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Run the function
analyze_numerical_data("numbers_data.txt")
