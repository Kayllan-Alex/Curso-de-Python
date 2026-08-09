from random import randint

tentativas = 0
tentativa = None 
numero_pensado = randint(1, 10)
while tentativa != numero_pensado:
    tentativa = int(input("Tente adivinhar o número que eu pensei [0 a 10]: "))
    tentativas += 1
print(
    f"Perfeito o número pensado foi {numero_pensado}. E você acertou em {tentativas} tentativa(s)."
)