


'''La empresa de eSports “eShirlitos”, necesita desarrollar un sistema que permita registrar los puntajes obtenidos por sus competidores en Fortnite, Valorant y Fifa. Para el funcionamiento del sistema se requiere las siguientes funcionalidades
1.
Registrar puntajes torneo
2.
Listar los todos puntajes
3.
Imprimir por Tipo 
4.
Salir del programa'''
listadepuntaje={}
EXPERTO=[]
AVANZADO=[]
PRINCIPIANTE=[]
def registro():

    idjugador=input('Ingresa tu ID de jugador')
    listadepuntaje['Id Jugador']=idjugador
    nombre=input('Nombre y apellido')
    listadepuntaje['Nombre']=nombre
    
    juego=input('Ingresa el juego VALORANT/FORNITE/FIFA').upper()


    #Elecció del juego
    if juego=='VALORANT' or juego=='FORNITE' or juego=='FIFA': 
    

        if juego=='VALORANT':
            puntaje=int(input('Escribe tu puntaje'))
            listadepuntaje['VALORANT']=puntaje
            


        if juego=='FORNITE':
            puntaje=int(input('Escribe tu puntaje'))
            listadepuntaje['VALORANT']=puntaje
            

        if juego=='FIFA': 
            puntaje=int(input('Escribe tu puntaje'))  
            listadepuntaje['VALORANT']=puntaje


      
    else:
        print('Juego no disponible')

'''Listar puntajes

Debe mostrar en la pantalla la lista de todos los puntajes registrados, similar al ejemplo anterior (opción 1).'''

def listadepuntajes():
    if len(listadepuntaje)>=1:
        print(listadepuntaje)
    else:
        print('No hay registros')


'''Para imprimir por tipo, el usuario debe seleccionar alguno de los 3 tipos (Principiante - Avanzado - Experto). 
Estos tipos deben estar previamente definidos en algún tipo de colección de Python en el código.
Al seleccionar uno de los tipos, se generará un archivo de texto (.txt) con el detalle de los puntajes obtenidos 
por los jugadores del tipo seleccionado. Este debe tener la misma forma del registro completo de las opciones anteriores, 
pero en archivo de texto.
Cada opción de la aplicación debe desarrollarse en una función que debe llamarse desde el programa principal.'''

def imprimirportipo():
    eleccion=''
    print('Seleccione una de las opciones siguientes')
    eleccion=int(input('''1.-Principiante - 2.-Avanzado - 3-Experto
    >'''))
    if eleccion==1 or eleccion==2 or eleccion==3:
        if eleccion==1:
            with open('Puntaje-Principiante.txt','w') as archivo:
                archivo.write(listadepuntaje)
        if eleccion=='2':
            
            with open('Puntaje-Avanzado.txt','w') as archivo:
                archivo.write(listadepuntaje)
        if eleccion=='3':

            with open('Puntaje-Experto.txt','w') as archivo:
                archivo.write(listadepuntaje)
            
            
    else:
        print('Opción no existe')



def menu():
    op=0
    while True:
        print('''
        1.-Registrar puntajes torneo
        2.-Listar los todos puntajes
        3.-Imprimir por Tipo
        4.-Salir del programa''')
        try:
            op=int(input(''''Elige tu opción
            >'''))
            if op>=1 and op<=4:
                if op==1:
                    registro()
                if op==2:
                    listadepuntajes()
                if op==3:
                    imprimirportipo()
                if op==4:
                    print('Hasta pronto')
                    break
            else:
                print('Opción fuera de rango')

        except:
            print('Opción debe ser un numero ')
            

