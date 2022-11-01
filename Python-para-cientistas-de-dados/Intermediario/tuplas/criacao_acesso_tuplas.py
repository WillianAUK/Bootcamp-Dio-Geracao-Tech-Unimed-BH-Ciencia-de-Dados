# ____________Criando tuplas_______________
#   Tuplas são estruturas de dados muito parecidas com as listas, a principal diferença é que 
# tuplas são imutáveis enquanto listas são mutáveis. Podemos criar tuplas através da classe tuple, 
# ou colocando valores separados por vírgula de parenteses.

frutas = ("laranja", "pera", "uva",)
letras = tuple("python")
numeros = tuple([1, 2, 3, 4])
pais = ("Brasil",)


#______________Acesso direto_______________
#   A tupla é uma sequência, portanto podemos acessar seus dados utilizando índices. Contamos o 
# índice de determinada sequência a partir do zero.

frutas = ("maçã", "laranja", "uva", "pera",)
frutas[0] # maçã
frutas[2] # uva


# ____________Índices negativos______________
#   Sequências suportam indexação negativa. A contagem começa em -1.

frutas = ("maçã", "laranja", "uva", "pera",)
frutas[-1] # pera
frutas[-3] # laranja


# __________Tuplas aninhadas________________
#   Tuplas podem armazenar todos os tipos de objetos Python, portanto podemos ter tuplas que 
# armazenam outras tuplas. Com isso podemos criar estruturas bidimensionais (tabelas), e 
# acessar informando os índices de linha e coluna.

matriz = (
    (1, "a",2),
    ("b",3,4),
    (6,5, "c"),
)

matriz[0] # (1, "a", 2)
matriz[0][0] # 1
matriz[0][-1] # 2
matriz[-1][-1] # "c"


# __________Fatiamento______________
#   Além de acessar elementos diretamente, podemos extrair um conjunto de valores de uma 
# sequência. Para isso basta passar o índice inicial e/ou final para acessar o conjunto.
# Podemos ainda informar quantas posições o cursor deve "pular" no acesso.

tupla = ("p", "y", "t", "h", "o", "n",)

tupla[2:] # ("t", "h", "o", "n")
tupla[:2] # ("p", "y")
tupla[1:3] # ("y", "t")
tupla[0:3:2] # ("p", "t")
tupla[::] # ("p", "y", "t", "h", "o", "n")
tupla[::-1] # ("n", "o", "h", "t", "y", "p")


# __________Iterar tuplas__________________
#   A forma mais comum para percorrer os dados de uma tupla é utilizando o comando for.

carros = ("gol", "celta", "palio",)

for carro in carros:
    print(carro)


# ___________Função enumerate________________
#   Às vezes é necessário saber qual o índice do objeto dentro do laço for. Para isso
# podemos usar a função enumerate.

carros = ("gol", "celta", "palio",)

for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")






