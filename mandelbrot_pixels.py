#!/usr/bin/env python3

"""A script to draw the Mandelbrot set.
"""

from PIL import Image
import numpy as np


def main():
    # Basic definitions
    boundary = 4
    max_iterations = 20
    y_range = (-1, 1)
    x_range = (-1.5, 0.5)
    size = 1000

    # Set scaling parameters
    y_step = (y_range[1] - y_range[0]) / (size-1)
    x_step = (x_range[1] - x_range[0]) / (size-1)
    y_values = [y_range[0] + i*y_step for i in range(size)]
    x_values = [x_range[0] + i*x_step for i in range(size)]

    # Fill the print matrix
    value_matrix = []
    for y in y_values:
        value_line = []
        for x in x_values:
            in_boundary, i = is_in_boundary(x + y*1j, boundary, max_iterations)
            value_line.append(i if not in_boundary else None)
        value_matrix.append(value_line)

    draw_matrix(value_matrix, max_iterations)


# Calculate if the iterative function stays inside boundary
def is_in_boundary(c, boundary, max_iterations):
    z = 0
    for i in range(max_iterations):
        z = z ** 2 + c
        if abs(z) > boundary:
            return False, i
    return True, None


# Draw the matrix in matplotlib
def draw_matrix(value_matrix, max_iterations):
    # Check for errors and set basic variables
    y_dim = len(value_matrix)
    if y_dim == 0:
        return
    x_dim = len(value_matrix[0])
    if x_dim == 0:
        return
    image = Image.new('HSV', (x_dim, y_dim))
    color_step = 360 / max_iterations

    # Put pixels with color scale on screen
    for row_index, row in enumerate(value_matrix):
        for value_index, value in enumerate(row):
            if value is not None:
                image.putpixel((value_index, row_index), (int(360 - value * color_step), 100, 100))

    # Convert image to RGB and save it
    image.convert("RGB").save("output.png")


if __name__ == '__main__':
    main()