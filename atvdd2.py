lista = ["arroz", "feijão", "leite", "pão", "ovos", "frutas", "açúcar", "sal", "óleo", "macarrão"]
lista[5] = ["maçã", "banana", "laranja", "uva", "melancia"]
lista[0] = "arroz integral"
lista[1] = "feijão preto"
del lista[2]
del lista[3]
del lista[4]
lista += ["café", "chá", "manteiga", "queijo"]
print("3º elemento:", lista[2])
print("5º elemento:", lista[4])
print("Total de itens:", len(lista))
print("Lista final:", lista)
