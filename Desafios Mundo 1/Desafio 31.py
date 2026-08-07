distancia_em_km = float(input("Digite a distância de sua viagem em km: "))
if distancia_em_km < 200:
    preco_da_viagem = distancia_em_km * 0.5
else:
    preco_da_viagem = distancia_em_km * 0.45
print(f"A sua viagem de {distancia_em_km}km vai custar R${preco_da_viagem:.1f}")

# print(
#     f"A sua viagem de {distancia_em_km}km vai custar R${distancia_em_km * 0.5:.1f}"
#     if distancia_em_km < 200
#     else f"A sua viagem de {distancia_em_km}km vai custar R${distancia_em_km * 0.45:.1f}"
#  )  Simplifado!