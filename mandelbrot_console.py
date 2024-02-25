#!/usr/bin/env python3

"""A script to draw the Mandelbrot set.
"""


def main():
    # Basic definitions
    boundary = 4
    iterations = 20
    y_range = (-1, 1)
    x_range = (-1.5, 0.5)
    size = 40

    # Set scaling parameters
    y_step = (y_range[1] - y_range[0]) / (size-1)
    x_step = (x_range[1] - x_range[0]) / (size-1)
    y_values = [y_range[0] + i*y_step for i in range(size)]
    x_values = [x_range[0] + i*x_step for i in range(size)]

    # Fill the print matrix
    print_matrix = []
    for y in y_values:
        print_line = ""
        for x in x_values:
            in_boundary, z = is_in_boundary(x + y*1j, boundary, iterations)
            print_line += "x" if in_boundary else " "
        print_matrix.append(print_line)
    draw_matrix(print_matrix)


# Calculate if the iterative function stays inside boundary
def is_in_boundary(c, boundary, iterations):
    z = 0
    for _ in range(iterations):
        z = z ** 2 + c
        if abs(z) > boundary:
            return False, z
    return True, z


# Draw the matrix on the console with a border
def draw_matrix(print_matrix):
    # Check for errors and set basic variables
    if len(print_matrix) == 0:
        return
    matrix_width = len(print_matrix[0])
    vertical_border = "+" + "-" * matrix_width + "+"

    # Print matrix with border
    print(" ".join(vertical_border))
    for print_line in print_matrix:
        print(" ".join("|" + print_line + "|"))
    print(" ".join(vertical_border))


if __name__ == '__main__':
    main()