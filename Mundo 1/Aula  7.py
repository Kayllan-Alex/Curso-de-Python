print("\033[1;31mOlá, Mundo!\033[m")
print("\033[4;30;45mOlá, Mundo!\033[m")
print("\033[7;33;44mOlá, Mundo!\033[m")

primeiro_valor = 5
segundo_valor = 1
print(f"O valor de \033[31m{primeiro_valor}\033[m e \033[34m{segundo_valor}\033[m")

nome = "Kayllan"
cor = {
    "limpa": "\033[m", 
    "azul": "\033[34m", 
    "vermelho": "\033[31m"
}
print(f"Olá! Muito prazer em te conhecer, {cor['azul']}{nome}{cor['limpa']}")