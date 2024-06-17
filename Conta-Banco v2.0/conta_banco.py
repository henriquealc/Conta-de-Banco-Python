import textwrap

# Função para exibor o menu e obter a escolha do usuário
def menu():
    menu_text = '''
    ========== MENU ==========
    [1]\tDepositar
    [2]\tSacar
    [3]\tExtrato
    [4]\tNova conta
    [5]\tListar contas
    [6]\tNovo usuário
    [7]\tSair

    '''
    
    # Retorna a opção de meno selecionada como um número interiro
    return int(input(textwrap.dedent(menu_text)))  # Utiliza textwrap.dedent para formatar o texto do menu corretamente


# Função para realizar um depósito na conta
def depositar(saldo, valor, extrato):
    if valor <= 0:
        print('Informe um valor positivo.')
    else:
        saldo += valor  # Adiciona o valor ao saldo atual
        extrato += f'Depósito: R$ {valor:.2f}\n'  # Adiciona a transação ao extrato
    return saldo, extrato  # Retorna o saldo e o extrato atualizados


# Função para realizar um deposito na conta
def sacar(*, saldo, valor, extrato, limite, numero_saques, LIMITE_SAQUES):
    if numero_saques >= LIMITE_SAQUES:
        print('Falha na tentativa de saque! Você excedeu o número de saques permitidos.')
    elif saldo < valor:
        print('Falha na tentativa de saque! Saldo insuficiente.')
    elif valor > limite:
        print('O valor solicitado excede o limite de saque.')
    elif valor <= 0:
        print('Operação falhou! O valor informado é inválido.')
    else:
        saldo -= valor
        extrato += f'Saque: R$ {valor:.2f}\n'
        numero_saques += 1
        print('===== SAQUE EFETUADO COM SUCESSO! =====')
    return saldo, extrato


# Função para exibir o extrato da conta
def exibir_extrato(saldo, /, *, extrato):
    print('=' * 20 + ' EXTRATO ' + '=' * 20)
    if saldo == 0:
        print('Não foram realizadas movimentações.')
    else:
        print(f'Saldo: R$ {saldo:.2f}')
    print('=' * 47)
    return saldo, extrato


# Função para criar um novo usuário
def criar_usuario(AGENCIA, numero_conta, usuarios):
    cpf = input('Informe seu CPF (somente números): ')
    usuario = filtrar_usuario(cpf, usuarios) # Verifica se o usuário ja existe na lista

    if usuario:
        print('Já existe um usuário com esse CPF!')
        return

    nome = input('Informe seu nome: ').capitalize()
    data_nascimento = input('Data de nascimento (dd-mm-aaaa): ')
    endereco = input('Informe seu endereço (logadouro, nro - bairro - cidade/sigla estado): ')


    # Adiciona o novo usuário a lita de usuários
    usuarios.append({'nome': nome, 'data_nascimento': data_nascimento, 'endereco': endereco, 'cpf': cpf})

    print('==== Usuário cadastrado com sucesso! ====')


# Função para filtrar um usuário por cpf
def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario['cpf'] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


# Função para criar um nova conta associada a um usuário existente
def criar_conta(agencia, numero_conta, usuarios):
    cpf = input('Informe o CPF do usuário (somente números): ')
    usuario = filtrar_usuario(cpf, usuarios) # Busca o usuário pelo CPF

    if usuario:
        print('\n=== Conta criada com sucesso! ===')
        return {'agencia': agencia, 'numero_conta': numero_conta, 'usuario': usuario}
    else:
        print('\nUsuário não encontrado. Criação de conta encerrada.')


# Função para listar todas as contas cadastradas
def listar_contas(contas):
    for conta in contas:
        linha = f'''\
            Agência: \t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        '''
        print("=" * 100)
        print(textwrap.dedent(linha)) # Utiliza textwrap.dedent para formatar corretamente a linha


# Função principal que coordena a interação com o usuário
def main():
    LIMITE_SAQUES = 3
    AGENCIA = '0001'

    saldo = 0
    limite = 500
    extrato = ''
    numero_saques = 0
    usuarios = [] # Lista para armazenar os usuários
    contas = [] # Lista para armazenar as contas

    while True:
        opcao = menu() # Exibe o menu e obtém a escolha do usuário

        if opcao == 1: # Opção para realizar um depósito
            valor = float(input('Informe o valor de depósito: R$ '))
            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == 2: # Opção para realizar um saque
            valor = float(input('Informe o valor de saque: R$ '))
            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                LIMITE_SAQUES=LIMITE_SAQUES,
            )

        elif opcao == 3: # Opção para exibir o extrato
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == 4: # Opção para criar uma nova conta
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            if conta:
                contas.append(conta) # Adiciona a nova conta à lista de contas

        elif opcao == 5: # Opção para listar todas as contas
            listar_contas(contas)

        elif opcao == 6:  # Opção para criar um novo usuário
            criar_usuario(AGENCIA, len(usuarios) + 1, usuarios)

        elif opcao == 7: # Opção para sair do programa
            break

        else: # Trata qualquer outra opção inválida
            print("Operação inválida. Por favor, selecione novamente a operação desejada.")


# Chama a função principal para iniciar o programa
main()
