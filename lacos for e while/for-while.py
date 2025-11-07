import os


for i in range(5):
    print(f"{i+1} Bem-vindo ao Buscante!")

input('digite enter para seguir')

#fim da 1 atividade


# Atividade 2: Calculando a soma de números
os.system('cls')

resultado = 0
valores = [1, 2, 3, 4, 5]

for valor in valores:
    resultado = valor + resultado    

print(resultado)

input('digite enter para seguir')

#fim da 2 atividade

# Atividade 3: Organizando texto
os.system("cls")

projetos = ["website", "jogo", "análise de dados", None, "aplicativo móvel"]


for projeto in projetos:
    if projeto is None:
        continue
    print(f"{projeto}")

input('digite enter para seguir')


#fim da 3 atividade

# Atividade 4: Entendendo o uso do break

os.system("cls")

livros = ["1984", "Dom Casmurro", "O Pequeno Príncipe", "O Hobbit", "Orgulho e Preconceito"]

for livro in livros:
    if livro == "O Hobbit":
        print(f"Livro encontrado! {livro}")
        break


input('digite enter para seguir')



#fim da 4 atividade

# Atividade 5: Controle de estoque

os.system("cls")
estoque = 5

while estoque > 0:
    estoque -= 1 
    print(f"Venda realizada! Estoque restante: {estoque}")

print("Estoque esgotado")


input('digite enter para seguir')


#fim da ativade 5

## Atividade 6: mostrar apenas o disponivel
os.system('cls')
livros = [
    {"nome": "1984", "estoque": 5},
    {"nome": "Dom Casmurro", "estoque": 0},
    {"nome": "O Pequeno Príncipe", "estoque": 3},
    {"nome": "O Hobbit", "estoque": 0},
    {"nome": "Orgulho e Preconceito", "estoque": 2}
]

for livro in livros:
    if livro['estoque'] > 0:
        print(f'livros disponiveis: {livro["nome"]}')

input('digite enter para seguir')
   
#fim da ativade 6


## Atividade 7: Validação de entrada para login
while True:
    nome_usuario = input("Digite seu nome de usuário: ")
    senha = input("Digite sua senha: ")

    if len(nome_usuario) < 5:
        print("O nome de usuário deve ter pelo menos 5 caracteres.")
        continue

    if len(senha) < 8:
        print("A senha deve ter pelo menos 8 caracteres.")
        continue

    print("Cadastro realizado com sucesso!")
    break
    
#fim da ativade 7


    




   







