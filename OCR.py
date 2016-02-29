import matplotlib.image as mpimagen#Se importa la libreria image como mpimagen.
import csv#Importa la libreria para la creación de archivos csv.
import os#De la libreria os se importa la función walk

#Calcular_dimenciones()
#Mediante la función de .shape se obtienen las dimensiones de la imagen.
#A la variable dimenciones 
def Calcular_dimenciones(imagen):
    #Calcula la dimención de la imagen
    dimenciones=imagen.shape#Se le asigna a la variable "dimenciones" el tamaño de la imagen mediante la función .shape la cual devuelve las dimensiones de la imagen.
    print('Dimenciones',dimenciones)#Se imprime la variable "dimenciones".
    return dimenciones

#Razon
#Se optiene la razon de filas entre columnas.
#Se realiza la división de las filas entre las columnas para obtener la razon de la imagen.
def Razon(dimenciones):
    razon=dimenciones[0]/dimenciones[1]#A la variable "razon" se le asigna lo obtenido de la división de dimenciones[0] (columnas) y dimenciones[1] (filas)
    print('Razon: ',razon)#Se imprime la variable "razon".
    return razon

#pixeles_blancosNegro()
#Se contabiliza el numero de imageneles negros y el numero de imageneles pixeles_blancoss 
#encontrados en la imagen.
#Se compara la variable "imagen" en las posiciones "i" y en "j" si es diferente de cero.
#la variable pixeles_blancos aumenta, sino la variable negro aumenta haciendo asi el conteo de
#ambos dentro de toda la imagen.
#Puntos pixeles_blancoss y negros.
def Pixeles_blancos(imagen,dimenciones):        
    pixeles_blancos=0#Se inicializa la variabe "pixeles_blancos".
    for i in range(0,dimenciones[0]):#Primer ciclo for recorre las columnas de la imagen.
        for j in range(0,dimenciones[1]):#Segndo ciclo for recorre las filas de la imagen.
            if (imagen[i][j]!=0):#Comparación de la variable "imagen" en las posiciones "i" y "j" si es diferente de cero.
                pixeles_blancos=pixeles_blancos+1#Aumento de la variable si "imagen[i][j]" es diferente de cero.
    print('Area: ',pixeles_blancos)#Se imprime la variable puntos a la cual se le asigno previamente ek valor de la división de las variables pixeles_blancos y negro.
    return pixeles_blancos

#Numero_De_Bits_Que_Representan_La_Imagen()
#Se recorre la imagen desde distintas posiciones para verificar 
#el numero de ceros y unos que tiene la misma en esa linea.
#Las variables dimenciones[0] y dimenciones[1] representan filas y columnas de la imagen.
#La variable "mc" esta representando una posicion especifica de las columnas en la imagen.
#La variable "mf" esta representando una posicion especifica de las filas de la imagen.
#imagen es la variable a la que se le asigno los valores de la imagne que se carga previamente.
def Numero_De_Bits_Que_Representan_La_Imagen(imagen,dimenciones):
    #Corte a la mitad de la imagen horizontalmente
    cont1=0
    fila_horizontal_mitad_pixeles=int(dimenciones[0]/2)#A fila_horizontal_mitad_pixeles se le asigna el valor de un entero obtenido por la divicion de dimenciones entre 2.
    for i in range(0,dimenciones[1]):#Ciclo for que recorre la columnas.
        #imagen_rayada[fila_horizontal_mitad_pixeles,i]=1
        if(imagen[fila_horizontal_mitad_pixeles][i]!=0):
            cont1=cont1+1
    print(cont1)#Se imprimen los valores obtenidos en las variables "i" hasta "mcm".    
    
    #Corte a un cuarto de la imagen horizontalmente
    cont2=0
    fila_horizontal_un_cuarto_pixeles=int(fila_horizontal_mitad_pixeles/2)#A fila_horizontal_un_cuarto_pixeles se le asigna el valor de un entero obtenido por la divicion fila_horizontal_mitad_pixeles entre 2.
    for i in range(0,dimenciones[1]):#Ciclo for que recorre la columnas.
        #imagen_rayada[fila_horizontal_un_cuarto_pixeles,i]=1
        if(imagen[fila_horizontal_un_cuarto_pixeles][i]!=0):
            cont2=cont2+1
    print(cont2)#Se imprimen los valores obtenidos en las variables "i" hasta "mcc".

    #Corte a tres cuartos de la imagen horizontalmente
    cont3=0
    fila_horizontal_tres_cuartos_pixeles=int(fila_horizontal_mitad_pixeles+fila_horizontal_un_cuarto_pixeles)#A mc3c (matriz columnas a tres cuartos) se le asigna el valor de un entero optenido por la suma de fila_horizontal_mitad_pixeles mas fila_horizontal_un_cuarto_pixeles.
    for i in range(0,dimenciones[1]):#Ciclo for que recorre la columnas.
        #imagen_rayada[fila_horizontal_tres_cuartos_pixeles,i]=1
        if(imagen[fila_horizontal_tres_cuartos_pixeles][i]!=0):
            cont3=cont3+1
    print(cont3)#Se imprimen los valores obtenidos en las variables "i" hasta "mc3c".
        
#Inicia vertical.
    #Corte a la mitad de la imagen verticalmente
    cont4=0
    columna_vertical_mitad_pixeles=int(dimenciones[1]/2)#A columna_vertical_mitad_pixeles se le asigna el valor de un entero obtenido por la divicion de dimenciones entre 2.
    for i in range(0,dimenciones[0]):#Ciclo for que recorre la columnas.
        #imagen_rayada[i,columna_vertical_mitad_pixeles]=1
        if(imagen[i][columna_vertical_mitad_pixeles]!=0):
            cont4=cont4+1
    print(cont4)#Se imprimen los valores obtenidos en las variables "i" hasta "mfm".

    #Corte a un cuarto de la imagen verticalmente
    cont5=0
    columna_vertical_un_cuarto_pixeles=int(columna_vertical_mitad_pixeles/2)#A columna_vertical_un_cuarto_pixeles se le asigna el valor de un entero obtenido por la divicion fila_vertical_mitad_pixeles entre 2.
    for i in range(0,dimenciones[0]):#Ciclo for que recorre la columnas.
        #imagen_rayada[i,columna_vertical_un_cuarto_pixeles]=1
        if(imagen[i][columna_vertical_un_cuarto_pixeles]!=0):
            cont5=cont5+1
    print(cont5)#Se imprimen los valores obtenidos en las variables "i" hasta "mfc".
    
    #Corte a tres cuartos de la imagen verticalmente
    cont6=0
    columna_vertical_tres_cuartos_pixeles=int(columna_vertical_mitad_pixeles+columna_vertical_un_cuarto_pixeles)#A columna_vertical_tres_cuartos_pixeles se le asigna el valor de un entero obtenido por la suma de columna_vertical_mitad_pixeles mas columna_vertical_un_cuarto_pixeles.
    for i in range(0,dimenciones[0]):#Ciclo for que recorre la columnas.
        #imagen_rayada[i,columna_vertical_tres_cuartos_pixeles]=1
        if(imagen[i][columna_vertical_tres_cuartos_pixeles]!=0):
            cont6=cont6+1
    print(cont6)#Se imprimen los valores obtenidos en las variables "i" hasta "mf3c".
    return cont1,cont2,cont3,cont4,cont5,cont6

#Cambios_En_La_Imagen()
#Se contabiliza el numero de cambios ue sufre la imagen al ser recorrida (ceros y unos)
#Se usa un contador el cual nos permite saber cuando se hace un corte en la imagen.
#En la variable "mc" se obtiene la posición en la imagen mediane la división.
#La variable "x" se usa para comparar.
#La variable "imagen" contiene la matriz de la imagen.

def Cambios_en_la_imagen(imagen,dimenciones):
    #Cambios a la mitad de la imagen horizontalmente
    cont7=0#Se inicializa el contador en cero.
    fila_horizontal_mitad_cortes=int(dimenciones[0]/2)#A la variable fila_horizontal_mitad_cortes se le asigna el valor de la división de dimenciones[0] entre 2.
    x=imagen[fila_horizontal_mitad_cortes,0]#A la variable x se le agrega el valor de las posiciones fila_horizontal_mitad_cortes y 0.
    for i in range(0,dimenciones[1]):#Ciclo for recorre las columnas de la imagen.
        #imagen_rayada[fila_horizontal_mitad_cortes,i]=1
        if (imagen[fila_horizontal_mitad_cortes,i]!=x):#Se hace la comparación de imagen en la posición fila_horizontal_mitad_cortes, i si es diferente de x.
            cont7=cont7+1#Se hace el aumento de la variable si imagen es diferente de x.
            x=imagen[fila_horizontal_mitad_cortes,i]#a la variable x se le asigna el valor de imagen en la posición fila_horizontal_mitad_cortes,i.
    print(cont7)#Se imprime el valor de la variable cont.       
    
    #Cambios a un cuarto de la imagen horizontalmente
    cont8=0#Se inicializa el contador en cero.
    fila_horizontal_un_cuarto_cortes=int(fila_horizontal_mitad_cortes/2)#A la variable fila_horizontal_un_cuarto_cortes se le asigna el valor de la división de fila_horizontal_mitad_cortes entre 2.
    x=imagen[fila_horizontal_un_cuarto_cortes,0]#A la variable x se le agrega el valor de las posiciones mcc y 0.
    for i in range(0,dimenciones[1]):#Ciclo for recorre las columnas de la imagen.
        #imagen_rayada[fila_horizontal_un_cuarto_cortes,i]=1
        if (imagen[fila_horizontal_un_cuarto_cortes,i]!=x):#Se hace la comparación de imagen en la posición fila_horizontal_mitad_cortes, i si es diferente de x.
            cont8=cont8+1#Se hace el aumento de la variable si imagen es diferente de x.
            x=imagen[fila_horizontal_un_cuarto_cortes,i]#a la variable x se le asigna el valor de imagen en la posición fila_horizontal_mitad_cortes,i.
    #print(cont8)#Se imprime el valor de la variable cont.        

    #Cambios a tres cuartos de la imagen horizontalmente
    cont9=0#Se inicializa el contador en cero.
    fila_horizontal_tres_cuartos_cortes=int(fila_horizontal_mitad_cortes+fila_horizontal_un_cuarto_cortes)#A la variable fila_horizontal_un_cuarto_cortes se le asigna el valor de la suma de fila_horizontal_mitad_cortes mas fila_horizontal_tres_cuartos_cortes para obtener la posicion en tres cuartos.
    x=imagen[fila_horizontal_tres_cuartos_cortes,0]#A la variable x se le agrega el valor de las posiciones fila_horizontal_tres_cuartos_cortes y 0.
    for i in range(0,dimenciones[1]):#Ciclo for recorre las columnas de la imagen.
        #imagen_rayada[fila_horizontal_tres_cuartos_cortes,i]=1
        if (imagen[fila_horizontal_tres_cuartos_cortes,i]!=x):#Se hace la comparación de imagen en la posición fila_horizontal_tres_cuartos_cortes, i si es diferente de x.
            cont9=cont9+1#Se hace el aumento de la variable si imagen es diferente de x.
            x=imagen[fila_horizontal_un_cuarto_cortes,i]#a la variable x se le asigna el valor de imagen en la posición fila_horizontal_tres_cuartos_cortes,i.
    print(cont9)#Se imprime el valor de la variable cont.

#Comienzan verticales

    #Cambios a la mitad de la imagen verticalmente
    cont11=0#Se inicializa el contador en cero.
    columna_vertical_mitad_cortes=int(dimenciones[1]/2)#A la variable columna_vertical_mitad_cortes se le asigna el valor de la división de dimenciones[1] entre 2.
    x=imagen[columna_vertical_mitad_cortes,0]#A la variable x se le agrega el valor de las posiciones columna_vertical_mitad_cortes y 0.
    for i in range(0,dimenciones[0]):#Ciclo for recorre las columnas de la imagen.
        #imagen_rayada[i,columna_vertical_mitad_cortes]=1
        if (imagen[i,columna_vertical_mitad_cortes]!=x):#Se hace la comparación de imagen en la posición columna_vertical_mitad_cortes,i si es diferente de x.
            cont11=cont11+1#Se hace el aumento de la variable si imagen es diferente de x.
            x=imagen[i,columna_vertical_mitad_cortes]#a la variable x se le asigna el valor de imagen en la posición i,columna_vertical_mitad_cortes.
    print(cont11)#Se imprime el valor de la variable cont.    
    
    #Cambios a un cuarto de la imagen verticalmente
    cont10=0#Se inicializa el contador en cero.
    columna_vertical_un_cuarto_cortes=int(columna_vertical_mitad_cortes/2)#A la variable columna_vertical_un_cuarto_cortes se le asigna el valor de la división de columna_vertical_mitad_cortes entre 2.
    x=imagen[columna_vertical_un_cuarto_cortes,0]#A la variable x se le agrega el valor de las posiciones mfc y 0.
    for i in range(0,dimenciones[0]):#Ciclo for recorre las columnas de la imagen.
        #imagen_rayada[i,mf]=1
        if (imagen[i,columna_vertical_un_cuarto_cortes]!=x):#Se hace la comparación de imagen en la posición mfc,i si es diferente de x.
            cont10=cont10+1#Se hace el aumento de la variable si imagen es diferente de x.
            x=imagen[i,columna_vertical_un_cuarto_cortes]#a la variable x se le asigna el valor de imagen en la posición i,mfc.
    print(cont10)#Se imprime el valor de la variable cont.

    #Cambios a tres cuartos de la imagen verticalmente
    cont12=0#Se inicializa el contador en cero.
    columna_vertical_tres_cuartos_cortes=int(columna_vertical_mitad_cortes+columna_vertical_un_cuarto_cortes)#A la variable columna_vertical_tres_cuartos_cortes se le asigna el valor de la suma de columna_vertical_mitad_cortes mas columna_vertical_un_cuarto_cortes para obtener la posicion en tres cuartos.
    x=imagen[columna_vertical_tres_cuartos_cortes,0]#A la variable x se le agrega el valor de las posiciones columna_vertical_tres_cuartos_cortes y 0.
    for i in range(0,dimenciones[0]):#Ciclo for recorre las columnas de la imagen.
        #imagen_rayada[i,columna_vertical_tres_cuartos_cortes]=1
        if (imagen[i,columna_vertical_tres_cuartos_cortes]!=x):#Se hace la comparación de imagen en la posición columna_vertical_tres_cuartos_cortes,i si es diferente de x.
            cont12=cont12+1#Se hace el aumento de la variable si imagen es diferente de x.
            x=imagen[i,columna_vertical_tres_cuartos_cortes]#a la variable x se le asigna el valor de imagen en la posición i,columna_vertical_tres_cuartos_cortes.
    print(cont12)#Se imprime el valor de la variable cont.    

    #imagenplot = plt.imshow(imagen_rayada)#La variable imagenplot sirve para imprimir la imagen previamente cargada.

    return cont7,cont8,cont9,cont10,cont11,cont12

#Escritura_CSV
#Escribe en el archivo csv que se creo previamente con los datos obtenidos de la imagen
#como son los cortes, los cambios, etc.
#Se lee la imagen
def Escritura_CSV():
    archivo_CSV=open('DataSet.csv','w', newline='')#Se abre un archivo csv y se indica la escritura del mismo.
    salida_CSV= csv.writer(archivo_CSV)#Se transfiere un archivo a la variable "salida".
    clase=-1
    contador=0
    carpeta='imagenes'
    for path, ficheros, archivos in os.walk(carpeta):
        for fname in archivos:
            nombre=path+'/'+fname
            imagen = mpimagen.imread(nombre)#Se importa la imagen a la variable.
            #imagen_rayada = mpimagen.imread(nombre)#Se importa la imagen a la variable.
            dimenciones=Calcular_dimenciones(imagen)
            razon=Razon(dimenciones)
            pixeles_blancos=Pixeles_blancos(imagen,dimenciones)
            cont1,cont2,cont3,cont4,cont5,cont6=Numero_De_Bits_Que_Representan_La_Imagen(imagen,dimenciones)
            cont7,cont8,cont9,cont10,cont11,cont12=Cambios_en_la_imagen(imagen,dimenciones)
            salida_CSV.writerow([razon,pixeles_blancos,cont1,cont2,cont3,cont4,cont5,cont6,cont7,cont8,cont9,cont10,cont11,cont12,clase])
            contador=contador+1
        clase=clase+1
    archivo_CSV.close()

Escritura_CSV()