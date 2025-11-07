import os
os.system('cls')


def validador(cpf):
       
        if not cpf.isdigit():
            return "Erro: O CPF deve conter apenas números."
        if len(cpf) != 11:
            return "Erro: O CPF deve ter exatamente 11 dígitos."
        
        bloco1 = cpf[:3]
        bloco2 = cpf[3:6]
        bloco3 = cpf[6:9]
        bloco4 = cpf[9:]

        cpfformatado = f'{bloco1}.{bloco2}.{bloco3}-{bloco4}'
        
        return f"CPF válido.: {cpfformatado}"

cpf = input("Digite seu cpf: ")

print(validador(cpf))
    

