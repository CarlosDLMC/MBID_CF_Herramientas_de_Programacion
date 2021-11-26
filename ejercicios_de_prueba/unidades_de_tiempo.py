segundos = int(input('Di los segundos que quieres: '))
if segundos >= 60:
    minutos = segundos // 60
    segundos = segundos % 60
else:
    minutos = 0
if minutos >= 60:
    horas = minutos // 60
    minutos = minutos % 60
else:
    horas = 0
print(f"Hay {horas} horas {minutos} minutos y {segundos} segundos")
