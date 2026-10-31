# Create a dummy file first
with open("numbers.txt", "w") as f:
    f.write("10\n20\n30\n40\n50")

def analyze_numbers(filename):
    try:
        with open(filename, "r") as file:
            # Read lines, strip whitespace, and convert to integers
            numbers = [int(line.strip()) for line in file if line.strip()]
            
            if not numbers:
                print("File is empty.")
                return
                
            total = sum(numbers)
            average = total / len(numbers)
            maximum = max(numbers)
            
            print(f"Data read: {numbers}")
            print(f"Total Sum: {total}")
            print(f"Average: {average}")
            print(f"Maximum: {maximum}")
            
    except FileNotFoundError:
        print("File not found.")

analyze_numbers("numbers.txt")