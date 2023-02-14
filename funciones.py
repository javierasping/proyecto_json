#Leer fichero ej2 

def leerfichero(fichero_a_leer):
    liga_baloncesto=[]
    for entrada in fichero_a_leer:
       valor = entrada.split(',')

       partido = {
           'fecha_partido': valor[0],
          'equipo_local': valor[1],
          'equipo_visitante': valor[2],
         'puntos_local': int(valor[3]),
         'puntos_visitante': int(valor[4])
         }
    
    liga_baloncesto.append(partido)
    return (liga_baloncesto)


#MENU
def menu():
    print("---------------------------------------")
    opcion_elegida=int(input('''
    1. Añadir partido
    2. Buscar el resultado de un partido
    3. Eliminar partido
    4. Listar nombres de los equipos
    5. Estadística de un equipo
    6. Salir
    ************ Examen *****************
    7.Modificar resultado de un partido
    8.Listar equipos en una determinada fecha
    9.Eliminar todos los partidos de una fecha 
    '''))
    print("---------------------------------------")

    return opcion_elegida


#AÑADIR PARTIDO
def añadir_partido():
        fecha=input("Fecha del partido ")
        nombre_e_local=input("Nombre del equipo local ")
        nombre_e_visitante=input("Nombre del equipo visitante ")
        puntos_e_local=int(input("Puntos del equipo local "))
        puntos_e_visitante=int(input("Puntos del equipo visitante "))
        partido = {
        'fecha_partido': fecha,
        'equipo_local': nombre_e_local,
        'equipo_visitante': nombre_e_visitante,
        'puntos_local': puntos_e_local,
        'puntos_visitante': puntos_e_visitante
    }

        return partido


#BUSCAR PARTIDO
def buscar_partido(liga_baloncesto):
    fecha_a_buscar= input("Ingresa la fecha del partido (formato dd/mm/yyyy): ")
    equipo_local_a_buscar = input("Ingresa el equipo local: ")
    equipo_encontrado=False
    for partido in liga_baloncesto:
        if partido['fecha_partido'] == fecha_a_buscar and partido['equipo_local'] == equipo_local_a_buscar:
                    equipo_encontrado=True
                    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                    print("La busqueda a sido exitosa , el resultado del partido fue :")
                    print("--> Equipo Local marco " ,partido['puntos_local'])
                    print("--> Equipo Visitante marco " ,partido['puntos_visitante'])

    if equipo_encontrado==False :
            print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
            print("No se ha encontrado ningun resultado")

#ELIMINAR PARTIDO            
def eliminar_partido(liga_baloncesto):
    equipo_local_a_buscar = input("Ingresa el equipo local: ")
    equipo_visitante_a_buscar = input("Ingresa el equipo visitante: ")

    equipo_encontrado=False
    for partido in liga_baloncesto:
        if partido['equipo_local'] == equipo_local_a_buscar and partido['equipo_visitante'] == equipo_visitante_a_buscar:
                    equipo_encontrado=True
                    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                    print("El partido se eliminara...")
                    liga_baloncesto.remove(partido)

    if equipo_encontrado==False :
            print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
            print("No se ha encontrado ningun partido")

    return liga_baloncesto

# LISTAR EQUIPOS 
def listar_equipos(liga_baloncesto):
    lista_equipos = set()
    for partido in liga_baloncesto:
        lista_equipos.add(partido['equipo_local'])
        lista_equipos.add(partido['equipo_visitante'])
    for equipo in lista_equipos:
        print(equipo)
    return lista_equipos


#estadisticas
def estadisticas(liga_baloncesto):
    equipo_a_buscar=input("Introduce el equipo que quieres ver sus estadisticas :")
    puntos = 0
    partidos_ganados = 0
    partidos_perdidos = 0
    partidos_empatados = 0
    equipo_encontrado=False
    # Si el equipo es el local
    for equipo in liga_baloncesto:
          
        if equipo["equipo_local"] == equipo_a_buscar:
            equipo_encontrado=True
            puntos=puntos+ equipo["puntos_local"]
            if equipo["puntos_local"] > equipo["puntos_visitante"] :
                    partidos_ganados= partidos_ganados + 1
            if equipo["puntos_local"] == equipo["puntos_visitante"] :
                    partidos_empatados= partidos_empatados + 1                
            if equipo["puntos_local"] < equipo["puntos_visitante"] :
                    partidos_perdidos= partidos_perdidos + 1
            
    # Si el equipo es el visitante

    for equipo in liga_baloncesto:
        if equipo["equipo_visitante"] == equipo_a_buscar:
            equipo_encontrado=True
            puntos=puntos+ equipo["puntos_visitante"]
            if equipo["puntos_local"] < equipo["puntos_visitante"] :
                    partidos_ganados= partidos_ganados + 1
            if equipo["puntos_local"] == equipo["puntos_visitante"] :
                    partidos_empatados= partidos_empatados + 1                
            if equipo["puntos_local"] > equipo["puntos_visitante"] :
                    partidos_perdidos= partidos_perdidos + 1
    
    if equipo_encontrado == True:
        print("Partidos ganados : ",partidos_ganados)
        print("Partidos perdidos : ",partidos_perdidos)
        print("Partidos empatados : ",partidos_empatados)
        print("Puntos marcados : ",puntos)
    else:
        print("No se ha encontrado datos de ese equipo")
