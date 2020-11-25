nombre = input('cual es tu nombre?\n')
peso = input(f'{nombre} cual es tu peso en kg?\n')
peso = float(peso)
altura = input(f'{nombre}, una cosa mas, cual es tu altura?\n')
altura = float(altura)
imc = peso / (altura * altura)

if imc >= 40:
    grado_Obesidad = 'Obesidad muy severa/morbica'
elif imc >= 35:
    grado_Obesidad = 'Obesidad severa'
elif imc >= 30:
    grado_Obesidad = 'Obesidad moderada'
elif imc >= 25:
    grado_Obesidad = 'Sobrepeso'
elif imc >= 18.5:
    grado_Obesidad = 'Peso saludable'
elif imc >= 16:
    grado_Obesidad = 'Delgadez'
elif imc >= 15:
    grado_Obesidad = 'Delgadez severa'
else:  
    grado_Obesidad = 'Delgadez muy severa'

resultado = print(f'{nombre} tu IMC es {imc:.2f}, que significa que tienes {grado_Obesidad}')
       

print (f'{nombre} ')