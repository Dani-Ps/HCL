def calcular_imc(peso, altura):
    '''
    Args
    '''
    if peso <= 0 or altura <= 0:
        raise ValueError("El peso y la altura deben ser valores positivos.")

    imc = peso / (altura ** 2)
    return imc
