import json
import requests

from Punto1 import Arreglo
from Punto2 import Expresion
from ConsumoAPI import *

if __name__ == '__main__':
    punto1 = Arreglo()
    punto2 = Expresion()
    consumo_api = CONSUMO_API()
    punto1.run()
    input('Enter para ejercicios punto 2. ')
    punto2.run()
    input('Enter para Consmo API por consola. ')
    consumo_api.run()
