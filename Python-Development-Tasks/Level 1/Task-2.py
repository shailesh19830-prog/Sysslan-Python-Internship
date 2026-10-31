# check whether a given number exists in the predefined grid
grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# you can change this number to test
search_num = int(input("Enter a number to search in the grid: "))
found = False

# Loop throught rows and columns to find the number
for row in grid:
    if search_num in row:
        found = True
        break

if found:
    print(f"Result: Yes, {search_num} exists in the grid.")
else:
    print(f"Result : No, {search_num} dose not exit in the grid")        