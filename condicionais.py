import os

def aperte_enter():
    input("\nAperte Enter para continuar...")
    os.system('cls')

# Atividade 1: Comparar idades

os.system('cls')
joao = int(input("Digite a idade do João: "))
maria = int(input("Digite a idade da Maria: "))

numeros = [joao, maria]

print(max(numeros), "é a maior idade." )

if joao > maria:
    print("João é mais velho que Maria.")
elif joao == maria:
    print("João e Maria têm a mesma idade.")
else:
    print("Maria é mais velha que João.")

aperte_enter()

#final da primeira atividade





# Atividade 2: Calculando o tempo total de projeto

while True:
    os.system('cls')
    print("=== Cálculo do Tempo Total de Projeto ===")
    A = int(input("Digite o tempo estimado para a tarefa A (em horas): "))
    B = int(input("Digite o tempo estimado para a tarefa B (em horas): "))
    C = int(input("Digite o tempo estimado para a tarefa C (em horas): "))
    numeros = [A, B, C]
    print(numeros)
    input('aperte enter para ver o resultado')
    os.system('cls')

    if A > 0 and B > 0 and C > 0:
        resultado = A + B + C
        print(f"O tempo total estimado para o projeto é de {resultado} horas.")
    else:
        print("Por favor, insira apenas valores positivos.")
        aperte_enter()
    break   

#final da segunda atividade







# Atividade 3: Calculando o IMC  formula: IMC = peso / (altura * altura)
os.system('cls')
print("=== Cálculo do IMC ===")
peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura em metros: observe usar ponto ao invés de vírgula: "))

imc = peso / (altura * altura)
print(f"Seu IMC é: {imc:.2f}")

if imc < 18.5:
    print("Você está abaixo do peso.")
elif 18.5 <= imc < 24.9:
    print("Você está com o peso normal.")
elif 25 <= imc < 29.9:
    print("Você está com sobrepeso.")
elif 30 <= imc < 34.9:
    print("Você está com obesidade grau 1.")
elif 35 <= imc < 39.9:
    print("Você está com obesidade grau 2.")
else:
    print("Você está com obesidade grau 3.")

aperte_enter()
#final da terceira atividade







# Atividade 4: Verificando a paridade de um número formula num % 2 == 0
os.system('cls')

print("=== Verificação de Paridade ===")
numero = int(input("Digite um número inteiro: "))
resultado = numero % 2
if resultado == 0:
    print(f"O número {numero} é par.")
else:
    print(f"O número {numero} é ímpar.")

#final da quarta atividade







# Atividade 5: Aprovando empréstimo formula salario * 0.3 >= valor_parcela

os.system('cls')
print("=== Simulação de Empréstimo ===")
salario = int(input("Digite seu salário mensal: "))
resultado = salario * 0.3
print(f"30% do seu salário é: {resultado}")
valor_parcela = int(input("Digite o valor da parcela do empréstimo: "))


if resultado >= valor_parcela:
    print("Empréstimo aprovado!")
else:
    print("Empréstimo negado.")

#final da quinta atividade





       



