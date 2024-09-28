# Entrada de dados
peso = float(input('Digite seu Peso (Kg): '))
altura = float(input('Digite sua Altura (m): '))

# Calculo IMC e exibição de resultado
imc = peso / (altura ** 2)
print(f'Seu IMC: {imc:.1f}')

# Classificação do IMC
if imc < 16.9:
    Classificação = 'Muito abaixo do Peso'
elif 17 <= imc <= 18.4:
    Classificação = 'Abaixo do Peso.'
elif 18.5 <= imc <= 24.9:
    Classificação = 'Peso Normal.'
elif 25 <= imc <= 29.9:
    Classificação = 'Sobrepeso/Acima do peso.'
elif 30 <= imc <= 34.9:
    Classificação = 'Obesidade grau 1.'
elif 35 <= imc <= 40:
    Classificação = 'Obesidade grau 2.'
elif imc > 40:
    Classificação = 'Obesidade grau 3 (Obesidade Mórbida).'
    
# Saída de dados
print(f'Seu IMC foi de {imc}.')
print(f'Sua classificação foi de ')