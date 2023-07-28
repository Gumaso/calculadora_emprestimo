from math import log, ceil

# Função para calcular o valor da prestação mensal em um empréstimo em anuidade
def pagamento_anuidade():
    while True:
        # Solicita o valor do empréstimo ao usuário
        print("\033[33mDigite o valor do empréstimo:")
        P = input()
        while not P.isdigit():
            print("\033[31mAPENAS NÚMEROS E POSITIVOS!\033[m")
            print("\033[33mDigite o valor do empréstimo:")
            P = input()
        P = float(P)

        # Solicita o número de pagamentos ao usuário
        print("Digite a quantidade de vezes:")
        n = input()
        while not n.isdigit():
            print("\033[31mAPENAS NÚMEROS E POSITIVOS!\033[m")
            print("\033[33mDigite a quantidade de vezes:")
            n = input()
        n = int(n)

        # Solicita a taxa de juros ao usuário
        print("\033[33mDigite o juros do empréstimo:")
        i = input()
        while not i.isdigit():
            print("\033[31mAPENAS NÚMEROS E POSITIVOS!\033[m")
            print("\033[33mDigite o juros do empréstimo:")
            i = input()
        i = float(i)
        break

    # Converte a taxa de juros anual para taxa mensal
    i = (i / 100) / 12

    # Calcula o valor da prestação mensal em empréstimo em anuidade
    A = P * (i * (1 + i) ** n / (((1 + i) ** n) - 1))
    print(f"Seu pagamento mensal é: R${ceil(A)}!")

# Função para calcular o valor principal do empréstimo em um empréstimo em anuidade
def emprestimo_principal():
    while True:
        # Solicita o valor da prestação mensal ao usuário
        print("\033[33mDigite o valor do pagamento da anuidade")
        A = input()
        while not A.isdigit():
            print("\033[31mAPENAS NÚMEROS E POSITIVOS!\033[m")
            print("\033[33mDigite o valor do pagamento da anuidade")
            A = input()
        A = float(A)

        # Solicita o número de pagamentos ao usuário
        print("\033[33mDigite a quantidade de vezes:")
        n = input()
        while not n.isdigit():
            print("\033[31mAPENAS NÚMEROS E POSITIVOS!\033[m")
            print("\033[33mDigite a quantidade de vezes:")
            n = input()
        n = int(n)

        # Solicita a taxa de juros ao usuário
        print("\033[33mDigite o juros do empréstimo:")
        i = input()
        while not i.isdigit():
            print("\033[31mAPENAS NÚMEROS E POSITIVOS!\033[m")
            print("\033[33mDigite o juros do empréstimo:")
            i = input()
        i = float(i)
        break

    # Converte a taxa de juros anual para taxa mensal
    i = (i / 100) / 12

    # Calcula o valor principal do empréstimo em um empréstimo em anuidade
    P = A / (i * (1 + i) ** n / ((1 + i) ** n - 1))
    print(f"Valor do seu empréstimo: R${P}!")

# Função para calcular o número de pagamentos mensais para quitar o empréstimo
def numero_pagamentos():
    while True:
        # Solicita o valor do empréstimo ao usuário
        print("\033[33mDigite o valor do empréstimo:")
        P = input()
        while not P.isdigit():
            print("\033[31mAPENAS NÚMEROS E POSITIVOS!\033[m")
            print("\033[33mDigite o valor do empréstimo:")
            P = input()
        P = float(P)

        # Solicita o valor do pagamento mensal ao usuário
        print("Digite o valor do pagamento mensal:")
        A = input()
        while not A.isdigit():
            print("\033[31mAPENAS NÚMEROS E POSITIVOS!\033[m")
            print("\033[33mDigite o valor do pagamento mensal:")
            A = input()
        A = float(A)

        # Solicita a taxa de juros ao usuário
        print("\033[33mDigite o juros do empréstimo:")
        i = input()
        while not i.isdigit():
            print("\033[31mAPENAS NÚMEROS E POSITIVOS!\033[m")
            print("\033[33mDigite o juros do empréstimo:")
            i = input()
        i = float(i)
        break

    # Converte a taxa de juros anual para taxa mensal
    i = (i / 100) / 12

    # Calcula o número de pagamentos mensais necessários para quitar o empréstimo
    base_log = (A / (A - (i * P)))
    numero = 1 + i
    n = log(base_log, numero)
    n = ceil(n) + 1
    n = round(n) / 12
    n = round(n, 1)
    anos = str(n).split(".")[0]
    meses = str(n).split(".")[1]
    return print(f"""\033[mTempo para quitação.
    {anos} anos
    {meses} meses""")

# Função principal do programa
def main():
    # Exibe o menu de opções para o usuário
    option = input("""
        \033[37mEscolha uma das opções para calcular formas de empréstimos\033[m
        n - número de pagamentos mensais
        a - valor da prestação mensal (anuidade)
        p - valor principal do empréstimo
        \033[33mDigite uma das opções:\033[m\n""")
    while option not in "nap":
        print("Apenas as opções (n, a, p)")
        option = input()

    # Chama a função correspondente ao tipo de cálculo escolhido pelo usuário
    if option == 'n':
        numero_pagamentos()
    elif option == 'a':
        pagamento_anuidade()
    elif option == 'p':
        emprestimo_principal()

# Verifica se o programa está sendo executado diretamente (não importado como módulo)
if __name__ == '__main__':
    main()
