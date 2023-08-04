import requests

##URL base 
BASE_URL = 'https://api.chucknorris.io/jokes/'

## Funcion creada para trart el chiste, uso el url base en base_url y en cada funcion agrego el parametro nuevo que necesite 
##Para este agrego el parametro random 
def chiste_chuck_norris():
    response = requests.get(BASE_URL + 'random')
    if response.status_code == 200:
        data = response.json()
        return data['value']
    else:
        return "Chiste no dispobible."

##Para este agrego el parametro categories 
def categorias():
    response = requests.get(BASE_URL + 'categories')
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return []

##Para este agrego el parametro categories random?category= y la opcion de la categoria que es seleccionada. 
def chiste_categoria(category):
    response = requests.get(BASE_URL + 'random?category=' + category)
    if response.status_code == 200:
        data = response.json()
        return data['value']
    else:
        return "Chiste no dispobible."


def display_categories(categories):
    print("\nCategorias:")
    for category in categories:
        print(f"- {category}")

## abro un while infinito en donde creo un meny y llamo las funciones de arriba. 
while True:
    print("\n Seleccione un numero:")
    print("1. Chiste de Chuck Norris")
    print("2. Ver categorias de chistes")
    print("3. Obtener un chiste por categoria")
    print("4. Salir")

    opcion = input("Elija una opcion (1, 2, 3 o 4): ")

    if opcion == '1':
        chiste = chiste_chuck_norris()
        print("\nChiste de Chuck Norris:")
        print(chiste)

    elif opcion == '2':
        categories = categorias()
        display_categories(categories)

    elif opcion == '3':
        category = input("\nIngrese la categoria deseada: ")
        chiste = chiste_categoria(category)
        print(f"Chiste de Chuck Norris de la categoria '{category}':")
        print(chiste)

    elif opcion == '4':
        print("Gracias por usar mi programa, adios.")
        break

    else:
        print("Opcion invalida. Obciones validas: 1, 2, 3 o 4.")


