# ___________Função input_______________

#   A função builtin input é utilizada quando queremos ler dados da entrada
# padrão (teclado). Ela recebe um argumento do tipo string, que é exibido 
# para o usuário na saída padrão (tela). A função lê a entrada, converte 
# para string e retorna o valor.

from telnetlib import WILL


nome = input("Informe o seu nome: ")
sobrenome = input("Informe o seu sobrenome: ")
idade = int(input("Informe sua idade: "))



# ___________Função print_______________

#   A função builtin print é utilizada quando queremos exibir dados na saída 
# padrão (tela). Ela recebe um argumento obrigatório do tipo varargs de objetos 
# e 4 argumentos opcionais (sep, end, file e flush). Todos os objetos são 
# convertidos para string, separados por sep e terminados por end. A string 
# final é exibida para o usuário.


print(nome, sobrenome, idade)
print(nome, sobrenome, idade, end="...\n")
print(nome, sobrenome, idade, sep="#")