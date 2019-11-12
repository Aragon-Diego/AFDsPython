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
    else:
        estadoA='merto'
        break
if estadoA=='muerto':
    print('cayo en el estado muerto')