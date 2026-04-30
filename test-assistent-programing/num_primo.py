import math

def is_prime(number):
    """Verifica se um número inteiro é primo.

    Args:
        number (int): Número inteiro a ser verificado.

    Returns:
        bool: True se o número for primo, False caso contrário.

    Raises:
        TypeError: Se o parâmetro não for um inteiro.
    """
    # Garantir entrada válida antes de qualquer processamento evita resultados incorretos.
    if not isinstance(number, int):
        raise TypeError("O input deve ser um inteiro.")
    
    # Números menores ou iguais a 1 não são considerados primos.
    if number <= 1:
        return False

    # O 2 é o único número par primo e deve ser tratado como caso especial.
    if number == 2:
        return True

    # Qualquer número par maior que 2 já é composto por 2.
    if number % 2 == 0:
        return False
    
    # A partir daqui, só testamos divisores ímpares até a raiz quadrada.
    # Isso reduz drasticamente o número de verificações necessárias.
    for i in range(3, int(math.sqrt(number)) + 1, 2):
        if number % i == 0:
            # Encontrar um divisor confirma que o número não é primo.
            return False
    return True

if __name__ == "__main__":
    try:
        num = int(input("Digite um número inteiro para verificar se é primo: "))
        result = is_prime(num)
        if result:
            print(f"O número {num} é primo.")
        else:
            print(f"O número {num} não é primo.")
    except ValueError:
        print("Erro: Por favor, digite um número inteiro válido.")
    except TypeError as e:
        print(f"Erro: {e}")