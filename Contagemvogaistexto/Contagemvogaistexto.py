import os
os.system('cls')

texto = str(input("Digite um texto: ")).lower()
vogais = "aeiou"
consoantes = "bcdfghjklmnpqrstvwxyz"
contagem_vogais = 0
contagem_consoantes = 0

for letra in texto:
    if letra in vogais:
        contagem_vogais += 1
    elif letra in consoantes:
        contagem_consoantes += 1
        


print("\nTotal de vogais:", contagem_vogais)
print("\nTotal de consoantes:", contagem_consoantes)


print("\nTotal de caracteres:", len(texto))

input("\nPressione Enter para sair...")

print("Fim do programa.")