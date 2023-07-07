from math import ceil
mensagens = ["Empréstimo principal efetivado: R$1000", "Mês 1: pago R$250", "Mês 2: pago R$250", "Mês 3: pago R$500"]
for msg in mensagens:
    print(msg)
print("Empréstimo efetuado ")
valor_prinicipal_emprestimo = float(input("Qual valor deseja pedir emprestado?\n"))
while True:
    opcao = input("""Escolha entre as duas opções abaixo para forma de pagamento.
                      Digite - "v" (Para pagar em valor mensal)
                      Digite - "p" (Para pagar em números de parcelas""").lower()
    if opcao == 'v':
        print("Você escolheu a opção de pagar em valores pré-definidos")
        valor_desejado = float(input("Qual valor deseja pagar mensalmente?\n"))
        num_parcelas = valor_prinicipal_emprestimo / valor_desejado
        num_parcelas = ceil(num_parcelas)
        print(f"Você levará {num_parcelas} meses para quitar o empréstimo.")
        break
    elif opcao == 'p':
        print("Você escolheu a opção de pagar parcelado")
        vezes = int(input("Em quantas parcelas deseja pagar?"))
        parcela_valores = valor_prinicipal_emprestimo / vezes
        a = round(parcela_valores)
        if parcela_valores - round(parcela_valores) > 0:
            valores_a_pagar = ceil(parcela_valores)
            x = (vezes - 1) * valores_a_pagar
            y = valor_prinicipal_emprestimo - x
            print(f"Você pagará {vezes - 1} parcelas de R${valores_a_pagar} e 1 de R${y}")
            break
        else:
            print(f"Você pagará {vezes} parcelas de R${parcela_valores}")
            break

    elif opcao not in "vp":
        print("Apenas letras v ou p especificamente!")