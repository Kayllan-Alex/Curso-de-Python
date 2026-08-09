valor_a_ser_sacado = int(input("Digite quanto deseja sacar: "))
total = valor_a_ser_sacado
cedula = 50
total_de_cedulas = 0
while True:
    if total >= cedula:
        total -= cedula
        total_de_cedulas += 1
    else:
        print(f"Total de {total_de_cedulas} cédulas de R${cedula}")
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 5
        elif cedula == 5:
            cedula = 1
        elif cedula == 1:
            break
        total_de_cedulas = 0
        if total == 0:
            break