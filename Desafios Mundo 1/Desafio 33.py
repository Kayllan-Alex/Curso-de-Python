primeiro_numero = int(input("Digite um número: "))
segundo_numero = int(input("Digite um segundo número: "))
terceiro_numero = int(input("Digite um terceiro número: "))
maior = primeiro_numero
menor = primeiro_numero
if segundo_numero > maior:
    maior = segundo_numero
if terceiro_numero > maior:
    maior = terceiro_numero
if segundo_numero < menor:
    menor = segundo_numero
if terceiro_numero < menor:
    menor = terceiro_numero
print(f"{maior} é o maior número.")
print(f"{menor} é o menor número.")