def contar_resta_banana(string):
    letras_banana = {'b': 1, 'a': 3, 'n': 2}
    conteo_actual = {'b': 0, 'a': 0, 'n': 0}
    resultado = 0
    string = string.lower()

    for letra in string: # O(m), m es la longitud de la cadena 'string'
        if letra in letras_banana:
            conteo_actual[letra] += 1
        while all(conteo_actual[letra] >= letras_banana[letra] for letra in letras_banana): # O(n), n es el tamaño del conjunto de letras_banana
            resultado += 1
            for letra in letras_banana: # O(n), n es el tamaño del conjunto de letras_banana
                conteo_actual[letra] -= letras_banana[letra]
    return resultado

#complejidad algoritmica O(m*n^2) 

# Ejemplos de uso
string1 = "ban"
string2 = "BANXYTANAFD"
string3 = "ANANABXGEBANANAHG"

print(contar_resta_banana(string1))  # Salida: 0
print(contar_resta_banana(string2))  # Salida: 1
print(contar_resta_banana(string3))  # Salida: 2