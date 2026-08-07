nome_completo = input("Digite seu nome completo: ")
nome_sem_espacos = nome_completo.replace(" ", "")
primeiro_nome = nome_completo.split()[0]
print(f"O seu nome com as letras maiúsculas fica: {nome_completo.upper()}")
print(f"O seu nome com as letras minúsculas fica: {nome_completo.lower()}")
print(f"O seu nome tem ao todo {len(nome_sem_espacos)} letras")
print(f"E seu primeiro nome tem ao todo {len(primeiro_nome)} letras")