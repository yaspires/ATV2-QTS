def calcular_valor_reserva(preco_diaria, criancas, noites, cupom):
    valor_diaria = preco_diaria + (criancas * 50)

    valor_total = valor_diaria * noites

    if cupom == "HOTEL10":
        valor_total = valor_total * 0.90

    elif cupom == "HOTEL20":
        valor_total = valor_total * 0.80

    return round(valor_total, 2)