#Escreva um programa em Python que solicite do usuário o nome, o preço unitário e a quantidade de 3 produtos comprados e imprima ao final o preço total da compra
produto1 = input("Digite o nome do produto 1: ")
preco_p1 = float(input("Digite o preço unitário do produto 1: R$"))
quant_p1 = int(input("Digite a quantidade do produto 1: "))
total_p1 = quant_p1 * preco_p1 

produto2 = input("Digite o nome do produto 2: ")
preco_p2 = float(input("Digite o preço unitário do produto 2: R$"))
quant_p2 = int(input("Digite a quantidade do produto 2: "))
total_p2 = quant_p2 * preco_p2

produto3 = input("Digite o nome do produto 3: ")
preco_p3 = float(input("Digite o preço unitário do produto 3: R$"))
quant_p3 = int(input("Digite a quantidade do produto 3: "))
total_p3 = quant_p3 * preco_p3

total = total_p1 + total_p2 + total_p3

print(f"Total: R${total:,.2f}")
