import os

def continuar():
    input('aperte enter para continuar')
    os.system('cls')

# atividade 1 :Julia é professora e precisa de um programa para ajudar seus alunos a calcularem suas idades 
# com base no ano de nascimento. Sua tarefa é criar uma função que receba o ano de nascimento e o ano atual 
# e retorne à idade correspondente.
os.system('cls')

def calulador_idade(DataNascimento, DataAtual):
    return DataAtual - DataNascimento


AnoNascimento = int(input('digite ano que voce nasceu: '))
AnoAtual = int(input('digite ano atual: '))

idade = calulador_idade(AnoNascimento, AnoAtual )

print(f'Voce tem {idade} anos')

continuar()

#fim da atividade 1

# atividade 2 :Sara está participando de um concurso de escrita, e uma das regras exige que cada palavra de seu texto 
# tenha um limite máximo de caracteres.
# Ajude Sara criando uma função que receba uma palavra e exiba a quantidade de caracteres.

def NomePessoa(Nome):
    return (f'Seu nome e : {Nome} e tem {len(Nome)} carateres')

MeuNome = str(input('digite seu nome: '))

Resultado = NomePessoa(MeuNome)

print(Resultado)

continuar()

#fim da atividade 2

# atividade 3 : Beatriz está desenvolvendo um sistema de atendimento para um site de serviços. Ela deseja criar um programa que exiba uma saudação
#  personalizada dependendo da hora do dia que o usuário acessa a plataforma. O sistema deverá ter a seguinte regra:
# Se for antes das 12h, exibir "Bom dia";

# Entre 12h e 18h, exibir "Boa tarde";

# Após 18h, exibir "Boa noite".


def saudacao (HoraDia):
    if HoraDia < 12:
        return "Bom dia"
    elif HoraDia == 12 and HoraDia < 18:
        return "Boa tarde"
    elif HoraDia > 18:
        return "Boa noite"
    
HoraDia = int(input('digite a hora do dia(0-23): '))

HoraAtual = saudacao(HoraDia)

print(HoraAtual)

#fim da atividade 3

#atividade 4: Pedro está criando um sistema de cadastro de produtos para sua loja e percebeu que todos os números de telefone dos clientes estão
#  armazenados como strings. No entanto, para facilitar buscas e validações, ele precisa que esses números sejam tratados como inteiros.
# Dado o seguinte código com uma lista de números de telefone armazenados incorretamente como str, faça duas funções, uma que converte
# os tipos para inteiro e outra que verifica se a conversão foi feita corretamente e todos os números de telefone são inteiros:



def converter_telefones(lista):  

   return [int(telefone) for telefone in lista] 

def verifica_tipos(lista):  

   for num in lista:  

       if not isinstance(num, int):  

           return "Erro na conversão."  

   return "Todos os números foram convertidos corretamente!" 

telefones = ["11987654321", "21912345678", "31987654321", "11911223344"] 

telefones_convertidos = converter_telefones(telefones) 

print(verifica_tipos(telefones_convertidos)) 

