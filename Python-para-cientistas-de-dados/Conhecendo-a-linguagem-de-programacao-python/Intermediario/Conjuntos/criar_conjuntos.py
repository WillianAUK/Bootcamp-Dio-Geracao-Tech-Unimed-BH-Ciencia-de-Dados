# ___________Criando sets____________
#   Um set é uma coleção que não possui objetos repetidos, usamos sets para representar 
# conjuntos matemáticos ou eliminar itens duplicados de um iterável.

set([1, 2, 3, 1, 3, 4]) # {1, 2, 3, 4}
set("abacaxi") # {"b", "a", "c", "x", "i"}
set(("palio", "gol", "celta", "palio")) # {"gol", "celta", "palio"}


# ____________Acessando os dados_______________
#   Conjuntos em Python não suportam indexação e nem fatiamento, caso queira acessar
#  os seus valores é necessário converter o conjunto para lista.

numeros = {1, 2, 3, 2}

numeros = list(numeros)
numeros[0]


# ____________Iterar conjuntos_________________ 
#   A forma mais comum para percorrer os dados de um conjunto é utilizando o comando for.

carros = {"gol", "celta", "palio"}

for carro in carros:
    print(carro)


# ____________Função enumerate________________
#   Às vezes é necessário saber qual o índice do objeto dentro do laço for. 
# Para isso podemos usar a função enumerate.

carros = {"gol", "celta", "palio"}

for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")


