# Importa a função 'ceil' da biblioteca math, que é utilizada para arredondar valores para cima
from math import ceil

# Lista de mensagens contendo informações sobre o empréstimo e os pagamentos
mensagens = ["Empréstimo principal efetivado: R$1000", "Mês 1: pago R$250", "Mês 2: pago R$250", "Mês 3: pago R$500"]

# Imprime as mensagens contidas na lista
for msg in mensagens:
    print(msg)

# Imprime uma mensagem informando que o empréstimo foi efetuado e solicita ao usuário o valor do empréstimo
print("Empréstimo efetuado ")
valor_prinicipal_emprestimo = float(input("Qual valor deseja pedir emprestado?\n"))

# Loop que continua até o usuário fornecer uma opção válida (v ou p) para a forma de pagamento
while True:
    opcao = input("""Escolha entre as duas opções abaixo para forma de pagamento.
                      Digite - "v" (Para pagar em valor mensal)
                      Digite - "p" (Para pagar em números de parcelas""").lower()

    # Se a opção for 'v', o usuário escolheu pagar em valores mensais predefinidos
    if opcao == 'v':
        print("Você escolheu a opção de pagar em valores pré-definidos")

        # Solicita ao usuário o valor que deseja pagar mensalmente
        valor_desejado = float(input("Qual valor deseja pagar mensalmente?\n"))

        # Calcula o número de parcelas necessárias para quitar o empréstimo
        num_parcelas = valor_prinicipal_emprestimo / valor_desejado
        num_parcelas = ceil(num_parcelas)

        # Imprime a quantidade de meses necessários para quitar o empréstimo
        print(f"Você levará {num_parcelas} meses para quitar o empréstimo.")
        break

    # Se a opção for 'p', o usuário escolheu pagar em parcelas com número específico de vezes
    elif opcao == 'p':
        print("Você escolheu a opção de pagar parcelado")

        # Solicita ao usuário a quantidade de parcelas desejada
        vezes = int(input("Em quantas parcelas deseja pagar?"))

        # Calcula o valor das parcelas para o pagamento parcelado
        parcela_valores = valor_prinicipal_emprestimo / vezes
        a = round(parcela_valores)

        # Verifica se o valor da parcela é exato ou se necessita de arredondamento
        if parcela_valores - round(parcela_valores) > 0:
            valores_a_pagar = ceil(parcela_valores)
            x = (vezes - 1) * valores_a_pagar
            y = valor_prinicipal_emprestimo - x

            # Imprime os detalhes sobre as parcelas a serem pagas
            print(f"Você pagará {vezes - 1} parcelas de R${valores_a_pagar} e 1 de R${y}")
            break
        else:
            # Imprime o valor das parcelas a serem pagas (valores exatos)
            print(f"Você pagará {vezes} parcelas de R${parcela_valores}")
            break

    # Se a opção digitada pelo usuário não for 'v' nem 'p', é solicitado que ele insira apenas 'v' ou 'p'
    elif opcao not in "vp":
        print("Apenas letras v ou p especificamente!")
