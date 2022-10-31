#--------------------------- Variáveis -------------------------------#
#   Em linguagens de programação podemos definir valores que
# podem sofrer alterações no decorrer da execução do
# programa. Esses valores recebem o nome de variáveis, pois
# eles nascem com um valor e não necessariamente devem
# permanecer com o mesmo durante a execução do programa.

age, name = (24, 'Willian')
print(f'\nMeu nome é {name} e eu tenho {age} anos de idade.')


#   Não é preciso definir o tipo de dados da variável, 
# o Python faz isso automaticamente. Por issonão é criada 
# uma variável sem atribuir um valor. Para alterar o valor
# da variável basta fazer uma atribuição de um novo valor:

age = 27
name = 'Marcelo'
print(f'\nMeu nome é {name} e eu tenho {age} anos de idade.')


#--------------------------- Constantes -------------------------------#
#   Assim como as variáveis, constantes são utilizadas para armazenar 
# valores. Uma constante nasce com um valor e permanece com ele até o 
# final da execução do programa, ou seja, o valor é imutável.

#   Não existe uma palavra reservada para informar ao interpretador que 
# o valor é constante. Em algumas linguagens por exemplo: Java e C 
# utilizamos final e const, respectivamente para declarar uma constante.

#   Em Python usamos a convenção que diz ao programador que a variável é 
# uma constante. Para fazer isso, você deve criar a variável com o nome 
# todo em letras maíusculas:

ABS_PATH = '/home/willian/Documents/Bootcamp-Dio-Geracao-Tech-Unimed-BH-Ciencia-de-Dados/'
DEBUG = True
STATES = ['PR', 'MT', 'PB']
AMOUNT = 28.4


# -------------- Boa Praticas --------------

# ● O padrão de nomes deve ser snake case.
# ● Escolher nomes sugestivos.
# ● Nome de constantestodo em maiúsculo.