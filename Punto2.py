import re


class Expresion:
    """
    Clase para ejercicios del punto 2
    """

    def run(self):
        a = "Hello world"
        b = "2 + 10 / 2 - 20"
        c = "(2 + 10) / 2 - 20"
        d = "(2 + 10 / 2 - 20"
        pruebas_punto2 = [a, b, c, d]

        punto2 = Expresion()

        for elemento in pruebas_punto2:
            print('Punto 1: {}'.format(punto2.operation(elemento)))
        print()

        for elemento in pruebas_punto2:
            print('Punto 2: {}'.format(punto2.compute(elemento)))
        print()

    def operation(self, cadena):
        """
        Determina si una cadena corresponde a una operación aritmética válida
        :param cadena:
        :return bolean:
        """
        try:
            operadores = re.search(r'([\d\-+*\\]+)', cadena)
            coincidencias_parentesis_abierto = len(re.findall('[(]+', cadena))
            coincidencias_parentesis_cerrado = len(re.findall('[)]+', cadena))
            if not operadores or coincidencias_parentesis_abierto != coincidencias_parentesis_cerrado:
                return False
            return True
        except Exception:
            return False

    def compute(self, cadena):
        """
        Evalúa una expresión aritméica válida. Retorna Flase si no es válida
        :param cadena:
        :return: float o boolean si la expresión no es válida
        """
        try:
            if self.operation(cadena):
                return eval(cadena)
            return False
        except Exception:
            return False
