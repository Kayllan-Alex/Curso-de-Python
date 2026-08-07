peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))
indice_de_massa_corporal = peso / altura**2
if indice_de_massa_corporal < 18.5:
    print(
        f"Você está com o IMC de {indice_de_massa_corporal:.1f}. Portanto está abaixo do peso."
    )
elif indice_de_massa_corporal < 25:
    print(
        f"Você está com o IMC de {indice_de_massa_corporal:.1f}. Está com o peso ideal."
    )
elif indice_de_massa_corporal < 30:
    print(
        f"Você está com o IMC de {indice_de_massa_corporal:.1f}. Portanto está com sobrepeso."
    )
elif indice_de_massa_corporal < 40:
    print(
        f"Você está com o IMC de {indice_de_massa_corporal:.1f}. Tome cuidado, você está na obesidade."
    )
else:
    print(f"Você está com o IMC de {indice_de_massa_corporal:.1f}. Obesidade mórbida.")
