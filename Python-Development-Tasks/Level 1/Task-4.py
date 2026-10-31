# Verify whether all number in the grid are unique
grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# To test duplicates, change the grid to : [[1, 2, 3] ,[4, 5, 6] ,[7, 8, 9,]
# Flattening the 2D grid into a 1D list
all_numbers =[]
for row in grid:
    all_numbers.extend(row)

# A set automatically remove duplicates. if the  original list, they are unique.
if len(all_numbers) == len(set(all_numbers)):
    print("Result: All number in the grid are unique.")
else:
    print("Result: The grid contains duplicate number.")        