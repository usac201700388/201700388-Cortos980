#Corto1 

def par_impar(num):
    if(num%2==0):#determinamos si el numero es par 
        return True
    else:
        return False

Carne = 388
Secuencia = []
archivo = open('Cortos/corto1/collatz.txt','w') #Abrir para SOBREESCRIBIR el archivo existente
for i in range(2, Carne):
    Secuencia = []
    j=i
    Secuencia.append(j)
    while(j>1):

        if (par_impar(j)):
            j=j/2
        else:
            j=3*j+1
        Secuencia.append(int(j))
    archivo.write('\n'+ str(Secuencia))
archivo.close()

