This program allows you to draw polyhedra from a matrix that represents the height of cubes in a three-dimensional arrangement. 
It uses the `matplotlib` library to visualize the cubes in a 3D plot.

## Description

The program reads an input file containing a matrix of integers. Each number in the matrix indicates the number of stacked cubes 
at that specific position. From this information, the program generates a 3D visualization of the polyhedron and can set axes, select the color, and choose the transparency.

## Requirements

- Python 3.x
- `matplotlib` library

Usage
Prepare a text file named matrix.txt with the following structure:

0,1,0,2
3,0,1,0
0,2,1,1
1,0,0,3

Each number represents the number of stacked cubes at that position and can be changed(row, column).

Run the program:

You will need to run the drawPolyhedra program, then enter the name of the matrix.txt file (it can be another name but in .txt format), choose 
whether to create the graphical representation with axes, select the color, and choose the transparency."
