#Crear funcion que doble los numeros dados en una lista 
def double_numbers(numeros):
    return list(map(lambda x: x * 2, numeros))
lista_original = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
lista_doblada = double_numbers(lista_original)
print(lista_doblada) 