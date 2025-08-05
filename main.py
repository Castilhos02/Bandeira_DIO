
def detectar_bandeira(numero_cartao):
    """
    Detecta a bandeira de um cartão de crédito com base no número inicial.

    Args:
        numero_cartao (str): O número do cartão de crédito como string.

    Returns:
        str: A bandeira do cartão (Visa, MasterCard, Elo, American Express,
             Discover, Hipercard) ou "Desconhecida" se não for detectada.
    """
    if numero_cartao.startswith('4'):
        return "Visa"
    elif numero_cartao.startswith(('51', '52', '53', '54', '55')) or (numero_cartao.startswith('222') and 1 <= int(numero_cartao[3:4]) <= 7) or (numero_cartao.startswith('22') and 21 <= int(numero_cartao[2:4]) <= 70):
         return "MasterCard"
    elif numero_cartao.startswith(('4011', '4312', '4389')):  # Adicione outros prefixos Elo conforme necessário
        return "Elo"
    elif numero_cartao.startswith(('34', '37')):
        return "American Express"
    elif numero_cartao.startswith(('6011', '65')) or (numero_cartao.startswith('64') and 4 <= int(numero_cartao[2:3]) <= 9):
        return "Discover"
    elif numero_cartao.startswith('6062'):
        return "Hipercard"
    else:
        return "Desconhecida"

# Exemplos de uso
if __name__ == "__main__":
    exemplos = [
        "4111111111111111",
        "5211111111111111",
        "4011111111111111",
        "341111111111111",
        "6011111111111111",
        "6062111111111111",
        "1234567890123456"
    ]

    for numero in exemplos:
        print(f"O cartão {numero} é da bandeira: {detectar_bandeira(numero)}")
