Explicação do Código Refatorado (refatoracao.py)
Código analisado
def filtrar_numeros_pares(lista):
    """Retorna apenas números pares de uma lista."""
    return [numero for numero in lista if numero % 2 == 0]
Explicação linha por linha
Linha 1:
def filtrar_numeros_pares(lista):
Define uma função chamada filtrar_numeros_pares
A função recebe um parâmetro chamado lista
Esse parâmetro representa uma lista de números que será analisada
Linha 2:
"""Retorna apenas números pares de uma lista."""
Isso é uma docstring (documentação da função)
Explica de forma clara o que a função faz
Boa prática de programação (Clean Code)
Linha 3:
return [numero for numero in lista if numero % 2 == 0]

Aqui temos uma list comprehension (forma compacta de criar listas):

Parte 1:
numero for numero in lista
Percorre cada elemento da lista
A variável numero representa cada item da lista
Parte 2:
if numero % 2 == 0
Verifica se o número é par
O operador % calcula o resto da divisão
Se o resto da divisão por 2 for igual a 0 → número é par
Resultado:
Cria uma nova lista contendo apenas os números pares
Essa lista é retornada pela função
Resumo

A função:

Recebe uma lista de números
Filtra apenas os números pares
Retorna uma nova lista com esses valores
Exemplo de uso
lista = [1, 2, 3, 4, 5, 6]
resultado = filtrar_numeros_pares(lista)

print(resultado)
Saída esperada:
[2, 4, 6]
Pontos positivos do código
Nome da função claro e descritivo
Uso de docstring
Código curto e eficiente
Uso de list comprehension (boa prática em Python)
Fácil leitura e manutenção
