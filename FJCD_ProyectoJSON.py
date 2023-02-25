from funciones import menu,listarPokemon,TotalPokemonTipos,BuscarPorTipoPeso,BuscarEvolucionDebilidades,BuscarEvolucionConAlturaPesoyTipo
import json
opcion_elegida=0

with open('pokedex.json', 'r') as pokedex:
    lista_pokemon = json.load(pokedex)

    # print(lista_juegos['pokemon'])
    # for i in lista_juegos['pokemon']:
    #     print(i['id'])  


while opcion_elegida != 6 :
    #Menu para elegir opccion
    opcion_elegida=menu()
    
    # 1. Lista los nombres de los pokemons y el numero de id en la pokedex
    if opcion_elegida == 1:
        listarPokemon(lista_pokemon)
    # 2. Muestra el total de pokemons de un determinado tipo (El usuario lo introduce)
    elif opcion_elegida == 2:
        TotalPokemonTipos(lista_pokemon)
    # 3. Pide al usuario el tipo de un pokemon y un limite superior en el peso . Mostrandote una lista de los nombrs que cumplen la condicion 

    elif opcion_elegida == 3:
        BuscarPorTipoPeso(lista_pokemon)
    # 4. Introduciendo el id de un poquemon te busque su siguiente evoluciones y te indique su nombre y sus debilidades 
    elif opcion_elegida == 4:
        BuscarEvolucionDebilidades(lista_pokemon)
    # 5. Pide la altura , peso y tipo mostrandote el nombre de los que cumplan las tres condiciones y el nombre de sus evoluciones si es que las tiene
    elif opcion_elegida == 5:
        BuscarEvolucionConAlturaPesoyTipo(lista_pokemon)
        
# 1. Lista los nombres de los pokemons y el numero de id en la pokedex
# 2. Muestra el total de pokemons de un determinado tipo (El usuario lo introduce)
# 3. Pide al usuario el tipo de un pokemon y un limite superior en el peso . Mostrandote una lista de los nombrs que cumplen la condicion 
# 4. Introduciendo el id de un poquemon te busque su siguiente evoluciones y te indique su nombre y sus debilidades 
# 5. Pide la altura , peso y tipo mostrandote el nombre de los que cumplan las tres condiciones y el nombre de sus evoluciones si es que las tiene
