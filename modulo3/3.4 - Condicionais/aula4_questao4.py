#Sistema de entrega expressa e que precisa calcular o valor do frete com base na distância e no peso do pacote.
distancia = float(input("Digite a distância da entrega (em km): "))
peso = float(input("Digite o peso do pacote (em kg): "))

if distancia <= 100:
    valor_frete = 1.00 * peso
elif 101 <= distancia <= 300:
    valor_frete = 1.50 * peso
else:
    valor_frete = 2.00 * peso

if peso > 10:
    valor_frete += 10

print(f"O valor do frete é: R${valor_frete:.2f}")
