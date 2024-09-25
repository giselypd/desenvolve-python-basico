#ler as dimensões de um terreno em inteiros (comprimento e largura), bem como o preço do metro quadrado da região em ponto flutuante. Calcule o valor do terreno e imprima o resultado
comprimento = int(input("Comprimento do terreno: "))
largura = int(input("Largura do terreno: "))
preco_m2 = float(input("Preço do metro quadrado: "))

area_m2 = comprimento * largura
preco_total = preco_m2 * area_m2

print(f"O terreno possui {area_m2}m² e custa R${preco_total:,.2f}")
