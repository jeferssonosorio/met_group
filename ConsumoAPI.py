import requests

URL = 'https://test-api-met.herokuapp.com'
HEADERS = {'content-type': 'application/json'}
CREAR_USUARIO = '/register'
LOGUEARSE = '/auth'
TIENDA = '/store/'
LISTA_TIENDAS = '/stores'
ITEM = '/item/'
LISTA_ITEMS = '/items'

MENU = """
        MENÚ
1) Registrarse
2) Loguearse
3) Tiendas
4) Items
5) salir

"""

SUB_MENU = """
        MENÚ
1) Ver lista
2) Ver uno
3) Crear
4) Eliminar
5) Actualizar

"""


class CONSUMO_API:

    def run(self):
        token = ''
        while True:

            print(MENU)
            opcionMenu = input("Inserte su opción ")

            #Menú Inicio Sesión
            if opcionMenu == "1":
                data = {}
                print("")
                data['username'] = input("Inserte usuario: ")
                data['password'] = input("Contraseña: ")
                print(data)
                respuesta = requests.post(url=URL + CREAR_USUARIO, headers=HEADERS, json=data)
                print(respuesta.json())
                input('pulsa una tecla para continuar. ')

            # Menú Loggeo
            elif opcionMenu == "2":
                data = {}
                print("")
                data['username'] = input("Inserte usuario: ")
                data['password'] = input("Contraseña: ")
                respuesta = requests.post(url=URL + LOGUEARSE, headers=HEADERS, json=data)
                print(respuesta.json())
                if respuesta.status_code == 200:
                    token = respuesta.json()['access_token']
                    HEADERS.update({'authorization': 'JWT ' + token})
                input('pulsa una tecla para continuar. ')

            # Menú Tiendas
            elif opcionMenu == "3":
                if not token:
                    input("Primero debe loguearse. \nEnter para continuar. ")
                else:
                    print(SUB_MENU)
                    opcionSubMenu = input("Inserte su opción: ")

                    #Ver todos
                    if opcionSubMenu == '1':
                        respuesta = requests.get(url=URL + LISTA_TIENDAS, headers=HEADERS)
                        print(respuesta.json())
                        input('pulsa una tecla para continuar. ')

                    #Ver uno
                    elif opcionSubMenu == '2':
                        id = input('Ingrese el id de la tienda. ')
                        respuesta = requests.get(url=URL + TIENDA + id, headers=HEADERS)
                        print(respuesta.json())
                        input('pulsa una tecla para continuar. ')

                    # Crear
                    elif opcionSubMenu == '3':
                        nombre = input('Ingrese el nombre de la tienda. ')
                        respuesta = requests.post(url=URL + TIENDA + nombre, headers=HEADERS)
                        print(respuesta.json())
                        input('pulsa una tecla para continuar. ')

                    # Eliminar
                    elif opcionSubMenu == '4':
                        nombre = input('Ingrese el nombre de la tienda. ')
                        respuesta = requests.delete(url=URL + TIENDA + nombre, headers=HEADERS)
                        print(respuesta.json())
                        input('pulsa una tecla para continuar. ')

                    # Actualizar
                    elif opcionSubMenu == '5':
                        input('No es posible acutalizar Tiendas. \nPulsa una tecla para continuar. ')

            # Menú artículos
            elif opcionMenu == "4":
                if not token:
                    input("Primero debe loguearse. \nEnter para continuar. ")
                else:
                    print(SUB_MENU)
                    opcionSubMenu = input("Inserte su opción: ")

                    # Ver todos
                    if opcionSubMenu == '1':
                        respuesta = requests.get(url=URL + LISTA_ITEMS, headers=HEADERS)
                        print(respuesta.json())
                        input('pulsa una tecla para continuar. ')

                    # Ver uno
                    elif opcionSubMenu == '2':
                        nombre = input('Ingrese el nombre del artículo. ')
                        respuesta = requests.get(url=URL + ITEM + nombre, headers=HEADERS)
                        print(respuesta.json())
                        input('pulsa una tecla para continuar. ')

                    #Crear
                    elif opcionSubMenu == '3':
                        nombre = input('Ingrese el nombre del artículo. ')
                        data = {'store_id': input('Ingrese el id de la tienda. '),
                                'price': input('Ingrese el precio del artículo. ')}
                        respuesta = requests.post(url=URL + ITEM + nombre, headers=HEADERS, json=data)
                        print(respuesta.json())
                        input('pulsa una tecla para continuar. ')

                    #Eliminar
                    elif opcionSubMenu == '4':
                        nombre = input('Ingrese el nombre del artículo. ')
                        respuesta = requests.delete(url=URL + ITEM + nombre, headers=HEADERS)
                        print(respuesta.json())
                        input('pulsa una tecla para continuar. ')

                    #Actualizar
                    elif opcionSubMenu == '5':
                        nombre = input('Ingrese el nombre del artículo. ')
                        data = {'store_id': input('Ingrese el id de la tienda. '),
                                'price': input('Ingrese el precio del artículo. ')}
                        respuesta = requests.put(url=URL + ITEM + nombre, headers=HEADERS)
                        print(respuesta.json())
                        input('pulsa una tecla para continuar. ')

            elif opcionMenu == "5":
                print("Saliendo.....")
                break

            else:
                print("")
                input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar. ")
