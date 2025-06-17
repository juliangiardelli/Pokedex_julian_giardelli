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




def filterByCharacter(name):
    # Define una función que acepta un parámetro 'name' para filtrar tarjetas según su nombre.
    filtered_cards = []
    # Crea una lista vacía para almacenar las tarjetas que coincidan con el criterio de búsqueda.
    name = name.strip().lower()
    # Normaliza el parámetro 'name' convirtiéndolo a minúsculas y eliminando espacios, para evitar.
    if len(name) == 0:
        # Si el parámetro 'name' está vacío, retorna una lista vacía.
        return filtered_cards
    
    cards = list(getAllImages())
    # Convierte el resultado de 'getAllImages()' en una lista de objetos Card.
    for i in range(len(cards)):
        # Itera sobre los índices de la lista de tarjetas para acceder a cada objeto Card.
        card = cards[i]
        # Obtiene el objeto Card en el índice actual.
        if card.name and card.name.lower().find(name) >= 0:
            # Comprueba si el atributo 'name' existe y si el parámetro 'name' es una subcadena, ignorando mayúsculas y minúsculas.
            filtered_cards.append(card)
            # Añade la tarjeta a la lista 'filtered_cards' si satisface la condición de búsqueda.
    
    return filtered_cards
    # Devuelve la lista 'filtered_cards' con todas las tarjetas cuyo atributo 'name' contiene el parámetro 'name'.

# función que filtra las cards según su tipo.
def filterByType(type_filter):
    # Define una función que acepta un parámetro 'type_filter' para filtrar tarjetas según su tipo.
    filtered_cards = []
    # Normaliza el parámetro 'type_filter' convirtiéndolo a minúsculas y eliminando espacios.
    type_filter = type_filter.lower().strip()
    # Si la longitud del parámetro 'type_filter' es cero, retorna una lista vacía.
    if len(type_filter) > 0:
        for card in getAllImages():
            # Verifica si el atributo 'type' de la tarjeta existe y si 'type_filter' está contenido en él.
            if card.types and any(type_filter in str(item).lower() for item in card.types):
                # Añade la tarjeta a la lista 'filtered_cards' si el tipo coincide.
                filtered_cards.append(card)
    
    return filtered_cards
    # Devuelve la lista 'filtered_cards' con todas las tarjetas cuyo atributo 'type' contiene el parámetro 'type_filter'.
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