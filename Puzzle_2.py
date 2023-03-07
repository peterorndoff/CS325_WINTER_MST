import itertools

# Define the matrix
matrix = [(i, j) for i in range(3) for j in range(3)]

# Generate all possible combinations of the matrix
combinations = list(itertools.combinations(matrix, 2))

# Print the combinations
print(combinations)