import random
import os
os.system('cls')

def grupoobrigatorio():
    vogaisminuscula = 'aeiou'
    consoantesminuscula = 'bcdfghjklmnpqrstvwxyz'
    caracteres_especiais = '!@#$%¨&*()_+-=[]{};:,.<>?/|'
    numeros = '0123456789'
    consoantes_maiusculas = consoantesminuscula.upper()
    vogais_maiusculas = vogaisminuscula.upper()
    return vogaisminuscula, consoantesminuscula, caracteres_especiais, numeros, consoantes_maiusculas, vogais_maiusculas


gerador_senha = grupoobrigatorio()

def minimo_de_caracteres():
    duas_vogais = random.choices(gerador_senha[0], k=2)
    duas_consoantes = random.choices(gerador_senha[1], k=2)
    duas_caracteres_especiais = random.choices(gerador_senha[2], k=3)
    duas_numeros = random.choices(gerador_senha[3], k=3)
    duas_consoantes_maiusculas = random.choices(gerador_senha[4], k=2)
    duas_vogais_maiusculas = random.choices(gerador_senha[5], k=2)

    senha_lista = (
        duas_vogais
        + duas_consoantes
        + duas_caracteres_especiais
        + duas_numeros
        + duas_consoantes_maiusculas
        + duas_vogais_maiusculas
    )
    
    random.shuffle(senha_lista)
    
    return ''.join(senha_lista)

senha12caracteres = minimo_de_caracteres()

print(f'Senha gerada: {senha12caracteres}')

input("\nPressione Enter para sair...")
os.system('cls')