# ___________ {}.clear _______________

contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},
}
contatos.clear()
contatos # {}


# ___________ {}.copy _______________

contatos = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}

copia = contatos.copy()
copia["guilherme@gmail.com"] = {"nome": "Gui"}

contatos["guilherme@gmail.com"] # {"nome": "Guilherme", "telefone": "3333-2221"}
copia["guilherme@gmail.com"] # {"nome": "Gui"}


# ___________ {}.fromkeys _______________

dict.fromkeys(["nome", "telefone"]) # {"nome": None, "telefone": None}
dict.fromkeys(["nome", "telefone"], "vazio") # {"nome": "vazio", "telefone":"vazio"}


# ___________ {}.get _______________

contatos = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}

contatos["chave"] # KeyError

contatos.get("chave") # None
contatos.get("chave", {}) # {}
contatos.get("guilherme@gmail.com", {})


# ___________ {}.items _______________

contatos = {"guilherme@gmail.com": {"nome": "Guilherme","telefone": "3333-2221"}}

contatos.items() # dict_items([('guilherme@gmail.com', {'nome': 'Guilherme','telefone': '3333-2221'})])


# ___________ {}.keys _______________

contatos = {"guilherme@gmail.com": {"nome": "Guilherme","telefone": "3333-2221"}}

contatos.keys() # dict_keys(['guilherme@gmail.com'])


# ___________ {}.pop _______________

contatos = {"guilherme@gmail.com": {"nome": "Guilherme","telefone": "3333-2221"}}

contatos.pop("guilherme@gmail.com") # {'nome': 'Guilherme', 'telefone': '3333-2221'}
contatos.pop("guilherme@gmail.com", {}) # {}


# ___________ {}.popitem _______________

contatos = {"guilherme@gmail.com": {"nome": "Guilherme","telefone": "3333-2221"}}

contatos.popitem() # ('guilherme@gmail.com', {'nome': 'Guilherme', 'telefone':'3333-2221'})
contatos.popitem() # KeyError


# ___________ {}.setdefault _______________

contato = {'nome': 'Guilherme', 'telefone': '3333-2221'}

contato.setdefault("nome", "Giovanna") # "Guilherme"
contato # {'nome': 'Guilherme', 'telefone': '3333-2221'}

contato.setdefault("idade", 28) # 28
contato # {'nome': 'Guilherme', 'telefone': '3333-2221', 'idade': 28}


# ___________ {}.update _______________

contatos = {"guilherme@gmail.com": {"nome": "Guilherme","telefone": "3333-2221"}}

contatos.update({"guilherme@gmail.com": {"nome": "Gui"}})
contatos # {'guilherme@gmail.com': {'nome': 'Gui'}}

contatos.update({"giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3322-8181"}})
contatos # {'guilherme@gmail.com': {'nome': 'Gui'}, 'giovanna@gmail.com':{'nome': 'Giovanna', 'telefone': '3322-8181'}}


# ___________ {}.values _______________

contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},
}

contatos.values() # dict_values([{'nome': 'Guilherme', 'telefone': '3333-2221'}, 
                    # {'nome': 'Giovanna', 'telefone': '3443-2121'}, {'nome': 'Chappie','telefone': '3344-9871'}, 
                    # {'nome': 'Melaine', 'telefone': '3333-7766'}])


# ___________ in _______________

contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},
}

"guilherme@gmail.com" in contatos # True
"megui@gmail.com" in contatos # False

"idade" in contatos["guilherme@gmail.com"] # False
"telefone" in contatos["giovanna@gmail.com"] # True


# ___________ del _______________

contatos = {
"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
"giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
"chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
"melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},
}

del contatos["guilherme@gmail.com"]["telefone"]
del contatos["chappie@gmail.com"]

contatos # {'guilherme@gmail.com': {'nome': 'Guilherme'}, 'giovanna@gmail.com':
         # {'nome': 'Giovanna', 'telefone': '3443-2121'}, 'melaine@gmail.com': {'nome':
         # 'Melaine', 'telefone': '3333-7766'}}

