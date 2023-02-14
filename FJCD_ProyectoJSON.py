from funciones import huevo


import json


with open('pokedex.json', 'r') as pokedex:
    lista_juegos = json.load(pokedex)

    # print(lista_juegos['pokemon'])
    for i in lista_juegos['pokemon']:
        print(i['id'])  

# Debes buscar en internet un fichero JSON del cual vas a extraer información. Intenta buscar un fichero con contenido real, 
# que no sea un ejemplo. Busca un fichero relacionado con algún tema que te interese.
# Crea un enunciado, donde indiques la información que vas a extraer. Tienes que hacer cinco funciones en cada ejercicio para extraer información:

# Listar información: Hacer un ejercicio que liste cierta información. Por ejemplo, “lista de provincias”,”lista los títulos de libros, año de publicación y precio”,…
# Contar información: Hacer un ejercicio que muestre el total de veces que aparece una información. Por ejemplo, “lista de provincias y el total de municipios que tiene cada una”, “¿Cuántos libros hay en la biblioteca?”,”mostrar los libros y el número de autores de cada uno”,…
# Buscar o filtrar información: Pedir por teclado uno o varios datos y utilizarlos para hacer una búsqueda, por ejemplo: “Mostrar provincias que empiecen por una subcadena”,”Mostrar libros cuyo precio este entre un valor inicial y otro final”,…
# Buscar información relacionada: Es decir me pide buscar una información, pero muestra información relacionada a ella. Por ejemplo: “Pide por teclado un autor y muestra los libros que ha escrito”,”Pide un municipio y muestra la provincia a la que pertenece”,…
# Ejercicio libre, piensa un tipo de ejercicio que sea diferente a los anteriores o una mezcla de alguno de ellos.