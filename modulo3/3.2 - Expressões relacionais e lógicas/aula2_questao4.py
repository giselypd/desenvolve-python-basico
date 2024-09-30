#Escreva um script que solicita a classe de personagem escolhida (guerreiro, mago ou arqueiro), os pontos de força e os pontos de magia atribuídos ao personagem. O programa deve imprimir True se os pontos de atributo são consistentes com a classe escolhida
classe = input("Escolha a classe (guerreiro, mago ou arqueiro): ")
forca = int(input("Digite os pontos de força (de 1 a 20): "))
magia = int(input("Digite os pontos de magia (de 1 a 20): "))

if classe == "guerreiro":
    apto = (forca >= 15) and (magia <= 10)
elif classe == "mago":
    apto = (forca <= 10) and (magia >= 15)
elif classe == "arqueiro":
    apto = (5 < forca <= 15) and (5 < magia <= 15)
else:
    apto = False

print("Pontos de atributo consistentes com a classe escolhida:", apto)