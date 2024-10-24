
# Programa que permite dibujar poliedros por pantalla y calcular el numero de caras de este


# BLOQUE DE DEFINICIONES
# IMPORTACION DE MODULOS
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
from numpy import array
import matplotlib.pyplot as plotter

# DEFINICIÓN DE FUNCIONES

# Función que transforma un archivo de texto en una matriz
# Entrada: un archivo de texto con la matriz
# Salida: una matriz con elementos expresados como strings
def leerFichero(archivo):
    matrizString = []
    if ".txt" in archivo:
        ficheroLectura = open(archivo, "r")
    else:
        ficheroLectura = open(archivo + ".txt", "r")
    
    for linea in ficheroLectura:
        lineaSinEspacio = linea.strip()
        fila = lineaSinEspacio.split(",")
        matrizString.append(fila)
    
    ficheroLectura.close()
    return matrizString

# Función que verifica si la matriz es valida
def validarMatrizDeString(matrizDeString):
    tamanoFila = len(matrizDeString)
    tamanoColumna = len(matrizDeString[0])
    cuentaSimbolos = 0
    
    for fila in range(tamanoFila):
        for columna in range(tamanoColumna):
            if matrizDeString[fila][columna].isalpha() or not matrizDeString[fila][columna].isdigit():
                cuentaSimbolos += 1
    
    return cuentaSimbolos == 0

# Función que transforma una matriz con elementos en string a una matriz con elementos enteros
def transformarMatriz(matriz):
    matrizDeEnteros = []
    for fila in matriz:
        filaMatriz = [int(columna) for columna in fila]
        matrizDeEnteros.append(filaMatriz)
    return matrizDeEnteros

def menuColores():
    while True:
        menu = '''
        Representacion del poliedro en colores:
                1. Azul
                2. Rojo
                3. Verde
                4. Amarillo
                5. Cian
                6. Magenta
                7. Naranjo
                8. Negro
                '''
        print(menu)
        color = input("Por favor, seleccione un numero para el color de su poliedro: ")
        
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
            print('Numero no valido.')
            if input('Desea volver a ingresar numero? Si=1, No=0: ') != "1":
                exit()

def menuTransparencia():
    while True:
        menu = '''
        Niveles de transparencia del poliedro
               1. Transparencia total
               2. Transparencia alto
               3. Transparencia medio
               4. Transparencia bajo
               5. Transparencia nula
                '''
        print(menu)
        opcion = input("Por favor, ingrese la opción que desea: ")
        
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
            print('Numero no valido.')
            if input('Desea volver a ingresar numero? Si=1, No=0: ') != "1":
                exit()

# Función que permite dibujar las coordenadas X del cubo
def ubicarCuboEnEjeX(x):
    largo = 1
    superficieX = [[x, x + largo, x + largo, x, x],
                    [x, x + largo, x + largo, x, x],
                    [x, x + largo, x + largo, x, x],
                    [x, x + largo, x + largo, x, x]]
    return array(superficieX)

# Función que permite dibujar las coordenadas Y del cubo
def ubicarCuboEnEjeY(y):
    ancho = 1
    superficieY = [[y, y, y + ancho, y + ancho, y],
                    [y, y, y + ancho, y + ancho, y],
                    [y, y, y, y, y],
                    [y + ancho, y + ancho, y + ancho, y + ancho, y + ancho]]
    return array(superficieY)

# Función que permite dibujar las coordenadas Z del cubo
def ubicarCuboEnEjeZ(z):
    altura = 1
    superficieZ = [[z, z, z, z, z],
                    [z + altura, z + altura, z + altura, z + altura, z + altura],
                    [z, z, z + altura, z + altura, z],
                    [z, z, z + altura, z + altura, z]]
    return array(superficieZ)

# Función que permite dibujar el poliedro
def dibujarPoliedro(matriz, opcion, transparencia):
    matrizReal = array(matriz)
    graficoPoliedro = plotter.figure("Poliedro")
    graficoPoliedro3D = graficoPoliedro.add_subplot(111, projection='3d')
    graficoPoliedro3D.set_aspect('equal')
    graficoPoliedro3D.set_xlabel("eje X")
    graficoPoliedro3D.set_ylabel("eje Y")
    graficoPoliedro3D.set_zlabel("eje Z")
    
    nFilas = len(matrizReal)
    nColumnas = len(matrizReal[0])

    for i in range(nFilas):
        for j in range(nColumnas):
            elementoMatrizReal = matrizReal[i][j]
            if elementoMatrizReal > 0:
                for k in range(elementoMatrizReal):
                    posicionCubo = [i, j, k]
                    X = ubicarCuboEnEjeX(posicionCubo[0])
                    Y = ubicarCuboEnEjeY(posicionCubo[1])
                    Z = ubicarCuboEnEjeZ(posicionCubo[2])
                    graficoPoliedro3D.plot_surface(X, Y, Z, color=opcion, rstride=1, cstride=1, alpha=transparencia)

    while True:
        decision = input('''¿Desea incluir los ejes cartesianos en el grafico? Si/No: ''')
        if decision.lower() == "si":
            graficoPoliedro3D.set_axis_on()
            plotter.show()
            break
        elif decision.lower() == "no":
            graficoPoliedro3D.set_axis_off()
            plotter.show()
            break
        else:
            print('Su entrada no es valida.')
            if input('¿Desea volver al programa? Si/No: ').lower() != "si":
                exit()

# BLOQUE PRINCIPAL
matriz = input('''Bienvenido al programa para dibujar poliedros.
Por favor, ingrese el nombre del archivo de texto a trabajar: ''')
color = menuColores()
transparencia = menuTransparencia()
matrizString = leerFichero(matriz)
matrizValida = validarMatrizDeString(matrizString)

if matrizValida:
    matrizEnteros = transformarMatriz(matrizString)
    print('''La matriz asociada al poliedro es la siguiente:''')
    print(array(matrizEnteros))
    dibujarPoliedro(matrizEnteros, color, transparencia)
else:
    print("ERROR: la matriz que usted introdujo, no es valida")