import os
os.system('cls')


#João trabalha como garçom em um restaurante e precisa calcular a gorjeta que os clientes deixam ao pagar a conta. 
# O restaurante sugere uma gorjeta de 10%, mas alguns clientes podem escolher dar mais ou menos.
# Para agilizar o processo, João quer um programa que receba o valor total da conta e a porcentagem de gorjeta desejada 
# e exiba o valor final que o cliente deverá pagar.Crie um programa que peça ao usuário o valor da conta e a porcentagem 
# de gorjeta. O programa deve calcular e exibir o valor da gorjeta e o total a ser pago.


def menu():
    while True:
        try:
            ValorConta = float(input("Digite o valor da conta: R$ "))
            PorcentagemGorgeta = int(input('Digite a porcentagem de gorjeta: '))

            Gorgeta = ValorConta * (PorcentagemGorgeta / 100)
            ValorTotal = ValorConta + Gorgeta
            os.system('cls')
            print(f'\nValor da gorjeta: R$ {Gorgeta:.2f}')
            print(f'\nValor total a pagar: R$ {ValorTotal:.2f}\n')
            break 

        except ValueError:
            print("Erro: digite apenas números válidos.\nTente novamente.\n")


menu()


