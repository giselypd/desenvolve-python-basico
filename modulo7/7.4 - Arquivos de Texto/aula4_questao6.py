import csv

musicas_por_ano = {}

with open('C://Users//PDBD091//Curso de Python//Módulo 7//7.4 - Arquivos de Texto//spotify-2023.csv', encoding='latin-1') as arquivo:
    leitor_csv = csv.reader(arquivo)
    next(leitor_csv)
    
    for linha in leitor_csv:
        if len(linha) >= 10:
            track_name = linha[0]
            artist_name = linha[1]
            artist_count = linha[2]
            released_year = linha[3]
            streams = linha[8]

            if int(artist_count) > 1 or '"' in track_name:
                continue
            
            if released_year.isdigit() and streams.isdigit():
                released_year = int(released_year)
                streams = int(streams)

                if 2012 <= released_year <= 2022:
                    if released_year not in musicas_por_ano:
                        musicas_por_ano[released_year] = (track_name, artist_name, streams)
                    else:
                        if streams > musicas_por_ano[released_year][2]:
                            musicas_por_ano[released_year] = (track_name, artist_name, streams)

resultado = []
for ano in range(2012, 2023):
    if ano in musicas_por_ano:
        track_name, artist_name, streams = musicas_por_ano[ano]
        resultado.append([track_name, artist_name, ano, streams])

print(resultado)