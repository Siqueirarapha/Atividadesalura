import os

# Lista inicial
lista = [
    {'nome': 'Raphael', 'idade': 19, 'cidade': 'São Paulo', 'status': 'Ativo'},
    {'nome': 'Maria', 'idade': 22, 'cidade': 'Rio de Janeiro', 'status': 'Inativo'},
    {'nome': 'Joao', 'idade': 25, 'cidade': 'Belo Horizonte', 'status': 'Ativo'},
    {'nome': 'Ana', 'idade': 30, 'cidade': 'Curitiba', 'status': 'Ativo'},
    {'nome': 'Pedro', 'idade': 28, 'cidade': 'Salvador', 'status': 'Inativo'}
]

os.system('cls')

# --- Mostrar lista inicial ---
print("Lista de pessoas:")
print(f"{'Nome':<15} {'Idade':<6} {'Cidade':<20} {'Status':<10}")
print("-" * 55)
for pessoa in lista:
    print(f"{pessoa['nome']:<15} {pessoa['idade']:<6} {pessoa['cidade']:<20} {pessoa['status']:<10}")

# --- Adicionar nova pessoa ---
print("\n--- Adicionar nova pessoa ---")
nomelista = input("Digite um nome: ")
idadelista = int(input("Digite uma idade: "))
cidadelista = input("Digite uma cidade: ")
statuslista = input("Digite um status: ")

novapessoa = {
    'nome': nomelista,
    'idade': idadelista,
    'cidade': cidadelista,
    'status': statuslista
}
lista.append(novapessoa)

os.system('cls')
print("✅ Pessoa adicionada com sucesso!\n")
print(f"{'Nome':<15} {'Idade':<6} {'Cidade':<20} {'Status':<10}")
print("-" * 55)
for pessoa in lista:
    print(f"{pessoa['nome']:<15} {pessoa['idade']:<6} {pessoa['cidade']:<20} {pessoa['status']:<10}")

input("\nAperte Enter para continuar...")
os.system('cls')

# --- Editar pessoa ---
print("--- Editar pessoa ---")
nome_pessoa_editar = input("Digite o nome da pessoa que deseja editar: ")

pessoa_encontrada = None
for pessoa in lista:
    if pessoa['nome'].lower() == nome_pessoa_editar.lower():
        pessoa_encontrada = pessoa
        break

if pessoa_encontrada:
    print("\nPessoa encontrada:")
    print(pessoa_encontrada)

    print("\nO que deseja editar?")
    print("1 - Nome")
    print("2 - Idade")
    print("3 - Cidade")
    print("4 - Status")
    opcao_editar = int(input("Digite o número da opção: "))

    if opcao_editar == 1:
        pessoa_encontrada['nome'] = input("Novo nome: ")
    elif opcao_editar == 2:
        pessoa_encontrada['idade'] = int(input("Nova idade: "))
    elif opcao_editar == 3:
        pessoa_encontrada['cidade'] = input("Nova cidade: ")
    elif opcao_editar == 4:
        pessoa_encontrada['status'] = input("Novo status: ")
    else:
        print("Opção inválida.")

    print("\n✅ Pessoa atualizada com sucesso!\n")
else:
    print("Pessoa não encontrada.")

print(f"{'Nome':<15} {'Idade':<6} {'Cidade':<20} {'Status':<10}")
print("-" * 55)
for pessoa in lista:
    print(f"{pessoa['nome']:<15} {pessoa['idade']:<6} {pessoa['cidade']:<20} {pessoa['status']:<10}")

input("\nAperte Enter para continuar...")
os.system('cls')

# --- Remover pessoa ---
print("--- Remover pessoa ---")
nome_remover = input("Digite o nome da pessoa que deseja remover: ")

removida = False
for pessoa in lista:
    if pessoa['nome'].lower() == nome_remover.lower():
        lista.remove(pessoa)
        removida = True
        print(f"\n✅ {nome_remover} foi removido da lista.")
        break

if not removida:
    print("Pessoa não encontrada na lista.")

print("\nLista atualizada:\n")
for pessoa in lista:
    print(pessoa['nome'], pessoa['idade'], pessoa['cidade'], pessoa['status'])





