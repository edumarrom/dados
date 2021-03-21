from sys import exit
from jugador import Jugador
from dado import Cubilete
PAR = 0
IMPAR = 1

class Bakuchi:
    """
    El Cho-Han Bakuchi es un juego da dados japonés.
    """
    def __init__(self, num_jugadores = 2):
        self.__jugadores = Jugador.asignar_jugadores(num_jugadores)
        self.__apuestas = {}
        self.__cubilete = Cubilete(2)
        self.ronda()

    def __get_jugadores(self):
        return self.__jugadores

    def __borrar_jugador(self, jugador):
        self.__get_jugadores().remove(jugador)

    def __get_apuestas(self):
        return self.__apuestas

    def __limpiar_apuestas(self):
        self.__apuestas = {}

    def cubilete(self):
        return self.__cubilete

    def ronda(self):
        while self.__get_jugadores() != []:
            self.__limpiar_apuestas()
            self.cubilete().agitar()
            print('¿[x] [x]?')
            for j in self.__get_jugadores():
                print(f'| Turno de {j}')
                self.apostar(j)
            print(self.cubilete().mostrar_dados())
            print(f'La suma de los dados da {self.cubilete().suma()}.')
            self.comprobar_apuestas()
            self.comprobar_fin_jugadores()
            self.comprobar_fin_juego()
        self.finalizar()

    def comprobar_fin_jugadores(self):
        for j in self.__get_jugadores():
            if j.puntos() <= 0:
                print(f'{j.nombre()} descalificado.')
                self.__borrar_jugador(j)
        input('Pulsa Intro para continuar.')

    def comprobar_fin_juego(self):
        if len(self.__get_jugadores()) == 1:
            ganador = self.__get_jugadores()[0]
            print(f'{ganador.nombre()} gana la partida.')
            self.finalizar()

    def comprobar_apuestas(self):
        resultado = self.cubilete().suma() % 2
        ganadores = ''
        perdedores = ''
        for k, v in self.__get_apuestas().items():
            if v == resultado:
                k.agregar_punto()
                ganadores += k.nombre()
            else:
                k.quitar_punto()
                perdedores += k.nombre()
        print(f'{ganadores} ganan la ronda, {perdedores} pierden.')

    def apostar(self, jugador):
        """
        pregunta al jugador si va a apostar por par o impar.
        """
        try:
            decision = str(input('¿Apuestas par o impar (P/I)?: '))
        except ValueError:
                print('Por favor, escribe un nombre válido.')
        if decision in ('p', 'e', 'par', 'even'):
            self.__apuestas[jugador] = PAR
        elif decision in ('i', 'o', 'impar', 'odd'):
            self.__apuestas[jugador] = IMPAR

    def finalizar(self):
        """El repartidor pregunta al jugador si quiere volver a jugar."""
        print('¡Hasta luego!.')
        input('Pulsa Intro para finalizar.')
        exit()

if __name__ == '__main__':
    b = Bakuchi()
