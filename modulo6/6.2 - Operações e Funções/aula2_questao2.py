import random

elementos = []
num_elementos = random.randint(5, 20)
for i in range(num_elementos):
    elementos.append (random.randint(1, 10))

soma_elementos = sum(elementos)
media_elementos = soma_elementos / num_elementos

print("Lista de elementos:", elementos)
print("Soma dos valores:", soma_elementos)
print("Média dos valores:", media_elementos)
