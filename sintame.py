def check_diagonals_left_to_right(grid):
  """
  Checks if the diagonals (from left to right) of a grid are all equal.

  Args:
    grid: A 2D list of integers representing the grid.

  Returns:
    True if all the diagonals are equal, False otherwise.
  """

  # Get the size of the grid.
  n = len(grid)

  # Check if the diagonals are all equal.
  for i in range(n):
    for j in range(n):
      if i == j:
        if grid[i][j] != grid[0][0]:
          return False
  return True
