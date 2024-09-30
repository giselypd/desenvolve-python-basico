#Maria precisa de sua ajuda para organizar os experimentos de seu laboratório.
n = int(input("Digite a quantidade de experimentos registrados: "))
cont = 0

total_cobaias = 0
total_sapos = 0
total_ratos = 0
total_coelhos = 0

while cont < n:
    quantia = int(input("Digite a quantidade de cobaias utilizadas: "))
    tipo = input("Digite o tipo de cobaia (S para sapos, R para ratos, C para coelhos): ")

    if tipo == 'S':
        total_sapos += quantia
    elif tipo == 'R':
        total_ratos += quantia
    elif tipo == 'C':  
        total_coelhos += quantia

    total_cobaias += quantia
    cont += 1  

percentual_sapos = (total_sapos / total_cobaias) * 100
percentual_ratos = (total_ratos / total_cobaias) * 100
percentual_coelhos = (total_coelhos / total_cobaias) * 100

print(f"Total: {total_cobaias} cobaias")
print(f"Total de coelhos: {total_coelhos}")
print(f"Total de ratos: {total_ratos}")
print(f"Total de sapos: {total_sapos}")
print(f"Percentual de coelhos: {percentual_coelhos:.2f}%")
print(f"Percentual de ratos: {percentual_ratos:.2f}%")
print(f"Percentual de sapos: {percentual_sapos:.2f}%")
