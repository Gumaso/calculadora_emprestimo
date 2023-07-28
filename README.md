# calculadora_emprestimo
Calculadora de Empréstimos Diferenciado
Essa é uma calculadora de empréstimos que permite calcular diferentes cenários de pagamento, como pagamento diferenciado e pagamento em anuidade. Ela foi implementada em Python e pode ser executada por linha de comando, permitindo que você forneça os parâmetros necessários para realizar os cálculos de forma flexível.

# Pré-requisitos
Antes de executar o programa, é necessário ter o Python instalado no seu sistema. Certifique-se de que você tenha a versão correta do Python instalada para que o programa funcione corretamente.

# Como utilizar
Baixe o arquivo **calculadora_emprestimos.py** e salve-o em um diretório de sua preferência.

Abra o terminal ou prompt de comando e navegue até o diretório onde o arquivo calculadora_emprestimos.py está localizado.

Para executar o programa, use o seguinte comando:


python **calculadora_emprestimos.py** [argumentos]
Substitua [argumentos] pelos parâmetros necessários para realizar os cálculos. Consulte a seção "Argumentos disponíveis" abaixo para saber quais argumentos estão disponíveis e como usá-los.

# Argumentos disponíveis
Para usar a calculadora, você pode fornecer os seguintes argumentos na linha de comando:

**-t** ou **--tipo**: Define o tipo de cálculo a ser realizado, escolhendo entre pagamento diferenciado (dif) ou pagamento em anuidade (ano).

**-p** ou **--pagamento**: Define o valor do pagamento mensal ou valor mensal a ser pago (dependendo do tipo de cálculo).

**-v** ou **--valor_emprestimo**: Define o valor do empréstimo desejado.

**-n** ou **--numeros_pagamentos**: Define o número de parcelas ou meses em que o empréstimo será quitado.

**-j** ou **--juros**: Define a porcentagem de juros anual.

# Exemplo de uso
Aqui estão alguns exemplos de como usar a calculadora de empréstimos:

Calcular pagamento diferenciado:

python calculadora_emprestimos.py -t dif -v 10000 -n 12 -j 10
Isso calculará o pagamento diferenciado para um empréstimo de R$ 10.000, com 12 meses para quitar e taxa de juros anual de 10%.

Calcular pagamento em anuidade:

python calculadora_emprestimos.py -t ano -p 1000 -n 12 -j 8
Isso calculará o valor do pagamento mensal para quitar um empréstimo de R$ 1.000 em 12 meses, com taxa de juros anual de 8%.

# Observações
Certifique-se de fornecer os valores corretos e válidos para cada argumento, como números positivos e as opções válidas para o tipo de cálculo.
Se você não fornecer argumentos suficientes ou válidos, o programa emitirá mensagens de erro e fornecerá ajuda sobre como usar os argumentos corretamente.
Esta calculadora foi desenvolvida para fins educacionais e pode não considerar todos os fatores relevantes em um cenário real de empréstimo. Sempre consulte um profissional financeiro antes de tomar decisões financeiras importantes.
Espero que esta calculadora de empréstimos seja útil para você realizar simulações financeiras e entender melhor suas opções de pagamento. Sinta-se à vontade para usar, modificar e compartilhar esse programa conforme necessário. Se tiver alguma dúvida ou sugestão, não hesite em entrar em contato!
