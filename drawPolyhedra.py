
# Program that allows drawing polyhedra on the screen

# BLOCK OF DEFINITIONS
# MODULE IMPORTS
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
from numpy import array
import matplotlib.pyplot as plotter

# FUNCTION DEFINITIONS

# Function that transforms a text file into a matrix
# Input: a text file with the matrix
# Output: a matrix with elements expressed as strings
def readMatrix(nameTxt):
    matrixString = []
    if ".txt" in nameTxt:
        nameMatrix = open(nameTxt, "r")
    else:
        nameMatrix = open(nameTxt + ".txt", "r")
    
    for line in nameMatrix:
        lineSpaceless = line.strip()
        row = lineSpaceless.split(",")
        matrixString.append(row)
    
    nameMatrix.close()
    return matrixString

# Function that checks if the matrix is valid
def chekMatrixString(matrixString):
    lenghtRow = len(matrixString)
    lenghtColumn = len(matrixString[0])
    countedSimbols = 0
    
    for row in range(lenghtRow):
        for column in range(lenghtColumn):
            if matrixString[row][column].isalpha() or not matrixString[row][column].isdigit():
                countedSimbols += 1
    
    return countedSimbols == 0

# Function that transforms a matrix with elements as strings into a matrix with integer elements
def transformMatrix(matrix):
    integerMatrix = []
    for row in matrix:
        rowMatrix = [int(column) for column in row]
        integerMatrix.append(rowMatrix)
    return integerMatrix

def colorsMenu():
    while True:
        menu = '''
        Polyhedron color representation:
                1. Blue
                2. Red
                3. Green
                4. Yellow
                5. Cyan
                6. Magenta
                7. Orange
                8. Black
                '''
        print(menu)
        color = input("Please, select a number for your polyhedron's color: ")
        
        if color == "1":
            return "b"
        elif color == "2":
            return "r"
        elif color == "3":
            return "g"
        elif color == "4":
            return "y"
        elif color == "5":
            return "c"
        elif color == "6":
            return "m"
        elif color == "7":
            return "orange"
        elif color == "8":
            return "k"
        else:
            print('Invalid number.')
            if input('Do you want to re-enter a number? Yes=1, No=0: ') != "1":
                exit()

def transparencyMenu():
    while True:
        menu = '''
        Polyhedron transparency levels:
               1. Full transparency
               2. High transparency
               3. Medium transparency
               4. Low transparency
               5. No transparency
                '''
        print(menu)
        opcion = input("Please, select your option: ")
        
        if opcion == "1":
            return 0.1
        elif opcion == "2":
            return 0.3
        elif opcion == "3":
            return 0.5
        elif opcion == "4":
            return 0.8
        elif opcion == "5":
            return 1
        else:
            print('Invalid number.')
            if input('Do you want to re-enter a number? Yes=1, No=0: ') != "1":
                exit()

# Function that allows drawing the X coordinates of the cube
def setCubeInX(x):
    lenght = 1
    xSurface = [[x, x + lenght, x + lenght, x, x],
                    [x, x + lenght, x + lenght, x, x],
                    [x, x + lenght, x + lenght, x, x],
                    [x, x + lenght, x + lenght, x, x]]
    return array(xSurface)

# Function that allows drawing the Y coordinates of the cube
def setCubeInY(y):
    broad = 1
    ySurface = [[y, y, y + broad, y + broad, y],
                    [y, y, y + broad, y + broad, y],
                    [y, y, y, y, y],
                    [y + broad, y + broad, y + broad, y + broad, y + broad]]
    return array(ySurface)

# Function that allows drawing the Z coordinates of the cube
def setCubeInZ(z):
    height = 1
    zSurface = [[z, z, z, z, z],
                    [z + height, z + height, z + height, z + height, z + height],
                    [z, z, z + height, z + height, z],
                    [z, z, z + height, z + height, z]]
    return array(zSurface)

# Function that allows drawing the polyhedron
def DrawPolyhedra(matrix, option, transparency):
    realMatrix = array(matrix)
    polyhedraGraphic = plotter.figure("Polyhedron")
    polyhedraGraphic3D = polyhedraGraphic.add_subplot(111, projection='3d')
    polyhedraGraphic3D.set_aspect('equal')
    polyhedraGraphic3D.set_xlabel("X axis")
    polyhedraGraphic3D.set_ylabel("Y axis")
    polyhedraGraphic3D.set_zlabel("Z axis")
    
    nFilas = len(realMatrix)
    nColumnas = len(realMatrix[0])

    for i in range(nFilas):
        for j in range(nColumnas):
            elementRealMatrix = realMatrix[i][j]
            if elementRealMatrix > 0:
                for k in range(elementRealMatrix):
                    cubePosition = [i, j, k]
                    X = setCubeInX(cubePosition[0])
                    Y = setCubeInY(cubePosition[1])
                    Z = setCubeInZ(cubePosition[2])
                    polyhedraGraphic3D.plot_surface(X, Y, Z, color=option, rstride=1, cstride=1, alpha=transparency)

    while True:
        decision = input('''Do you want to include Cartesian axes in the graph? Yes/No: ''')
        if decision.lower() == "yes":
            polyhedraGraphic3D.set_axis_on()
            plotter.show()
            break
        elif decision.lower() == "no":
            polyhedraGraphic3D.set_axis_off()
            plotter.show()
            break
        else:
            print('Your input is invalid.')
            if input('Do you want to return to the program? Yes/No: ').lower() != "yes":
                exit()

# MAIN BLOCK
matrix = input('''Welcome to the polyhedron drawing program.
Please, enter the name of the text file to work with: ''')
color = colorsMenu()
transparency = transparencyMenu()
matrixString = readMatrix(matrix)
isValidMatrix = chekMatrixString(matrixString)

if isValidMatrix:
    matrizEnteros = transformMatrix(matrixString)
    print('''The matrix associated with the polyhedron is as follows:''')
    print(array(matrizEnteros))
    DrawPolyhedra(matrizEnteros, color, transparency)
else:
    print("ERROR: the matrix you entered is not valid")