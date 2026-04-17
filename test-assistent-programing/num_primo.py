import math

def is_prime(number):
    """
    Verifica se um número é primo.

    Um número primo é um inteiro maior que 1 que não tem divisores positivos
    além de 1 e ele mesmo.

    Args:
        number (int): O número a ser verificado.

    Returns:
        bool: True se o número for primo, False caso contrário.

    Raises:
        TypeError: Se o input não for um inteiro.
    """
    if not isinstance(number, int):
        raise TypeError("O input deve ser um inteiro.")
    
    if number <= 1:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    
    # Verifica divisibilidade até a raiz quadrada, pulando números pares
    for i in range(3, int(math.sqrt(number)) + 1, 2):
        if number % i == 0:
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