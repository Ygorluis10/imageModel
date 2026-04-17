def calcular_estatisticas(lista):
    """
    Calcula o total, média, valor máximo e mínimo de uma lista de números.

    Args:
        lista (list): Lista de números.

    Returns:
        tuple: (total, media, maximo, minimo)
    """
    if not lista:
        raise ValueError("A lista não pode estar vazia.")

    total = sum(lista)
    media = total / len(lista)
    maximo = max(lista)
    minimo = min(lista)

    return total, media, maximo, minimo


# Exemplo de uso
numeros = [23, 7, 45, 2, 67, 12, 89, 34, 56, 11]
total, media, maior, menor = calcular_estatisticas(numeros)

print(f"Total: {total}")
print(f"Média: {media:.2f}")
print(f"Maior: {maior}")
print(f"Menor: {menor}")