import os

def generateMatrix():
    n = int(input("Ingrese la dimensión de la matriz: "))
    
    matrix = generateTemplate(n)

    for i in range(n):
        for j in range(n):
            clearConsole()
            printMatrix(matrix)
            matrix[i][j] = float(input(f"\n\nIngrese el valor de a{i + 1}{j + 1}: "))
    
    return matrix

def det(matrix):
    if len(matrix) == len(matrix[0]) == 1:
        return matrix[0][0]

    elif len(matrix) == len(matrix[0]):
        determinant = 0

        for i in range(len(matrix[0])):
            small_matrix = []
            for j in range(1, len(matrix)):
                small_matrix.append(matrix[j][:i] + matrix[j][i + 1:])

            determinant += (-1) ** (2 + i) * matrix[0][i] * det(small_matrix)

    else:
        return "Matrix must be square"

    return determinant

def printMatrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if j == 0:
                print("\n\t", end="")
            print(f" {matrix[i][j]}", end="  ")
            

def generateTemplate(n):
    template = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(f"a{i + 1}{j + 1}")
        template.append(row)
    return template

def clearConsole():
    os.system('cls' if os.name=='nt' else 'clear')

def main():
    clearConsole()
    matrix = generateMatrix()
    clearConsole()
    print("Insertada la matriz: ")
    printMatrix(matrix)
    print("\n\nSu determinante es: ")
    print(f"\t {det(matrix)}")


main()
