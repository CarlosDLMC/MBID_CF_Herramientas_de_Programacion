import matplotlib.pyplot as plt

# fig, ax = plt.subplots()
# ax.plot(list(range(0, 5, 1)), list(range(5, 0, -1)))
# plt.show()

def ganancia(dias, intervalo):
    staked = 2.9911
    com = 0.0001
    rew = 0.00103
    perc = rew / staked
    total = staked
    for i in range(1, dias):
        total = total + perc * staked
        if not i % intervalo :
            total -= com
            staked = staked + intervalo * perc * staked - com
        # print(f"Día {i} ===> total: {total}, staked: {staked}")
    return total

dias = 300

for descanso in range(1, dias):
    print(f"Si en {dias} dias le metes cada {descanso} días al final tienes {ganancia(dias, descanso)} elrond")
ganancia(dias, 7)

fig, ax = plt.subplots()
ax.plot(list(range(1, dias)), [ganancia(dias, i) for i in range(1, dias)])
plt.show()


# totales = 3000
# for dias in range(2, totales):
#     ganancias = [(ganancia(dias, i), i) for i in range(1, dias)]
#     resultado = max(ganancias, key=lambda x: x[0])
#     print(f"Si lo dejas {dias} dias, lo máximo que puedes conseguir es {resultado[0]} elronds, metiendo el stake cada {resultado[1]} días" )
