with open("C://Users//PDBD091//Curso de Python//Módulo 7//7.4 - Arquivos de Texto//meus_livros.csv", "w") as arquivo:
    arquivo.write("Título,Autor,Ano de publicação,Número de páginas\n")
    livros = [
        ("Verity", "Colleen Hoover", 2018, 336),
        ("Divergente", "Veronica Roth", 2011, 487),
        ("Insurgente", "Veronica Roth", 2012, 544),
        ("Convergente", "Veronica Roth", 2013, 526),
        ("Minha Vida Fora de Série 1", "Paula Pimenta", 2011, 408),
        ("Minha Vida Fora de Série 2", "Paula Pimenta", 2013, 424),
        ("Minha Vida Fora de Série 3", "Paula Pimenta", 2015, 424),
        ("Minha Vida Fora de Série 4", "Paula Pimenta", 2017, 406),
        ("Querido John", "Nicholas Sparks", 2006, 288),
        ("A Paciente Silenciosa", "Alex Michaelides", 2019, 336)
    ]

    for livro in livros:
        linha = f"{livro[0]},{livro[1]},{livro[2]},{livro[3]}\n"
        arquivo.write(linha)
