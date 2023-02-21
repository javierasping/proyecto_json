#MENU
def menu():
    print("---------------------------------------")
    opcion_elegida=int(input('''
    1. Lista los nombres de los pokemons y el numero de id en la pokedex
    2. Muestra el total de pokemons de un determinado tipo (El usuario lo introduce)
    3. Pide al usuario el tipo de un pokemon y un limite superior en el peso . Mostrandote una lista de los nombrs que cumplen la condicion 
    4. Introduciendo el id de un poquemon te busque sus evoluciones y te indique su nombre y sus debilidades 
    5. Pide la altura , peso y tipo mostrandote el nombre de los que cumplan las tres condiciones y el nombre de sus evoluciones si es que las tiene
    6. Salir
    '''))
    print("---------------------------------------")

    return opcion_elegida

# 1. Lista todos los nombres de los pokemons y el numero de id en la pokedex
def listarPokemon(lista_pokemon):
    for i in lista_pokemon['pokemon']:
        print(i['id'], i['name'],)  

# 2. Muestra el total de pokemons de un determinado tipo (El usuario lo introduce)
def TotalPokemonTipos(lista_pokemon):
    print("Los tipos de pokemos que existen son Bug, Dragon, Electric, Fighting, Fire, Flying, Ghost, Grass, Ground, Ice, Normal, Poison, Psychic, Rock, and Water.")
    tipo_a_buscar=input("Introduce el tipo de pokemon que deseas buscar ")
    for i in lista_pokemon['pokemon']:
        for tipo in i['type']:
            if tipo == tipo_a_buscar:
             print(i['id'], i['name'],)  

# 3. Pide al usuario el tipo de un pokemon y un limite superior en el peso . Mostrandote una lista de los nombrs que cumplen la condicion 
def BuscarPorTipoPeso(lista_pokemon):
    print("Los tipos de pokemos que existen son Bug, Dragon, Electric, Fighting, Fire, Flying, Ghost, Grass, Ground, Ice, Normal, Poison, Psychic, Rock, and Water.")
    tipo_a_buscar=input("Introduce el tipo de pokemon que deseas buscar ")
    Limite_sup_peso=input("Introduce el limite superior de peso que desea  : ")
    for i in lista_pokemon['pokemon']:
        for tipo in i['type']:
            if tipo == tipo_a_buscar:
                peso = i["weight"].split()[0]
                if peso > Limite_sup_peso:
                     print(i['id'], i['name'],)  


                    #  weight_str = pokemon["weight"]  # Acceder al valor de la clave "weight"
                    # weight_int = int(weight_str.split()[0])  # Convertir de cadena a entero
                    # print(weight_int)  # Imprimir el peso como entero
# 4. Introduciendo el id de un poquemon te busque sus evoluciones y te indique su nombre y sus debilidades 
# 5. Pide la altura , peso y tipo mostrandote el nombre de los que cumplan las tres condiciones y el nombre de sus evoluciones si es que las tiene