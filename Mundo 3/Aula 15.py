pessoas = {
    'nome' : 'Kayllan',
    'sexo' : 'M',
    'idade' : 17
}

print(f"O {pessoas['nome']} tem {pessoas['idade']} anos de idade")
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())

del pessoas['sexo']
pessoas['nome'] = 'Breno'
pessoas['peso'] = 79.8
for k, v in pessoas.items():
    print(f"{k} = {v}")

brasil = []
estado = {
    'uf' : 'Ceará',
    'sigla' : 'CE'
}
brasil.append(estado)
print(brasil)

estado = {}
brasil = []
for c in range(3):
    estado['uf'] = input("Unidade federativa: ")
    estado['sigla'] = input("Sigla do estado: ")
    brasil.append(estado.copy())
for estado in brasil:
    for k, v in estado.items():
        print(f"O campo {k} tem valor {v}")