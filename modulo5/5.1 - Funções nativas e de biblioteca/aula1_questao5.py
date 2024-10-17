import emoji

print("Emojis disponíveis:")
print("🌟 - :star:")
print("😄 - :smile:")
print("🎉 - :tada:")
print("🐶 - :dog:")

frase = input("Digite uma frase e ela será emojizada:\n")
frase_emojizada = emoji.emojize(frase)

print("Frase emojizada:")
print(frase_emojizada)
