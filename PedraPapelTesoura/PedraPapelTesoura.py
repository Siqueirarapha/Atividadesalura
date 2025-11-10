import os
os.system('cls' if os.name == 'nt' else 'clear')
Aleatorio = ["Pedra", "Papel", "Tesoura"]

try:
    from random import choice
    escolhaUsuario = input("Escolha Pedra, Papel ou Tesoura: ")
    print(f"Você escolheu: {escolhaUsuario}")
    escolhaComputador = choice(Aleatorio)
    print(f"Computador escolheu: {escolhaComputador}")
    if escolhaUsuario == escolhaComputador:
        print("Empate!")
    elif (escolhaUsuario == "Pedra" and escolhaComputador == "Tesoura") or \
         (escolhaUsuario == "Papel" and escolhaComputador == "Pedra") or \
         (escolhaUsuario == "Tesoura" and escolhaComputador == "Papel"):
        print("Você ganhou!")
    else:
        print("Computador ganhou!")
except ImportError:
    print("Módulo random não está disponível.")