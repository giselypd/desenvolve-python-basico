#Desenvolvendo um programa para verificar se um ano é bissexto.
ano = int(input("Insira um ano: "))

if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print("Bissexto")
else:
    print("Não Bissexto")
