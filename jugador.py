class Jugador:

    def __init__(self, nombre, puntos = 3):
        self.__set_nombre(nombre)
        self.__set_puntos(puntos)

    def __str__(self):
        return f'| {self.nombre()} | {self.puntos()} puntos |'

    def nombre(self):
        return self.__nombre

    def puntos(self):
        return self.__puntos

    def __set_nombre(self, nombre):
        self.__nombre = nombre

    def __set_puntos(self, puntos):
        self.__puntos = puntos

    def agregar_punto(self):
        self.__set_puntos(self.puntos() + 1)

    def quitar_punto(self):
        self.__set_puntos(self.puntos() - 1)

    @staticmethod
    def asignar_jugadores(num_jugadores):
        """
        Creador interactivo de humanos. Solicita por entrada el \
            nombre del jugador.
        """
        jugadores = []
        for i in range(num_jugadores):
            try:
                nombre_jugador = str(input('¿Nombre del jugador?: '))
            except ValueError:
                print('Por favor, escribe un nombre válido.')
            jugadores.append(Jugador(nombre_jugador))
        return jugadores
