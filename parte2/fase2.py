
arrEstados=input('estados: separa por espacios\n').split(' ')
arrAlfabeto=input('alfabeto: separa por espacios\n').split(' ')
dictEstados={'m':[False]}
for i in arrEstados:
    dictEstados[i]=[False]
    dicMov={}
    for j in arrAlfabeto:
        estado=input(i+' cuando llega "'+j+'" a que estado se va?\n(para que no lo acepte pon m)\n')
        dicMov[j]=estado
    dictEstados[i].append(dicMov)  
arrEstadosFinales=input('estados finales: separa por espacios\n').split(' ')
for i in arrEstadosFinales:
    dictEstados[i][0]=True
estadoA=input('estado inicial: solo puede ser uno\n')
b=True
while b:
    cadena=input('cadena a evaluar:\n')
    if cadena=='00':
        b=False
        break
    estadoA1=estadoA
    for i in cadena:
        estadoA1=dictEstados[estadoA1][1][i]
    if dictEstados[estadoA1][0]:
        print('aceptado')
    else:
        if estadoA1=='m':
            print('en el estado muerto')
        else:
            print('no aceptado')