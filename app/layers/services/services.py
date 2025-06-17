# capa de servicio/lógica de negocio

from ..transport import transport
from ...config import config
from ..persistence import repositories
from ..utilities.translator import fromRequestIntoCard 
#Importo la función from request into card
from django.contrib.auth import get_user

# función que devuelve un listado de cards. Cada card representa una imagen de la API de Pokemon
def getAllImages():
    
    # Obtiene todas las imágenes de pokemones usando transport.getAllImages()
    pokemon_data=transport.getAllImages()
    cartas=[]
    
    
    # Itera sobre cada pokemon en la lista de pokemones
    for pokemon in pokemon_data:
        
        # Agrega cada pokemon a la lista de cartas
        #Llamo a la función para convertir el json en una card
        cartas.append(fromRequestIntoCard(pokemon))

    # Retorna la lista completa de cartas después de procesar todos los pokemones
    return cartas

    # 1) traer un listado de imágenes crudas desde la API (ver transport.py)
    # 2) convertir cada img. en una card.
    # 3) añadirlas a un nuevo listado que, finalmente, se retornará con todas las card encontradas.




# función que filtra según el nombre del pokemon.
def filterByCharacter(name):
    # guarda la lista entera de pokemones en all_cards
    all_cards = getAllImages()
    
    # armamos una lista vacía para ser llenada con los pokemons
    filtered_cards = []

    # message con un string vacío, se asignará 'No se encuentra el pokemon' si no se encuentran resultados
    message = ''

    # si no se ingresa un nombre, devuelve todas las cartas
    if len(name) == 0:
        return all_cards, message
    
    # recorremos la variable all_cards
    for current_card in all_cards:
        # si hay un nombre y está en la carta, se encontró un resultado
        if len(name) > 0 and name.lower() in current_card.name.lower():
            # agregamos la carta a filtered_cards
            filtered_cards.append(current_card)

    # si el resultado es 0 es porque no se encontraron resultados
    if len(filtered_cards) == 0:
        # cambiamos el mensaje a "No se encuentra el pokemon"
        message = "No se encuentra el pokemon"
    # devolvemos las cartas y el mensaje, que será 'No se encuentra el pokemon' si no hay resultados
    return filtered_cards, message
    
    



# función que filtra las cards según su tipo.
def filterByType(type_filter):
    filtered_cards = []

    for card in getAllImages():
        # debe verificar si la casa de la card coincide con la recibida por parámetro. Si es así, se añade al listado de filtered_cards.
        filtered_cards.append(card)

    return filtered_cards

# añadir favoritos (usado desde el template 'home.html')
def saveFavourite(request):
    fav = '' # transformamos un request en una Card (ver translator.py)
    fav.user = get_user(request) # le asignamos el usuario correspondiente.

    return repositories.save_favourite(fav) # lo guardamos en la BD.

# usados desde el template 'favourites.html'
def getAllFavourites(request):
    if not request.user.is_authenticated:
        return []
    else:
        user = get_user(request)

        favourite_list = [] # buscamos desde el repositories.py TODOS Los favoritos del usuario (variable 'user').
        mapped_favourites = []

        for favourite in favourite_list:
            card = '' # convertimos cada favorito en una Card, y lo almacenamos en el listado de mapped_favourites que luego se retorna.
            mapped_favourites.append(card)

        return mapped_favourites

def deleteFavourite(request):
    favId = request.POST.get('id')
    return repositories.delete_favourite(favId) # borramos un favorito por su ID

#obtenemos de TYPE_ID_MAP el id correspondiente a un tipo segun su nombre
def get_type_icon_url_by_name(type_name):
    type_id = config.TYPE_ID_MAP.get(type_name.lower())
    if not type_id:
        return None
    return transport.get_type_icon_url_by_id(type_id)