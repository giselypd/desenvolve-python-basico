import random
n = random.randint(1, 10)

while True:
    valor = int(input("Adivinhe o valor entre 1 e 10: ")) 
    if valor == n:
        print("Correto! O número é",n )
        break
    elif valor > n:
        print("Muito alto, tente novamente!")
    else:
        print("Muito baixo, tente novamente!")
            