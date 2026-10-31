# Calculate and display the sum of each row in the grid
grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("--- Sum of Each Row ---")
for i, row in enumerate(grid):
    #Using Python's built-in sum() function
    row_sum = sum(row)
    print(f"Row {i+1}: {row} -> sum = {row_sum}")