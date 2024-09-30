#Escreva um programa em Python que solicita ao usuário para inserir a avaliação de um filme em uma escala de 1 a 5.
nome_filme = input("Nome do filme: ")
avaliacao = int(input("Insira a avaliação do filme (de 1 a 5): "))

if avaliacao == 5:
    print("Excelente!")
elif avaliacao == 4:
    print("Muito Bom!")
elif avaliacao == 3:
    print("Bom!")
elif avaliacao == 2:
    print("Regular.")
elif avaliacao == 1:
    print("Ruim.")
else:
    print("Avaliação inválida. Por favor, insira um valor entre 1 e 5.")
