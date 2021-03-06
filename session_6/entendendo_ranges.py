"""
Ranges

Precisamos conhecer o loop for para usar os ranges.
Precisamos conhecer o range para trabalhar melhor com os loops for.

Ranges são utilizados para gerar sequências numéricas, não de forma aleatória,
mas sim de maneira especificada.

Formas Gerais:

Forma 1
range(valor_de_parada)

OBS: valor_de_parada não inclusive (inicio padrão 0, e em passo de 1 em 1)

Exemplo forma 1
for num in range(11):
    print(num)

Forma 2
range(valor_de_inicio, valor_de_parada)

OBS: valor_de_parada não incluso (inicio especificado, passo de 1 em 1)

Exemplo forma 2
for num in range(4, 11):
    print(num)

Forma 3
range(valor_de_inicio, valor_de_parada, passo)

OBS: valor_de_parada não incluso (inicio especificado, e passo especificado)

Exemplo forma 3
for num in range(1, 10, 2)
    print(num)

Forma 4 (inversa
range(valor_de_inicio, valor_de_parada, passo)

OBS: valor_de_parada não incluso (inicio especificado, e passo especificado)

Exemplo forma 4
for num in range(10, 0, -1)
    print(num)
"""

