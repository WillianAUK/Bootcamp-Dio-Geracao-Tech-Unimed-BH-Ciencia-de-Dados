# ________________Convertendo tipos_____________________
#   Em alguns momentos é necessário será necessário converter o tipo de uma
# variável para manipular de forma diferente. 
#   Por exemplo: Variáveis do tipo string, que armazenam números e precisamos 
# fazer alguma operação matemática com esse valor.

# Inteiro para float
preco = 22
print(preco)
preco = float(preco)
print(preco)
preco = 22 / 2
print(preco,'\n')

# Float para inteiro
preco = 17.22
print(preco)
preco = int(preco)
print(preco,'\n')

# Conversão por divisão
preco = 22
print(preco)
print(preco / 2)
print(preco // 2,'\n')

# Numérico para string
preco = 17.22
idade = 13
print(str(preco))
print(str(idade))

texto = f"idade {idade} preco {preco}"
print(texto,'\n')

# String para número
preco = "17.22"
idade = "13"
print(float(preco))
print(int(idade),'\n')

# Erro de conversão
preco = "python"
print(float(preco))