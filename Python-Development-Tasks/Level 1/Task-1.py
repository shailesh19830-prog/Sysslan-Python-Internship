# Creating a 3x3 grid and displaying it
grid = [
    [1, 2, 3],
    [4, 5, 6],
    [6, 7, 8]
]

print("--- 3x3 Number Grid ---")
for row in grid:
    #printing number separated by a space for a clean look
    print(f"{row[0]} {row[1]} {row[2]}")