cpf = (input('Digite seu CPF: ')).strip()  # recebe o CPF digitado
i = 1  # contador das multiplicações
soma = 0  # armazena a soma total
num = list(map(int, cpf))  # transforma o CPF em lista de números
valid = num[0:9]  # separa os números para validar o 1º dígito

# cálculo do primeiro dígito
for j in valid:
    mult = j * i
    i += 1
    soma += mult

# verifica se o primeiro dígito está correto
if soma % 11 == 10 and num[9] == 0:
    print('Primeiro dígito válido!!')

elif soma % 11 == num[9]:
    print('Primeiro dígito válido!!')

else:
    print('Primeiro dígito inválido!!')


valid = num[1:10]  # separa os números para validar o 2º dígito
soma = 0  # reinicia a soma
i = 1  # reinicia o contador

# cálculo do segundo dígito
for j in valid:
    mult = j * i
    i += 1
    soma += mult

# verifica se o segundo dígito está correto
if soma % 11 == 10 and num[10] == 0:
    print('Segundo dígito válido!!')

elif soma % 11 == num[10]:
    print('Segundo dígito válido!!')

else:
    print('Segundo dígito inválido!!')