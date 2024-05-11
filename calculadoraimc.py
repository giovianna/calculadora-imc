# CALCULADORA IMC EM PYTHON

print('Vamos calcular seu IMC')
altura = float(input('Digite sua altura: '))

peso = float(input('Digite o seu peso: '))

altura_calculo = altura * altura

imc = peso / altura_calculo
imc = round(imc, 2)

print('Seu IMC é:', imc)


if imc < 18.5:
    print('Sua classificação é: Magreza.')
elif 18.5 <= imc < 24.9:
    print('Sua classificação é: Normal.')
elif 25 <= imc < 29.9:
    print('Sua classificação é: Sobrepeso.')
elif 30 <= imc < 39.9:
    print('Sua classificação é: Obesidade.')
else:
    print('Sua classificação é: Obesidade grave.')
