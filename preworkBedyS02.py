lista1 = [1, 4, 7, 9, 10]

lista1.append(12)

lista1.pop(0)
## print(lista1)


Mycat = {
    'nombre' : 'petunia',
    'hair color' : 'calico',
    'hair length': 'medium',
    'adoption day' : 'January 6th, 2020',
    'City of birth' : 'Tlaquepaque',
}
Chai = {
    'nombre' : 'chai',
    'hair color' : 'black and white',
    'hair length': 'medium',
    'adoption day' : 'cant remember =/',
    'City of birth' : 'Hermosillo',
}
catList = [] 
catList.append(Mycat)
catList.append(Chai)

Nombres_Cat = []
for gatos in catList:
    nombreGato = gatos.get('nombre')
    if nombreGato is not None:
        Nombres_Cat.append(gatos)
for gatos in Nombres_Cat:
    print(gatos['nombre'])

def sumar_dos_a_numero(numero):
    suma = numero + 2
    return suma

suma_de_5_mas_2 = sumar_dos_a_numero(5)
print(suma_de_5_mas_2)

def holita():
    print('hola edna')
    print('holita')

holita()


big = max('Hello world')
print(big)

tiny = min('Hello world')
print(tiny)     