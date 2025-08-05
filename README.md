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
    elif numero_cartao.startswith(('4011', '4312', '4389')): # Adicione outros prefixos Elo conforme necessário
        return "Elo"
    elif numero_cartao.startswith(('34', '37')):
        return "American Express"
    elif numero_cartao.startswith(('6011', '65')) or (numero_cartao.startswith('64') and 4 <= int(numero_cartao[2:3]) <= 9):
        return "Discover"
    elif numero_cartao.startswith('6062'):
        return "Hipercard"
    else:
        return "Desconhecida"

# Exemplo de uso:
numero_exemplo = "4111111111111111"
bandeira = detectar_bandeira(numero_exemplo)
print(f"O cartão {numero_exemplo} é da bandeira: {bandeira}")

numero_exemplo_master = "5211111111111111"
bandeira_master = detectar_bandeira(numero_exemplo_master)
print(f"O cartão {numero_exemplo_master} é da bandeira: {bandeira_master}")

numero_exemplo_elo = "4011111111111111"
bandeira_elo = detectar_bandeira(numero_exemplo_elo)
print(f"O cartão {numero_exemplo_elo} é da bandeira: {bandeira_elo}")

numero_exemplo_amex = "341111111111111"
bandeira_amex = detectar_bandeira(numero_exemplo_amex)
print(f"O cartão {numero_exemplo_amex} é da bandeira: {bandeira_amex}")

numero_exemplo_discover = "6011111111111111"
bandeira_discover = detectar_bandeira(numero_exemplo_discover)
print(f"O cartão {numero_exemplo_discover} é da bandeira: {bandeira_discover}")

numero_exemplo_hipercard = "6062111111111111"
bandeira_hipercard = detectar_bandeira(numero_exemplo_hipercard)
print(f"O cartão {numero_exemplo_hipercard} é da bandeira: {bandeira_hipercard}")

numero_exemplo_desconhecida = "1234567890123456"
bandeira_desconhecida = detectar_bandeira(numero_exemplo_desconhecida)
print(f"O cartão {numero_exemplo_desconhecida} é da bandeira: {bandeira_desconhecida}")
