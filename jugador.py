from random import choice
class Jugador:

    def __init__(self, nombre, saldo = 1000.0):
        self.__set_nombre(nombre)
        self.__set_saldo(saldo)

    def __str__(self):
        return f'| {self.nombre()} | Monedero: {self.saldo()} ¥ |'

    def nombre(self):
        return self.__nombre

    def saldo(self):
        return self.__saldo

    def __set_nombre(self, nombre):
        self.__nombre = nombre

    def __set_saldo(self, saldo):
        self.__saldo = saldo

    def agregar_saldo(self, cantidad):
        self.__set_saldo(self.saldo() + cantidad)

    def retirar_saldo(self, cantidad):
        if cantidad <= self.saldo():
            self.__set_saldo(self.saldo() - cantidad)
        else: raise ValueError('La cantidad solicitada es mayor '\
            'que el saldo disponible')

    @staticmethod
    def asignar_jugadores(num_jugadores):
        """
        Creador interactivo de humanos. Solicita por entrada el \
            nombre del jugador.
        """
        jugadores = []
        for i in range(num_jugadores):
            try:
                nombre_jugador = str(input(f'¿Nombre del jugador nº '\
                    f'{str(i + 1)}?: '))
            except ValueError:
                print('Por favor, escribe un nombre válido.')
            jugadores.append(Jugador(nombre_jugador))
        return jugadores
