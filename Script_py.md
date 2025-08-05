{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": []
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "gQerTTwHcXYN",
        "outputId": "11b1a204-bed3-41a8-8be3-bf5d2e89e48c"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "O cartão 4111111111111111 é da bandeira: Visa\n",
            "O cartão 5211111111111111 é da bandeira: MasterCard\n",
            "O cartão 4011111111111111 é da bandeira: Visa\n",
            "O cartão 341111111111111 é da bandeira: American Express\n",
            "O cartão 6011111111111111 é da bandeira: Discover\n",
            "O cartão 6062111111111111 é da bandeira: Hipercard\n",
            "O cartão 1234567890123456 é da bandeira: Desconhecida\n"
          ]
        }
      ],
      "source": [
        "def detectar_bandeira(numero_cartao):\n",
        "    \"\"\"\n",
        "    Detecta a bandeira de um cartão de crédito com base no número inicial.\n",
        "\n",
        "    Args:\n",
        "        numero_cartao (str): O número do cartão de crédito como string.\n",
        "\n",
        "    Returns:\n",
        "        str: A bandeira do cartão (Visa, MasterCard, Elo, American Express,\n",
        "             Discover, Hipercard) ou \"Desconhecida\" se não for detectada.\n",
        "    \"\"\"\n",
        "    if numero_cartao.startswith('4'):\n",
        "        return \"Visa\"\n",
        "    elif numero_cartao.startswith(('51', '52', '53', '54', '55')) or (numero_cartao.startswith('222') and 1 <= int(numero_cartao[3:4]) <= 7) or (numero_cartao.startswith('22') and 21 <= int(numero_cartao[2:4]) <= 70):\n",
        "         return \"MasterCard\"\n",
        "    elif numero_cartao.startswith(('4011', '4312', '4389')): # Adicione outros prefixos Elo conforme necessário\n",
        "        return \"Elo\"\n",
        "    elif numero_cartao.startswith(('34', '37')):\n",
        "        return \"American Express\"\n",
        "    elif numero_cartao.startswith(('6011', '65')) or (numero_cartao.startswith('64') and 4 <= int(numero_cartao[2:3]) <= 9):\n",
        "        return \"Discover\"\n",
        "    elif numero_cartao.startswith('6062'):\n",
        "        return \"Hipercard\"\n",
        "    else:\n",
        "        return \"Desconhecida\"\n",
        "\n",
        "# Exemplo de uso:\n",
        "numero_exemplo = \"4111111111111111\"\n",
        "bandeira = detectar_bandeira(numero_exemplo)\n",
        "print(f\"O cartão {numero_exemplo} é da bandeira: {bandeira}\")\n",
        "\n",
        "numero_exemplo_master = \"5211111111111111\"\n",
        "bandeira_master = detectar_bandeira(numero_exemplo_master)\n",
        "print(f\"O cartão {numero_exemplo_master} é da bandeira: {bandeira_master}\")\n",
        "\n",
        "numero_exemplo_elo = \"4011111111111111\"\n",
        "bandeira_elo = detectar_bandeira(numero_exemplo_elo)\n",
        "print(f\"O cartão {numero_exemplo_elo} é da bandeira: {bandeira_elo}\")\n",
        "\n",
        "numero_exemplo_amex = \"341111111111111\"\n",
        "bandeira_amex = detectar_bandeira(numero_exemplo_amex)\n",
        "print(f\"O cartão {numero_exemplo_amex} é da bandeira: {bandeira_amex}\")\n",
        "\n",
        "numero_exemplo_discover = \"6011111111111111\"\n",
        "bandeira_discover = detectar_bandeira(numero_exemplo_discover)\n",
        "print(f\"O cartão {numero_exemplo_discover} é da bandeira: {bandeira_discover}\")\n",
        "\n",
        "numero_exemplo_hipercard = \"6062111111111111\"\n",
        "bandeira_hipercard = detectar_bandeira(numero_exemplo_hipercard)\n",
        "print(f\"O cartão {numero_exemplo_hipercard} é da bandeira: {bandeira_hipercard}\")\n",
        "\n",
        "numero_exemplo_desconhecida = \"1234567890123456\"\n",
        "bandeira_desconhecida = detectar_bandeira(numero_exemplo_desconhecida)\n",
        "print(f\"O cartão {numero_exemplo_desconhecida} é da bandeira: {bandeira_desconhecida}\")"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# Nova seção"
      ],
      "metadata": {
        "id": "BFxqSgbTd445"
      }
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "3fc62faf"
      },
      "source": [
        "# Detector de Bandeira de Cartão de Crédito\n",
        "\n",
        "Este projeto contém um script Python para detectar a bandeira de um cartão de crédito com base nos dígitos iniciais do número do cartão.\n",
        "\n",
        "## Como usar\n",
        "\n",
        "1.  Clone este repositório:"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "cfacde66"
      },
      "source": [
        "    cd <nome do diretório>"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "b87b1524"
      },
      "source": [
        "    python nome_do_seu_arquivo.py"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "761add5a"
      },
      "source": [
        "def detectar_bandeira(numero_cartao):\n",
        "    \"\"\"\n",
        "    Detecta a bandeira de um cartão de crédito com base no número inicial.\n",
        "\n",
        "    Args:\n",
        "        numero_cartao (str): O número do cartão de crédito como string.\n",
        "\n",
        "    Returns:\n",
        "        str: A bandeira do cartão (Visa, MasterCard, Elo, American Express,\n",
        "             Discover, Hipercard) ou \"Desconhecida\" se não for detectada.\n",
        "    \"\"\"\n",
        "    if numero_cartao.startswith('4'):\n",
        "        return \"Visa\"\n",
        "    elif numero_cartao.startswith(('51', '52', '53', '54', '55')) or (numero_cartao.startswith('222') and 1 <= int(numero_cartao[3:4]) <= 7) or (numero_cartao.startswith('22') and 21 <= int(numero_cartao[2:4]) <= 70):\n",
        "         return \"MasterCard\"\n",
        "    elif numero_cartao.startswith(('4011', '4312', '4389')): # Adicione outros prefixos Elo conforme necessário\n",
        "        return \"Elo\"\n",
        "    elif numero_cartao.startswith(('34', '37')):\n",
        "        return \"American Express\"\n",
        "    elif numero_cartao.startswith(('6011', '65')) or (numero_cartao.startswith('64') and 4 <= int(numero_cartao[2:3]) <= 9):\n",
        "        return \"Discover\"\n",
        "    elif numero_cartao.startswith('6062'):\n",
        "        return \"Hipercard\"\n",
        "    else:\n",
        "        return \"Desconhecida\"\n",
        "\n",
        "# Exemplo de uso:\n",
        "numero_exemplo = \"4111111111111111\"\n",
        "bandeira = detectar_bandeira(numero_exemplo)\n",
        "print(f\"O cartão {numero_exemplo} é da bandeira: {bandeira}\")\n",
        "\n",
        "numero_exemplo_master = \"5211111111111111\"\n",
        "bandeira_master = detectar_bandeira(numero_exemplo_master)\n",
        "print(f\"O cartão {numero_exemplo_master} é da bandeira: {bandeira_master}\")\n",
        "\n",
        "numero_exemplo_elo = \"4011111111111111\"\n",
        "bandeira_elo = detectar_bandeira(numero_exemplo_elo)\n",
        "print(f\"O cartão {numero_exemplo_elo} é da bandeira: {bandeira_elo}\")\n",
        "\n",
        "numero_exemplo_amex = \"341111111111111\"\n",
        "bandeira_amex = detectar_bandeira(numero_exemplo_amex)\n",
        "print(f\"O cartão {numero_exemplo_amex} é da bandeira: {bandeira_amex}\")\n",
        "\n",
        "numero_exemplo_discover = \"6011111111111111\"\n",
        "bandeira_discover = detectar_bandeira(numero_exemplo_discover)\n",
        "print(f\"O cartão {numero_exemplo_discover} é da bandeira: {bandeira_discover}\")\n",
        "\n",
        "numero_exemplo_hipercard = \"6062111111111111\"\n",
        "bandeira_hipercard = detectar_bandeira(numero_exemplo_hipercard)\n",
        "print(f\"O cartão {numero_exemplo_hipercard} é da bandeira: {bandeira_hipercard}\")\n",
        "\n",
        "numero_exemplo_desconhecida = \"1234567890123456\"\n",
        "bandeira_desconhecida = detectar_bandeira(numero_exemplo_desconhecida)\n",
        "print(f\"O cartão {numero_exemplo_desconhecida} é da bandeira: {bandeira_desconhecida}\")"
      ],
      "execution_count": null,
      "outputs": []
    }
  ]
}