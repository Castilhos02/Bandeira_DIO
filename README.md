
# Detectar Bandeira de Cartão de Crédito

Este projeto em Python tem como objetivo identificar a **bandeira de um cartão de crédito** com base no número informado. Ele analisa os prefixos conhecidos de cada bandeira e retorna a correspondente, ou "Desconhecida" se não identificar.

## 🚀 Funcionalidades

- Detecta as principais bandeiras de cartões:
  - Visa
  - MasterCard
  - Elo
  - American Express
  - Discover
  - Hipercard
- Fácil de usar e personalizar.

## 🧠 Como funciona

A função `detectar_bandeira(numero_cartao)` analisa os dígitos iniciais do número do cartão, comparando com os prefixos que caracterizam cada bandeira.

```python
def detectar_bandeira(numero_cartao):
    if numero_cartao.startswith('4'):
        return "Visa"
    elif numero_cartao.startswith(('51', '52', '53', '54', '55')) or (numero_cartao.startswith('222') and 1 <= int(numero_cartao[3:4]) <= 7) or (numero_cartao.startswith('22') and 21 <= int(numero_cartao[2:4]) <= 70):
        return "MasterCard"
    elif numero_cartao.startswith(('4011', '4312', '4389')):
        return "Elo"
    elif numero_cartao.startswith(('34', '37')):
        return "American Express"
    elif numero_cartao.startswith(('6011', '65')) or (numero_cartao.startswith('64') and 4 <= int(numero_cartao[2:3]) <= 9):
        return "Discover"
    elif numero_cartao.startswith('6062'):
        return "Hipercard"
    else:
        return "Desconhecida"
```

## ▶️ Exemplo de uso

```python
numero_exemplo = "4111111111111111"
print(detectar_bandeira(numero_exemplo))  # Saída: Visa
```

## 📁 Arquivos

- `main.py`: Código fonte da função com exemplos de uso.
- `README.md`: Este arquivo com informações sobre o projeto.

## ✅ Requisitos

- Python 3.6 ou superior

## 📌 Observações

Este projeto é educativo e não garante cobertura completa de todos os prefixos possíveis de bandeiras de cartões. Para produção, considere o uso de bibliotecas validadas.

## 📄 Licença

Este projeto está sob a licença MIT.
