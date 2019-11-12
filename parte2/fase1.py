estadoA='q0'
estados={'q0':True,'q1':False,'q2':False,'q3':True,'m':False}
alfabeto=['a','b']
cadena=input()
for i in cadena:
    if i in alfabeto:
        if estadoA=='q0':
            if i == 'a':
                estadoA='q2'
            else:
                estadoA='q1'
        elif estadoA=='q1':
            if i == 'a':
                estadoA='q3'
            else:
                estadoA='m'
        elif estadoA=='q2':
            if i == 'a':
                estadoA='q2'
            else:
                estadoA='q3'
        elif estadoA=='q3':
            if i == 'a':
                estadoA='m'
            else:
                estadoA='q0'
        else:
            estadoA='m'
            break   
    else:
        estadoA='m'
        break
if estados[estadoA]:
    print('aceptado')
else:
    if estadoA == 'm':
        print('en estado muerto')
    else:
        print('no aceptado')