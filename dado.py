from random import randint
class Dado:
    """
    La clase Dado representa a un dado,
    el cual posee un número de caras determinado.

    Por tanto el dado tendrá tantos valores
    como caras tenga.

    Al comienzo de vida del dado, el dado se tira,
    de manera que una de sus caras mire hacia arriba.

    """
    def __init__(self, caras):
        """Constructor de la clase Dado."""
        self.__set_caras(caras)
        self.tirar()

    def __repr__(self):
        """Devuelve la forma normal de un dado."""
        return f'Dado({self.valor()})'

    def __str__(self):
        """Devuelve un literal que representa al dado."""
        return f'Un dado con el valor {self.valor()} hacia arriba.'

    def caras(self):
        """Devuelve el valor de una cara"""
        return self.__caras

    def valor(self):
        """Devuelve el valor del dado."""
        return self.__valor

    def __set_caras(self, caras):
        """Asigna un número de caras determinado."""
        self.__caras = caras

    def __set_valor(self, valor):
        """
        Asigna un valor al dado.
        El valor nunca podrá superar el nº de caras.
        """
        if valor in range(1, self.caras() + 1):
            self.__valor = valor
        else: raise ValueError('El valor no puede superar el nº de caras.')

    def tirar(self):
        """
        Tira un dado, cambiando su valor por otro al azar
        de los posibles entre todas sus caras.
        """
        self.__set_valor(randint(1, self.caras()))

class D6(Dado):
    """
    Clase D6
    ---
    extends Dado.\
    La clase D6 representa un dado de 6 caras (d6).
    Como característica única, los dados de 6 caras
    siempre cumplen la condición de que la suma de \
    una cara y su opuesta siempre es 7.
    """
    def __init__(self):
        """Constructor de la clase D6"""
        super().__init__(6)

    def opuesta(self):
        """
        Devuelve el valor de la cara opuesta al valor \
        actual del dado"""
        return 7 - self.valor()

class Cubilete:
    """
    Clase Cubilete
    ---
    La clase cubilete representa un cubilete, el cual se \
    compone porel numero de dados que contenga.

    Nada más comenzar los dados del cubilete ya tienen \
        un valor (la cara que mira hacia arriba).
    """
    def __init__(self, num, tipo = D6):
        """Constructor de la clase cubilete."""
        self.__dados = []
        for d in range(num):
            self.__dados.append(D6())

    def __get_dados(self):
        """
        Devuelve la lista de los dados en el cubilete.
        """
        return self.__dados

    def mostrar_dados(self):
        """
        Devuelve un literal, mostrando el valor de los dados \
        (la cara que mira hacia arriba).
        """
        dados = ''
        # [dados + f'[{d.valor()}] ' for d in self.__get_dados()]
        for d in self.__get_dados():
            dados += f'[{d.valor()}] '
        return dados

    def agitar(self):
        """
        Agita el cubilete, haciendo que los valores de los
        dados cambie.
        """
        [d.tirar() for d in self.__get_dados()]


c = Cubilete(5)
print(c.mostrar_dados())
