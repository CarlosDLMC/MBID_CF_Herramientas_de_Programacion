# Ejercicio 1: Identificador válido

# En este caso usaremos la función incluida en python, isalpha()
# Dado que el resultado únicamente depende de la primera letra, sólo
# analizaremos esta, y devolveremos inmediatamente el resultado

print("Ejercicio 1:\n")

def FirstChar(palabra):
    return palabra[0].isalpha() or palabra[0] == "_"

# Prueba:
for word in ["paciente001", "P001", "1Pac", "_001", ":p001"]:
    respuesta = "Sí" if FirstChar(word) else "No"
    print(f"La palabra {word} es un Identificador válido: {respuesta}")

# Ejercicio 2: Porcentaje de vocales
# En este caso contaremos el número de vocales de cada palabra y los dividiremos
# entre la cantidad de letras de la misma. En el caso de que no haya palabra,
# lanzaremos un error con un mensaje personalizado
print("\nEjercicio 2:\n")

class NoWordException(Exception):
    pass

def porcentVocal(palabra):
    if not palabra:
        raise NoWordException("¡ERROR! Necesitas escribir una palabra")
    vocales = "aeiouAEIOU"
    count = 0
    for letter in palabra:
        if letter in vocales:
            count += 1
    return round((count / len(palabra) * 100), 1)

for word in ["Hola", "acacia", "Brrr", "aEa", ""]:
    try:
        print(f"Porcentaje de vocales en {word}: {porcentVocal(word)}")
    except NoWordException as e:
        print(e)


# Ejercicio 3: Nuevo string
# En esta función vamos a crear un nuevo string y vamos a iterar por el string
# original. Las consonantes las sumaremos igual, y las vocales el número de veces
# que se indique en el argumento. En el caso de que el usuario introduzca un
# número negativo o una palabra vacía, le saltará un error
# Para el segundo caso, utilizaremos la clase NoWordException creada en el segundo
# ejercicio

print("\nEjercicio 3:\n")

class NegativeNumberException(Exception):
    pass

def nuevo_string(palabra, multiplicador_de_vocales):
    if not palabra:
        raise NoWordException("¡ERROR! Necesitas escribir una palabra")
    if multiplicador_de_vocales < 0:
        raise NegativeNumberException("¡ERROR! Tienes que introducir un número positivo")
    nueva_palabra = ""
    vocales = "aeiouAEIOU"
    for letra in palabra:
        if letra in vocales:
            nueva_palabra += multiplicador_de_vocales * letra
        else:
            nueva_palabra += letra
    return nueva_palabra

for word, multiplicator in [("Charleston", 2), ("RTD11", 3), ("H2O", 3), ("", 1), ("negativo", -2)]:
    try:
        print(f"nuevo_string(\"{word}\", {multiplicator}) = {nuevo_string(word, multiplicator)}")
    except NoWordException as e:
        print(e)
    except NegativeNumberException as e:
        print(e)

# Ejercicio 4: Notas al pie de página
# En esta función vamos a iterar por la string que recibamos, además vamos a llevar
# la cuenta de asteriscos con un parámetro dentro de la función. Cada vez que nos
# encontremos con un asterisco, lo sustituiremos por el número (entre paréntesis)
# que le corresponda y aumentaremos nuestro contador en 1.

print("\nEjercicio 4:\n")

def notas_al_pie(original):
    result = ""
    count = 1
    for letter in original:
        if letter == "*":
            result += f"({count})"
            count += 1
        else:
            result += letter
    return result

for nota in ["Esta es la primera nota*; y esta la segunda*.", "Esta frase no tiene notas. Esta otra tampoco.", "*,*. *.", ""]:
    print(notas_al_pie(nota))

# Ejercicio 5: Calcula código
# Para añadir un poco más de dificultad, en esta ocasión vamos a resolver el problema
# de una forma más original, en una sola línea de código. Utilizando la string convertida
# en una lista de caracteres, usamos list comprehension para filtrar las mayúsculas, y
# lo devolvemos a string con el método join(). A esta string le sumamos la cantidad total
# de caracteres que contiene la string original, eliminando los espacios

print("\nEjercicio 5:\n")

def codigo(nombre_completo):
    return "".join([letter for letter in list(nombre_completo) if letter.isupper()]) + str(len(nombre_completo.replace(" ", "")))

for full_name in ["Mireia Belmonte García", "Bruce Frederick Joseph Springsteen", "", "Gerard Piqué Bernabéu", "Sergio Ramos García"]:
    print(f"\"{full_name}\" -> {codigo(full_name)}")

# Ejercicio 6: Contador de hidrógenos
# En esta función vamos a iterar por la string que se nos dé, y cada vez que aparezca
# una "H" vamos a mirar al siguiente carácter, aprovechando que el número de hidrógenos
# sólo va a ocupar un carácter en la string. Si no hay un número, lo contaremos como 1.
# Vamos a iterar de la forma clásica, con el índice, porque así será más fácil comprobar
# si el siguiente carácter existe, para que no nos de error a la hora de buscar número
# en el caso de que "H" esté al final de la string.

print("\nEjercicio 6:\n")

def contar_hidrogenos(molecula):
    count = 0
    for i in range(len(molecula)):
        if molecula[i] == 'H':
            if i < len(molecula) - 1 and molecula[i + 1].isdigit():
                count += int(molecula[i + 1])
            else:
                count += 1
    return count

for molecula in ['HIO', 'H2O', 'C2H5O', 'Fe3O4', 'C2OH']:
    print(f"Átomos de hidrógeno en la molécula {molecula}: {contar_hidrogenos(molecula)}")

# Ejercicio 7: Temperatura media en rango [15, 45]
# Esta vez volvemos a intentar resolver el problema en una línea. Para mayor variedad,
# ahora filtramos la lista con el método filter(), al que le indicamos nuestros requisitos
# en una función lambda. Con la función sum() sumamos sus elementos y lo dividimos entre la
# cantidad de elementos de la lista. Si la lista tras el filtro está vacía, devolvemos
# -1 automáticamente

print("\nEjercicio 7:\n")

def mediaTempRang(lst):
    filtrada = list(filter(lambda x: x >= 15 and x <= 45, lst))
    return round(sum(filtrada) / len(filtrada), 2) if filtrada else -1

for lista in ([34.5, 12.9, 15, 43, 51.4, 23.4], [45.5, 12.9, 15, 32.5, 51.4, 21.2], [14.5, 12.6, 47.8], [15, 16, 14, 50, 17]):
    print(f"{lista} ===> {mediaTempRang(lista)} ")

# Ejercicio 8: Umbral de presión de sonido
# En esta función vamos a iterar por cada elemento de la lista. El parámetro found nos
# indica si ya ha sido encontrada una presión superior a la que buscamos. Si ha sido
# encontrada, la próxima presión mayor será la que retornará la función. Si no, el
# parámetro found pasa a True

print("\nEjercicio 8:\n")

from math import log10

def SPL_dB(P):
    return 20 * log10(P / 20)

def detect2ndNdB(lst, N):
    found = False
    for sound in lst:
        if SPL_dB(sound) > N:
            if found:
                return sound
            else:
                found = True
    return -1

for sonidos, minimo in [([90,590,750,632, 650, 900, 2000, 789, 545], 30), ([90,590,750,632, 650, 900, 2000, 789, 545], 33), ([90,590,750,632, 630, 600, 200, 589, 545], 30), ([9e3,1e4,1.1e5,2.2e5, 1.3e6, 2.5e6, 3.2e6], 83), ([2000, 2450.5, 2500 , 456.7, 1567.8], 42)]:
    print(f"detect2ndNdB({sonidos}, {minimo}) ==> {detect2ndNdB(sonidos, minimo)}")

# Ejercicio 9: Primos pitagóricos
# Usamos la misma lógica que con el ejercicio anterior, solo que como indicador de si
# ha sido encontrado un número primo utilizaremos la propia lista (una lista vacía en
# python es False al pasarlo a bool). Al iterar por la lista, cuando encontremos un
# número primo, comprobaremos si ya existe un número en nuestra lista resultante. Si
# hay, añadimos el número y devolvemos la lista. Si no, añadimos el número y seguiremos
# iterando.

print("\nEjercicio 9:\n")

def es_primo(n):
    if n <= 1: return False
    for d in range(2, n//2+1):
        if n % d == 0:
            return False
    return True

def primoPitagoric2(lst):
    result = list()
    for number in lst:
        if es_primo(number) and number % 4 == 1:
            if result:
                result.append(number)
                return result
            else:
                result.append(number)
    return -1

for numeros in ([3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], [5, 9, 13, 17, 21, 25, 29, 33, 37, 41], [41, 45, 49, 53, 57, 61, 65, 69, 73, 77, 81], [3, 4, 5, 6, 7, 8, 9, 10], [81, 85, 89, 93, 97, 101, 105, 109, 113, 117, 121]):
    print(f"Dos primeros primos pitagóricos en {numeros}: {primoPitagoric2(numeros)}")

# Ejercicio 10: Contar positivos.
# En esta ocasión haremos una doble iteración, entendiendo que por cada primera iteración
# estaremos iterando por cada línea de la matriz. Cuando encontremos un número positivo,
# simplemente aumentaremos en 1 nuestro contador, que acabará devolviendo nuestra función.

print("\nEjercicio 10:\n")

def contar_pos(matriz):
    count = 0
    for linea in matriz:
        for elemento in linea:
            if elemento > 0:
                count += 1
    return count

matrix = [[1, -2, 3],[-4,5,6],[7,8,-9]]
print(f"La matriz {matrix} tiene {contar_pos(matrix)} números positivos")


# Ejercicio 11: Mayor densidad
# Dentro de la función, crearemos una variable en la que almacenaremos el primer elemento
# de la lista. Luego iteraremos por la lista que se nos de, y compararemos la densidad
# de cada planeta con la del que está en nuestra variable. En el caso de que la densidad
# sea mayor, nuestra variable pasará a tener el planeta con más densidad. Al final,
# nuestra función devolverá esta variable

print("\nEjercicio 11:\n")

def densidad(planeta):
    return planeta[1] / planeta[2]

def mas_denso(planetas):
    if not planetas:
        return list()
    mayor_densidad = planetas[0]
    for planeta in planetas[1:]:
        if densidad(planeta) > densidad(mayor_densidad):
            mayor_densidad = planeta
    return mayor_densidad[0]

planetas = [['Marte', 1, 2], ['Tierra', 2, 3], ['Venus', 1, 3]]
print(f"El planeta más denso de esta lista ({planetas}) es {mas_denso(planetas)}")

# Ejercicio 12: Jugadores de fútbol
# En esta ocasión vamos a olvidarnos de la eficiencia en favor de la claridad y el orden
# en el código. Para que todo sea más entendible, vamos a crear un dicconario para cada
# jugador en el cada dato esté clasificado. Después, vamos a iterar por la lista de
# jugadores, calcular la media de kilómetros de cada uno e incluir su nombre en la lista
# de jugadores que hayan superado los kilómetros medios, en el caso de que su media
# sea satisfactoria. Luego esa lista la devolveremos ordenada.

print("\nEjercicio 12:\n")

def media(l):
    if not l:
        return 0
    return sum(l) / len(l)

def diccionario_del_jugador(jugador):
    ordenado = {"dorsal": jugador[0],
                "nombre": jugador[1],
                "es comunitario": jugador[2],
                "edad": jugador[3],
                "km por partido": jugador[4:]}
    return ordenado

def jugComKm(equipo, min_km):
    dignos = []
    lista_clara = [diccionario_del_jugador(jugador) for jugador in equipo]
    for jugador in lista_clara:
        if media(jugador["km por partido"]) > min_km:
            dignos.append(jugador["nombre"])
    return sorted(dignos)

lst_equipo = [[3, 'Pique', True, 33, 10.2, 9.0], \
              [4, 'Ramos', True, 34, 11.0, 11.1, 9.8, 8.5], \
              [6, 'Koke', True, 27, 7.5, 9.6, 10.3, 6.5, 5.6], \
              [7, 'Joao',  True, 25, 10.5, 8.4, 9.0, 8.6], \
              [8, 'Saul', True, 24, 9.5, 8.9, 10.0, 9.6], \
              [9, 'Suarez', False, 33, 8.6, 7.5], \
              [10, 'Lionel', False, 33, 10.0, 11.1, 9.8, 8.5,10.1], \
              [19, 'Odriozola', True, 25, 9.5], \
              [14, 'Araujo', False, 21, 8.9, 9.5], \
              [15, 'Valverde', False, 22, 9.9, 10.2], \
              [16, 'Pedri', True, 18, 10.5, 11, 9.5, 10.6], \
              [22, 'Hermoso', False, 23, 10, 7.5, 6.6], \
              [23, 'Iago', True, 33, 11.1, 9.0, 9.3, 8.8]]

for kilometros in [10, 10.2, 10.5, 9.5, 9.4]:
    print(f"Estos jugadores tienen más de {kilometros} kilómetros de media: {jugComKm(lst_equipo, kilometros)}")
