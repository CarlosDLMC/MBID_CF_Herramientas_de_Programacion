#Ejercicio 1: Frecuencia de pares
# Para este ejercicio, iteraremos sobre la función del argumento. Si el elemento es par,
# se busca si existe en el dicconario. En el caso de que exista, el número de veces
# que aparece aumentará en 1. En caso contrario, se creará una entrada en el diccionario
# que se igualará a 1
print("Ejercicio 1:\n")

def dpar(M):
    result = dict()
    for number in M:
        if number % 2 == 0:
            if number in result:
                result[number] += 1
            else:
                result[number] = 1
    return result

M = [12, 19, 19, 18, 18, 16, 18, 13, 19, 18, 12, 18, 11, 20, 14, 14, 20, 20, 20, 16, 13, 15, 19, 14, 12]

print(f"{{Número par: veces que aparece}} (primer método)==> {dpar(M)}")

# Este ejercicio también se puede resolver en una línea con dict comprehension y usando
# el método count(), lo añado aparte porque se me ha ocurrido más tarde

def dpar2(M):
    return {number: M.count(number) for number in M if number % 2 == 0}

print(f"{{Número par: veces que aparece}} (segundo método)==> {dpar2(M)}")

# Ejercicio 2: Temperaturas de ciudades
# Esta vez vamos a volver a usar un dict comprehension para que nos cree un diccionario
# en el que la clave es el nombre de la ciudad, y el valor una lista en el que el primer
# elemento es el máximo de la lista que se nos da (excluyendo el primer elemento), y el
# segundo el mínimo. Para que salgan en orden alfabético, vamos a ordenar la lista dentro
# de la dict comprehension

print("\nEjercicio 2:\n")

def TempMaxMin(lst):
    return {ciudad[0]: [max(ciudad[1:]), min(ciudad[1:])] for ciudad in sorted(lst)}

lst_ciudad = [['Londres', 3.4, 6.3, 10.5, 6.8], ['Oslo', -3.8, -5.0, 5.1, 4.2], ['Berlin', 7.5, 4.1, 12.3, 13.0], ['Málaga', 14.7, 12.3, 19.5, 18.4]]
print(f"{{Ciudad: [temperatura máxima, temperatura mínima]}} ====> {TempMaxMin(lst_ciudad)}")

# Ejercicio 3: Temperaturas nevada
# Volvemos a usar nuestras queridas comprehensions. Aprovechamos que todos los nombres
# que nos hacen falta están en las claves del diccionario de personas, y le aplicamos el
# filtro de que la temperatura de su ciudad tiene que ser menor de 0. Aprovechamos que
# dPers[nombre de la persona] = ciudad y dCiudT[ciudad] = temperatura, lo combinamos y
# tenemos que dCiudT[dPercC[nombre de la persona]] = temperatura

print("\nEjercicio 3:\n")

def PersMayTemp(dPersC, dCiudT):
    return sorted([name for name in dPersC if dCiudT[dPersC[name]] < 0])

dCi = {'Manchester': 1.1, 'Madrid': -8.9, 'Gava': 4, \
               'Pobla de Segur': -5.6, 'Lleida': -3.2, 'Elche': 2.1, \
               'Burgos': -6.0, 'Sant Boi': 4.5}

dPe = {'Pepe': 'Manchester', 'Lionel': 'Gava', 'Mike': 'Sant Boi', \
               'Puyol': 'Pobla de Segur', 'Jaime': 'Elche', 'Sergi': 'Lleida',\
                'Ernesto': 'Madrid', 'Carlos': 'Burgos'}


print(f"Gente que ha pasado la primera semana a bajo cero: {PersMayTemp(dPe, dCi)}")

# Ejercicio 4: Hipertensión
# Volvemos a hacer uso de list comprehension. En este caso aprovechamos que los nombres
# que tenemos que filtrar están en las claves del diccionario, y en las condiciones
# ponemos las condiciones explicadas en el ejercicio, teniendo en cuenta que
# dpers[name][0] = edad, dpers[name][1] = sistólica, dpers[name][2] = diastólica

print("\nEjercicio 4:\n")

dpers = {'Maria': [40, 135, 90],'Nuria': [63, 141, 92], \
                 'Jose': [47, 110, 59], 'Luis': [49, 146, 94], \
                 'Oriol': [52, 130, 89], 'Carlos': [65, 125, 89], \
                 'Pepe': [70, 130, 92] }

def lst_hiper(dicc, edad):
    return sorted([name for name in dpers if (dpers[name][1] >= 140 or dpers[name][2] >= 90) and dpers[name][0] < edad])
edad = 70
print(f"personas de mas de {edad} años con problemas de tensión: {lst_hiper(dpers, edad)}")

# Ejercicio 5: Nivel de potasio en sangre
# Esta vez vamos a iterar sobre cada elemento del diccionario y comparar su resultado
# con cada elemento de la lista. Los resultados los vamos metiendo en un diccionario que
# creamos en nuestra función y que acabamos devolviendo

print("\nEjercicio 5:\n")

def nivelKsang(dK, lst):
    results = dict()
    for name in dK:
        if dK[name] < lst[0]:
            results[name] = 'hipokalemia crítica'
        elif dK[name] < lst[1]:
            results[name] = 'hipokalemia leve'
        elif dK[name] <= lst[2]:
            results[name] = 'normal'
        elif dK[name] <= lst[3]:
            results[name] = 'hiperkalemia moderada'
        else:
            results[name] = 'hiperkalemia severa'
    return results

dK1 = {'Luis': 2.2, 'Carlos': 7.0, 'Laia': 4.0, 'Mikel': 5.5, \
               'Jordi': 5.2, 'Anna': 3.6, 'Joe': 7.2}

ls1 = [2.0, 3.5, 5.2, 7.0]

print(nivelKsang(dK1, ls1))

# Ejercicio 6: Temperatura ciudades en DataFrame
# En este ejercicio vamos a crear las listas aparte para luego meterlas con un diccionario
# en el argumento de nuestro DataFrame. Para calcular la media y la desviación normal,
# usaremos los métodos incluidos en la biblioteca numpy

import pandas as pd
import numpy as np

print("\nEjercicio 6:\n")

ciudades = [['Londres', 3.4, 6.3, 10.5, 6.8], ['Oslo', -3.8, -5.0, 5.1, 4.2], ['Berlin', 7.5, 4.1, 12.3, 13.0], ['Málaga', 14.7, 12.3, 19.5, 18.4]]

def create_simple_dataframe(lista_de_ciudades):
    nombres = [elemento[0] for elemento in lista_de_ciudades]
    enero = [elemento[1] for elemento in lista_de_ciudades]
    febrero = [elemento[2] for elemento in lista_de_ciudades]
    marzo = [elemento[3] for elemento in lista_de_ciudades]
    abril = [elemento[4] for elemento in lista_de_ciudades]

    return pd.DataFrame({"Ciudad": nombres, "Enero": enero, "Febrero": febrero, "Marzo": marzo, "Abril": abril})

print("6a (lista simple):")
print(create_simple_dataframe(ciudades))

def create_complete_dataframe(lista_de_ciudades):
    nombres = [elemento[0] for elemento in lista_de_ciudades]
    enero = [elemento[1] for elemento in lista_de_ciudades]
    febrero = [elemento[2] for elemento in lista_de_ciudades]
    marzo = [elemento[3] for elemento in lista_de_ciudades]
    abril = [elemento[4] for elemento in lista_de_ciudades]
    minimas = [min(elemento[1:]) for elemento in lista_de_ciudades]
    maximas = [max(elemento[1:]) for elemento in lista_de_ciudades]
    media = [np.mean(elemento[1:]) for elemento in lista_de_ciudades]
    desviacion_normal = [np.std(elemento[1:]) for elemento in lista_de_ciudades]
    return pd.DataFrame({"Ciudad": nombres, "Enero": enero, "Febrero": febrero, "Marzo": marzo, "Abril": abril, "Min": minimas, "Max": maximas, "Media": media, "StdDev": desviacion_normal})

print("\n6b (lista más compleja):")
print(create_complete_dataframe(ciudades))

# Ejercicio 7: Base de datos cardíaca
# En este ejercicio simplemente vamos a utilizar métodos de la biblioteca pandas para
# ejecutar todas las acciones requeridas en el enunciado

print("\nEjercicio 7:\n")

try:
    dfCardio = pd.read_csv("heart.csv")

    print("Mostrando las primeras 10 filas:")
    print(dfCardio.head(10))

    cantidad_de_hombres = len(dfCardio[dfCardio["sex"] == 1]) # Filtramos el df para que sólo haya hombres y contamos
    cantidad_de_mujeres = len(dfCardio[dfCardio["sex"] == 0]) # Filtramos el df para que sólo haya mujeres y contamos
    print(f"En este DataFrame hay {cantidad_de_hombres} hombres y {cantidad_de_mujeres} mujeres\n")

    angina = len(dfCardio[dfCardio["exang"] == 1]) #Filtramos el df para que sólo haya casos positivos y contamos
    print(f"Hay {angina} casos de angina de pecho inducida\n")

# Creamos un Dataframe a partir de una columna del que ya tenemos
    dfThalach = pd.DataFrame({"Frecuencia cardíaca": dfCardio["thalach"]})
    print("DataFrame con sólo la frecuencia cardíaca:")
    print(dfThalach)

# Creamos un Dataframe a partir de dos columnas del que ya tenemos
    dfCorazon = pd.DataFrame({"Sistólica": dfCardio["trestbps"], "Colesterol": dfCardio["chol"]})
    print("\nDataFrame con la presión sistólica y el colesterol:")
    print(dfCorazon)
except Exception:
    print("¡No se ha podido encontrar el archivo!\n \
Por favor, asegúrate de que el archivo \"heart.csv\" se encuentra en \n \
la misma carpeta que el archivo \"practica_2.py\"")

# Ejercicio 8: Base de datos presión arterial en DataFrame
# En este ejercicio vamos a hacer listas aparte para cada tipo y luego hacer un dataframe
# con ellas. para poder conseguir un diagnóstico con una list comprehension, creamos la
# función "diagnosticar" que directamente nos devuelva un diagnóstico a partir de la
# presión sistólica y diastólica

print("\nEjercicio 8:\n")

tensiones = {'Maria': [40, 135, 90],'Nuria': [63, 141, 92], \
                 'Jose': [47, 110, 59], 'Luis': [49, 146, 94], \
                 'Oriol': [52, 130, 89], 'Carlos': [65, 125, 89], \
                 'Pepe': [70, 130, 92] }

def diagnosticar(sis, dis):
    if sis >= 140 or dis >= 90:
        return "alta"
    elif sis < 90 or dis < 60:
        return "baja"
    return "normal"

def create_pacients_dataframe(pacientes):
    nombres = [paciente for paciente in pacientes]
    edad = [pacientes[paciente][0] for paciente in pacientes]
    sistolica = [pacientes[paciente][1] for paciente in pacientes]
    diastolica = [pacientes[paciente][2] for paciente in pacientes]
    diagnostico = [diagnosticar(pacientes[paciente][1], pacientes[paciente][2]) for paciente in pacientes]
    return pd.DataFrame({"Nombre": nombres, "Sistólica": sistolica, "Diastólica": diastolica, "Diagnóstico": diagnostico})

print("Pacientes con sus presiones:")
print(create_pacients_dataframe(tensiones))
