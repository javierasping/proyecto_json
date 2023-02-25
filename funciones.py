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



# 4. Introduciendo el id de un poquemon te busque su siguiente evoluciones y te indique su nombre y sus debilidades 
def BuscarEvolucionDebilidades(lista_pokemon):
    id_a_buscar=input("Introduce el id del pokemon que desea buscar: ")
    for i in lista_pokemon['pokemon']:
        if int(id_a_buscar) == int(i['id']):
           print("El id que ha introducido corresponde a ", i['name'],)
           pokemon_buscado=i
           if 'next_evolution' in pokemon_buscado :  
            for siguiente_evolucion in i['next_evolution'] :
                    print(40*'*')
                    print (siguiente_evolucion['name'], "y sus debilidades son : ")
                    for debilidades in lista_pokemon['pokemon']:
                        if siguiente_evolucion['name'] == debilidades['name']:
                                for weaknesses in debilidades['weaknesses']:
                                    print(weaknesses)
           else:
                print("El pokemon que has introducido no tiene evoluciones")

  




# 5. Pide la altura , peso y tipo mostrandote el nombre de los que cumplan las tres condiciones y el nombre de sus evoluciones si es que las tiene
