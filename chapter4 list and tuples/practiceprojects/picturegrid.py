# grid = [['.', '.', '.', '.', '.', '.'],
#         ['.', 'O', 'O', '.', '.', '.'],
#         ['O', 'O', 'O', 'O', '.', '.'],
#         ['O', 'O', 'O', 'O', 'O', '.'],
#         ['.', 'O', 'O', 'O', 'O', 'O'],
#         ['O', 'O', 'O', 'O', 'O', '.'],
#         ['O', 'O', 'O', 'O', '.', '.'],
#         ['.', 'O', 'O', '.', '.', '.'],
#         ['.', '.', '.', '.', '.', '.']]
# Think of grid[x][y] as being the character at the x- and y-coordinates of a “picture” drawn with text characters. The (0, 0) origin is in the upper-left corner, the x-coordinates increase going right, and the y-coordinates increase going down.
# Copy the previous grid value, and write code that uses it to print the image.
# ..OO.OO..
# .OOOOOOO.
# .OOOOOOO.
# ..OOOOO..
# ...OOO...
# ....O....


grid = [['.', '.', '0', '0', '.', '0', '0', '.', '.'],
        ['.', '0', '0', '0', '0', '0', '0', '0', '.'],
        ['.', '0', '0', '0', '0', '0', '0', '0', '.'],
        ['.', '.', '0', '0', '0', '0', '0', '.', '.'],
        ['.', '.', '.', '0', '0', '0', '.', '.', '.'],
        ['.', '.', '.', '.', '0', '.', '.', '.', '.'],
]

for i in range(5):
    for j in range(9):
        print(grid[i][j], end='')
    print()

