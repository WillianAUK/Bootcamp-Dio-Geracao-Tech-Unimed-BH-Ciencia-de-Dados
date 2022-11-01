# __________[].append____________

lista = []
lista.append(1)
lista.append("Python")
lista.append([40, 30, 20])
print(lista) # [1, "Python", [40, 30, 20]]


# __________[].clear____________

lista = [1, "Python", [40, 30, 20]]
print(lista) # [1, "Python", [40, 30, 20]]
lista.clear()
print(lista) # []


# __________[].copy____________

lista = [1, "Python", [40, 30, 20]]
lista.copy()
print(lista) # [1, "Python", [40, 30, 20]]


# __________[].count____________

cores = ["vermelho", "azul", "verde", "azul"]
cores.count("vermelho") # 1
cores.count("azul") # 2
cores.count("verde") # 1


# __________[].extend____________

linguagens = ["python", "js", "c"]
print(linguagens) # ["python", "js", "c"]
linguagens.extend(["java", "csharp"])
print(linguagens) # ["python", "js", "c", "java", "csharp"]


# __________[].index____________

linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.index("java") # 3
linguagens.index("python") # 0


# __________[].pop____________

linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.pop() # csharp
linguagens.pop() # java
linguagens.pop() # c
linguagens.pop(0) # python


# __________[].remove____________

linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.remove("c")
print(linguagens) # ["python", "js", "java", "csharp"]


# __________[].reverse____________

linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.reverse()
print(linguagens) # ["csharp", "java", "c", "js", "python"]


# __________[].sort____________

linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort() # ["c", "csharp", "java", "js", "python"]

linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(reverse=True) # ["python", "js", "java", "csharp", "c"]

linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(key=lambda x: len(x)) # ["c", "js", "java", "python", "csharp"]

linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(key=lambda x: len(x), reverse=True) # ["python", "csharp", "java", "js", "c"]


# __________len____________

linguagens = ["python", "js", "c", "java", "csharp"]
len(linguagens) # 5


# __________sorted____________

linguagens = ["python", "js", "c", "java", "csharp"]
sorted(linguagens, key=lambda x: len(x)) # ["c", "js", "java", "python", "csharp"]
sorted(linguagens, key=lambda x: len(x), reverse=True) # ["python", "csharp", "java", "js", "c"]