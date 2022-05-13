
class Arreglo:

    def run(self):
        a = [1, 2]
        b = [[1, 2], [2, 4]]
        c = [[1, 2], [2, 4], [2, 4]]
        d = [[[3, 4], [6, 5]]]
        e = [[[1, 2, 3]], [[5, 6, 7], [5, 4, 3]], [[3, 5, 6], [4, 8, 3], [2, 3]]]
        f = [[[1, 2, 3], [2, 3, 4]], [[5, 6, 7], [5, 4, 3]], [[3, 5, 6], [4, 8, 3]]]
        pruebas_punto1 = [a, b, c, d, e, f]

        punto1 = Arreglo()

        for elemento in pruebas_punto1:
            print('Punto 1: {}'.format(punto1.dimension(elemento)))
        print()

        for elemento in pruebas_punto1:
            print('Punto 2: {}'.format(punto1.straight(elemento)))
        print()

        for elemento in pruebas_punto1:
            print('Punto 3: {}'.format(punto1.compute(elemento)))
        print()

    """
    Clase para ejercicios del punto 1
    """

    def dimension(self, lista):
        """
        Retorna la profundidad mximo de una lista
        :param lista:
        :return:
        """
        if isinstance(lista, list):
            return 1 + (max(map(self.dimension, lista)) if lista else 0)
        return 0

    def straight(self, lista):
        """
        Determina si cada lista tiene el mismo tamaño en cada una de sus profundidades
        :param lista:
        :return:
        """
        dimensiones_lista = self.obtener_dimension(lista)
        if not isinstance(dimensiones_lista, list):
            return True
        return dimensiones_lista.count(dimensiones_lista[0]) == len(dimensiones_lista)

    def obtener_dimension(self, lista):
        """
        Retrorna una lista con los tamaños de la lista y/o sublistas
        :param lista:
        :return:
        """
        lista_nueva = []
        for item in lista:
            # Si el elemento no es una lista, retorna el tamaño de la lista
            if not isinstance(item, list):
                return len(lista)
            if type(item) in [list]:
                respuesta = self.obtener_dimension(item)

                # Si la respuesta es un entero hace extend, si es una lista, hace append
                lista_nueva.append(respuesta) if isinstance(respuesta, int) else lista_nueva.extend(respuesta)

        return lista_nueva

    def compute(self, lista):
        """
        Retorna la suma de cada uno de los elementos de una lista
        :param lista:
        :return:
        """
        if isinstance(lista, list):
            return 0 + (sum(map(self.compute, lista)) if lista else 0)
        return lista

