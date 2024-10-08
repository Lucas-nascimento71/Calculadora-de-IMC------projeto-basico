# adicionei linhas delimitadoras
print('=-=' * 15)
print('               Calculo de IMC')
print('=-=' * 15)

# Entrada de dados
try:
    peso = float(input('Digite seu Peso (Kg): '))
    altura = float(input('Digite sua Altura (m): '))
except ValueError:
    print("Por favor, insira valores numéricos válidos.")

# Calculo do imc: peso dividido pela altura ao quadrado; E exibição de resultado
imc = peso / (altura ** 2)

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
else:
    Classificação = 'Obesidade grau 3 (Obesidade Mórbida).'
    
# Saída de dados
print(f'\nSeu IMC foi de {imc:.1f}.')
print(f'Sua classificação foi de {Classificação}')

# adicionei linhas delimitadoras
print('=-=' * 15)
print('                    Fim')
print('=-=' * 15)
