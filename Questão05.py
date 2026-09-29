Distância = float(input('Insira a distância da sua encomenda em quilômetros: '))
Peso = float(input('Insira o peso de sua encomenda em quilogramas: '))

def calcular_entegra(Distância, Peso):
    valor = 0
    if Distância <= 10.00:
        valor += 12
    elif Distância <= 30.00:
        valor += 20.00
    elif Distância <= 60.00: 
        valor += 35.00
    else:
        valor += 50.00

    if Peso <= 5:
        valor += 0
    elif Peso >5:
        for i in range(int((Peso - 5))):
            valor += 2

    return valor

valor_total = calcular_entegra(Distância, Peso)
print(f'O valor total da entrega será de: R${valor_total :.2f}')