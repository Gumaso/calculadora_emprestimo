import math
from math import log, ceil


def pagamento_anuidade():
    while True:
        print("\033[33mDigite o valor do empréstimo:")
        P = input()
        while not P.isdigit():
            print("\033[31mAPENAS NÚMEROS E POSITIVOS!\033[m")
            print("\033[33mDigite o valor do empréstimo:")
            P = input()
        P = float(P)
        print("Digite a quantidade de vezes:")
        n = input()
        while not n.isdigit():
            print("\033[31mAPENAS NÚMEROS E POSITIVOS!\033[m")
            print("\033[33mDigite a quantidade de vezes:")
            n = input()
        n = int(n)
        print("\033[33mDigite o juros do empréstimo:")
        i = input()
        while not i.isdigit():
            print("\033[31mAPENAS NÚMEROS E POSITIVOS!\033[m")
            print("\033[33mDigite o juros do empréstimo:")
            i = input()
        i = float(i)
        break
    i = (i / 100) / 12
    A = P * (i * (1 + i) ** n / (((1 + i) ** n) - 1))
    print(f"Seu pagamento mensal é: R${ceil(A)}!")




def emprestimo_principal():
    while True:
        print("\033[33mDigite o valor do pagamento da anuidade")
        A = input()
        while not A.isdigit():
            print("\033[31mAPENAS NÚMEROS E POSITIVOS!\033[m")
            print("\033[33mDigite o valor do pagamento da anuidade")
            A = input()
        A = float(A)
        print("\033[33mDigite a quantidade de vezes:")
        n = input()
        while not n.isdigit():
            print("\033[31mAPENAS NÚMEROS E POSITIVOS!\033[m")
            print("\033[33mDigite a quantidade de vezes:")
            n = input()
        n = int(n)
        print("\033[33mDigite o juros do empréstimo:")
        i = input()
        while not i.isdigit():
            print("\033[31mAPENAS NÚMEROS E POSITIVOS!\033[m")
            print("\033[33mDigite o juros do empréstimo:")
            i = input()
        i = float(i)
        break
    i = (i / 100) / 12
    P = A / (i * (1 + i) ** n / ((1 + i) ** n - 1))
    print(f"Valor do seu empréstimo: R${P}!")


def numero_pagamentos():
    while True:
        print("\033[33mDigite o valor do empréstimo:")
        P = input()
        while not P.isdigit():
            print("\033[31mAPENAS NÚMEROS E POSITIVOS!\033[m")
            print("\033[33mDigite o valor do empréstimo:")
            P = input()
        P = float(P)
        print("Digite o valor do pagamento mensal:")
        A = input()
        while not A.isdigit():
            print("\033[31mAPENAS NÚMEROS E POSITIVOS!\033[m")
            print("\033[33mDigite o valor do pagamento mensal:")
            A = input()
        A = float(A)
        print("\033[33mDigite o juros do empréstimo:")
        i = input()
        while not i.isdigit():
            print("\033[31mAPENAS NÚMEROS E POSITIVOS!\033[m")
            print("\033[33mDigite o juros do empréstimo:")
            i = input()
        i = float(i)
        break
    i = (i / 100) / 12
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



option = input("""
\033[37mEscolha uma das opções para calcular formas de empréstimos\033[m
n - número de pagamentos mensais
a - valor da prestação mensal (anuidade)
p - valor principal do empréstimo
\033[33mDigite uma das opções:\033[m\n""")
while option not in "nap":
    print("Apenas as opções (n, a, p)")
    option = input()
if option == 'n':
    numero_pagamentos()
elif option == 'a':
    pagamento_anuidade()
elif option == 'p':
    emprestimo_principal()


