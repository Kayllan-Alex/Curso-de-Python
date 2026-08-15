from desafio112_modulo.utilidadesCeV import moeda
from desafio112_modulo.utilidadesCeV import dado

preco = dado.leiaDinheiro('Informe um preço: R$')

moeda.resumo(preco, 65, 25)