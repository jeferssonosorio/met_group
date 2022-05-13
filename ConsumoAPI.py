import os
import requests

URL = 'https://test-api-met.herokuapp.com'
HEADERS = {'content-type': 'application/json'}
CREAR_USUARIO = '/register'
LOGUEARSE = '/auth'
TIENDA = '/store/'
LISTA_TIENDAS = '/stores'
ARTICULO = '/item/'
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

            if opcionMenu == "1":
                data = {}
                print("")
                data['username'] = input("Inserte usuario: ")
                data['password'] = input("Contraseña: ")
                print(data)
                respuesta = requests.post(url=URL + CREAR_USUARIO, headers=HEADERS, json=data)
                print(respuesta.json())
                input('pulsa una tecla para continuar')

            elif opcionMenu == "2":
                data = {}
                print("")
                data['username'] = input("Inserte usuario: ")
                data['password'] = input("Contraseña: ")
                respuesta = requests.post(url=URL + LOGUEARSE, headers=HEADERS, json=data)
                print(respuesta.json())
                if respuesta.status_code == 200:
                    token = respuesta.json()['access_token']
                input('pulsa una tecla para continuar')

            elif opcionMenu == "3":
                if not token:
                    input("Primero debe loguearse. ")
                else:
                    print(SUB_MENU)
                    opcionSubMenu = input("Inserte su opción: ")

                    if opcionSubMenu == '1':
                        HEADERS.update({'authorization': 'JWT ' + token})
                        respuesta = requests.get(url=URL + LISTA_TIENDAS, headers=HEADERS, )
                        print(respuesta.json())
                        input('pulsa una tecla para continuar')
                    elif opcionSubMenu == '2':
                        pass
                    elif opcionSubMenu == '3':
                        pass
                    elif opcionSubMenu == '4':
                        pass
                    elif opcionSubMenu == '5':
                        pass
                    input()

            elif opcionMenu == "4":
                if not token:
                    input("Primero debe loguearse. ")
                print(SUB_MENU)
                opcionSubMenu = input("Inserte su opción: ")
                input()

            elif opcionMenu == "5":
                print("Saliendo.....")
                break

            else:
                print("")
                input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")
