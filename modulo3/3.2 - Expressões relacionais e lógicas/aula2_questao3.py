# Escreva um programa em Python que pergunte ao usuário sua idade, se já jogou pelo menos 3 jogos de tabuleiro (resposta deve ser True ou False) e quantas vezes venceu um jogo.
idade = int(input("Digite sua idade: "))
jogos_jogados = input("Já jogou pelo menos 3 jogos de tabuleiro? (True/False): ")
jogos_vencidos = int(input("Quantos jogos já venceu? "))

jogos_jogados = jogos_jogados.lower() == 'true'
apto = (16 <= idade <= 18) and jogos_jogados and (jogos_vencidos >= 1)
print(f"Apto para ingressar no clube de jogos de tabuleiro: {apto}")
