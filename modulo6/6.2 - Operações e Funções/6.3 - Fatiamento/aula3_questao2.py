urls = ["www.google.com", "www.gmail.com", "www.github.com", "www.reddit.com", "www.yahoo.com"]
dominios = []
for url in urls:
    dominios.append(url[4:-4])
    
print(dominios)
