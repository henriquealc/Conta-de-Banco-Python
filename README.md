# Conta-de-Banco
 Conta de Banco - Desafio feito junto ao bootcamp da DIO 
================================================================================
                    Documentação do Sistema Bancário Simples
================================================================================

Este programa implementa um sistema bancário básico com as seguintes funcionalidades:

1. Menu Principal:
   - O usuário pode selecionar diferentes operações através de um menu.

2. Funções Principais:
   - Depositar: Permite ao usuário adicionar um valor ao saldo de uma conta.
   - Sacar: Permite ao usuário retirar um valor do saldo de uma conta, desde que respeite o limite de saques e o saldo disponível.
   - Extrato: Exibe o saldo atual da conta e o histórico de transações (extrato).
   - Nova Conta: Permite a criação de uma nova conta associada a um usuário existente.
   - Listar Contas: Exibe detalhes de todas as contas criadas no sistema.
   - Novo Usuário: Permite a criação de um novo usuário para associar a uma conta.

3. Estrutura de Dados:
   - O sistema utiliza listas para armazenar informações de usuários (`usuarios`) e contas (`contas`).

4. Limitações e Regras:
   - Limite de Saques: Cada conta tem um limite máximo de saques (`LIMITE_SAQUES`).
   - Limite de Saldo para Saque: Não é permitido sacar um valor maior do que o saldo disponível na conta.
   - Valores Inválidos: Operações como saque de valor negativo ou igual a zero são tratadas como inválidas.

5. Funcionamento do Código:
   - O código utiliza funções para modularizar cada operação específica (depositar, sacar, exibir extrato, etc.).
   - A função `menu()` exibe um menu de opções e retorna a escolha do usuário.
   - A função `main()` coordena a interação com o usuário, chamando as funções apropriadas com base na escolha do menu.

6. Exemplos de Uso:
   - O usuário pode realizar operações como depósitos, saques, criar novas contas e visualizar extratos diretamente pelo menu.
   - O sistema valida as entradas do usuário para garantir que as operações sejam realizadas corretamente e de forma segura.

================================================================================
