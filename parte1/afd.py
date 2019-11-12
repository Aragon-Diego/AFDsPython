estadoA='q0'
cadena=input()
for i in cadena:
    if (i == 'a' or  i == 'b') and (not estadoA == 'q2'):
        if estadoA=='q0':
            if i=='a':
               estadoA='q2'
            else:
                estadoA='q1'
        else:
            if i=='a':
                estadoA='q2'
            else:
                estadoA='muerto'
                break
    else:
        estadoA='muerto'
        break
if estadoA=='muerto':
    print('En estado muerto')
elif estadoA=='q2':
    print('aceptado')
else:
    print('no aceptado')