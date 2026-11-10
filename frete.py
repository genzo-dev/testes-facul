def calcular_frete(peso_gramas: int) -> int:
    if peso_gramas <= 0:
        raise ValueError("O peso deve ser maior que zero")
    if peso_gramas > 10000:
        raise ValueError("Produto acima do limite de envio")
    if peso_gramas <= 1000:
        return 10
    elif peso_gramas <= 5000:
        return 20
    else:
        return 30
