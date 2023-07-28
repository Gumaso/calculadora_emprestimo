# Importação dos módulos necessários
from argparse import ArgumentParser
from math import ceil, log

# Configuração do parser para receber os argumentos da linha de comando
parser = ArgumentParser(description="Uma calculadora de empréstimos diferenciado.")

# Definição dos argumentos aceitos pelo programa
parser.add_argument("-t", '--tipo',
                    help="Define qual tipo de calculo a ser efetuado, sendo ele pagamento diferenciado "
                         "ou pagamento em anuidade.",
                    choices=["dif", 'ano'])

parser.add_argument("-p", "--pagamento",
                    type=int,
                    help="Parâmetro usado para calcular em quantos meses um empréstimo será quitado.")

parser.add_argument('-v', '--valor_emprestimo',
                    type=float,
                    help="Digite 'valor_emprestimo=valor' para adicionar o valor de empréstimo. "
                         "Exemplo: valor_emprestimo=1000000")

parser.add_argument('-n', "--numeros_pagamentos",
                    type=int,
                    help="Digite 'numeros_pagamentos=quantidade_de_meses' para definir em quantas vezes irá pagar."
                         "Exemplo: numeros_pagamentos=32")

parser.add_argument('-j', '--juros',
                    type=float,
                    help="Digite 'juros=valor' para definir a porcentagem de juros anual. Exemplo: juros=12. "
                         "#Se der erro, tente: -i valor")

# Faz o parsing dos argumentos fornecidos na linha de comando
args = parser.parse_args()

# Lista de argumentos fornecidos, excluindo os valores None
argumentos = [args.valor_emprestimo, args.numeros_pagamentos, args.juros, args.pagamento, args.tipo]
while None in argumentos:
    argumentos.remove(None)

# Verifica se foram fornecidos pelo menos 4 argumentos obrigatórios
if len(argumentos) < 4:
    print(len(argumentos))
    print("Quantidade de parâmetros inválidos. Use ajuda -h ou --help para mais detalhes!")

# Verifica se os valores fornecidos são válidos (diferente de 'dif' ou 'ano', e valores positivos)
for item in argumentos:
    if item not in ['dif', 'ano'] and item <= 0:
        print("Valor para o parâmetro incorreto, apenas números positivos!")
        break


def calculo(p, n, j):
    """Calcula pagamento diferenciado
    p = Valor do empréstimo desejado
    n = Número de parcelas
    j = Juros anual"""

    m = 1
    soma = 0

    # Converte a taxa de juros anual para taxa mensal
    j = (j / 100) / 12

    while m < n:
        pd = (p / n) + j * (p - p * (m - 1) / n)
        print(f"O pagamento da parcela n°{m}: R${ceil(pd):.2f}")
        soma += pd
        m += 1

    if m == n:
        pd = (p / n) + j * (p - p * (m - 1) / n)
        print(f"O último pagamento será no valor de: R${ceil(pd):.2f}")
        soma += pd

    print(f"Total pago= R${soma:.2f}")
    print(f"Pagamento em excesso = {(soma - p):.2f}")


def anuidade(pmt, j, n):
    """Calcula pagamento em anuidade
    pmt = Valor do pagamento mensal
    j = Juros anual
    n = Número de parcelas"""

    # Converte a taxa de juros anual para taxa mensal
    j = (j / 100) / 12

    n = -n
    x = pmt * (1 - ((1 + j) ** n))
    p = x / j
    return p


def numero_pagamentos(p, a, j):
    """Calcula o número de pagamentos para quitar o empréstimo
    p = Valor do empréstimo desejado
    a = Valor do pagamento mensal
    j = Juros anual"""

    # Converte a taxa de juros anual para taxa mensal
    j = (j / 100) / 12

    base_log = (a / (a - (j * p)))
    numero = 1 + j
    n = log(base_log, numero)
    n = ceil(n) + 1
    n = round(n) / 12
    n = round(n, 1)
    anos = str(n).split(".")[0]
    meses = str(n).split(".")[1]
    return print(f"""\033[mTempo para quitação.
    {anos} anos
    {meses} meses""")


# Verifica o tipo de cálculo a ser realizado
if args.tipo == "dif":
    # Realiza o cálculo de pagamento diferenciado
    calculo(args.valor_emprestimo, args.numeros_pagamentos, args.juros)
elif args.tipo == 'ano':
    # Verifica se o valor do empréstimo foi fornecido
    if args.valor_emprestimo not in argumentos:
        # Realiza o cálculo para encontrar o valor do pagamento mensal para quitar o empréstimo em anuidade
        print(f"{ceil(anuidade(args.pagamento, args.juros, args.numeros_pagamentos)):.2f}")
    # Verifica se a quantidade de parcelas foi fornecida
    elif args.numeros_pagamentos not in argumentos:
        # Realiza o cálculo para encontrar o número de parcelas necessárias para quitar o empréstimo em anuidade
        numero_pagamentos(p=args.valor_emprestimo, a=args.pagamento, j=args.juros)
    else:
        # Realiza o cálculo para encontrar o valor do pagamento mensal em anuidade e o valor total pago
        j = (args.juros / 100) / 12
        PI = (args.valor_emprestimo * args.juros / 12) / (1 - 1 / (1 + args.juros / 12) ** args.numeros_pagamentos)
        A = args.valor_emprestimo * (
                j * (1 + j) ** args.numeros_pagamentos / (((1 + j) ** args.numeros_pagamentos) - 1))
        pagamento_excessivo = ceil(A) * args.numeros_pagamentos
        print(f"Seu pagamento mensal é: R${ceil(A)}!")
        print(f"Pagamento excessivo: R${(pagamento_excessivo - args.valor_emprestimo):.2f}")
# Caso o tipo de cálculo fornecido seja diferente de 'dif' ou 'ano'
elif args.tipo != 'dif' or 'ano':
    print("Parâmetro '--tipo' inválido ou ausente.")
