numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def multiplicar_por_2(x):
    resultado = x * 2
    return resultado

def impar_cero(x):
    if x % 2 == 0:
        return x
    else: 
        return 0

print(list(map(impar_cero, numeros)))

numeros2 = [1, -4, 11, -14, 7, 9, 22, -1]

def num_positivo(y):
    if y >= 0:
        return True
    else: 
        return False

print(list(filter(num_positivo, numeros2)))

numeros3 = [1, 100, 50, 2, 3, 4, 5, 6, 75, 55, 60, 74, 22, 11, 15]

def num_par(z):
    if z % 2 == 0:
        return True
    else:
        return False

def num_mayor50(z):
    if z >= 50:    
        return True
    else:
        return False

def none_mayor50(and_example):
    if num_par(and_example) and num_mayor50(and_example):
        return True
    else:
        return False

def none_mayor50(or_example):
    if num_par(or_example) or num_mayor50(or_example):
        return True
    else:
        return False

print(list(filter(none_mayor50, numeros3)))
print(list(filter(lambda x: not num_par(x), numeros3)))



