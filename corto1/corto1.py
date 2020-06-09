#Corto1
def Escribir(Nombre= 'collatz.txt',lista):
    archivo = open(Nombre,'w') #Abrir para SOBREESCRIBIR el archivo existente
    archivo.write(str(hora+' --> '+str(i)+'\n'))
        time.sleep(1)

    archivo.close() #Siempre cerrar el archivo al finalizar la escritura
    print('Append finalizado')

def par_impar(num):
    if(num%2==0):#determinamos si el numero es par 
        return True
    else:
        return False

Carne = 388
Secuencia = []

for i in range(2, Carne):
    Secuencia = []
    j=i
    Secuencia.append(j)
    while(j>1):

        if (par_impar(j)):
            j=j/2
        else:
            j=3*j+1
        Secuencia.append(j)
        print(Secuencia)


