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
        self.__botin = 0
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

    def botin(self):
        return self.__botin

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
            if j.saldo() <= 0:
                print(f'{j.nombre()} se quedó sin fondos.')
                self.__borrar_jugador(j)
                input('Pulsa Intro para continuar.')

    def quien_gana(self):
        ganador = None
        for j in self.__get_jugadores():
            if j.saldo() == (75 * (1000 * len(self.__get_jugadores()))) / 100:
                ganador = j
                break
        if ganador == None:
            input('Pulsa Intro para pasar a la siguiente ronda.')
        else:
            print(f'{ganador.nombre()} gana la partida, '\
                f'con {ganador.puntos()} puntos, el 75% del total.')
            self.finalizar()

    def comprobar_fin_juego(self):
        if len(self.__get_jugadores()) == 1:
            ganador = self.__get_jugadores()[0]
            print(f'{ganador.nombre()} gana la partida, '\
                'por ser el último jugador en pié.')
            self.finalizar()
        else: self.quien_gana()

    def comprobar_apuestas(self):
        resultado = self.cubilete().suma() % 2
        ganadores = []
        perdedores = []
        for k, v in self.__get_apuestas().items():
            if v == resultado:
                ganadores.append(k)
            else:
                perdedores.append(k)
        g = ''
        p = ''

        for j in self.__get_jugadores():
            if j in ganadores:
                j.agregar_saldo(self.botin() / len(ganadores))
                if j == ganadores[-1]:
                    g += f'y {j.nombre()}'
                else:
                    g += f'{j.nombre()}, '
            else:
                if j == perdedores[-1]:
                    p += f'y {j.nombre()}'
                else:
                    p += f'{j.nombre()}, '
        print(f'{g} ganan la ronda. {p} pierden.')

    def apostar(self, jugador: Jugador):
        """
        pregunta al jugador si va a apostar por par o impar.
        A continuación pregunta cuanto quiere apostar.
        """
        try:
            decision = str(input('¿Apuestas par o impar (P/I)?: '))
        except ValueError:
                print('Por favor, escribe un nombre válido.')
        if decision in ('p', 'e', 'par', 'even'):
            self.__apuestas[jugador] = PAR
        elif decision in ('i', 'o', 'impar', 'odd'):
            self.__apuestas[jugador] = IMPAR
        try:
            apuesta = int(input('¿Cuánto quieres apostar?: '))
        except ValueError:
                print('Por favor, escribe una cantidad válida.')
        jugador.retirar_saldo(apuesta)
        self.__botin += apuesta


    def finalizar(self):
        """El repartidor pregunta al jugador si quiere volver a jugar."""
        print('¡Hasta luego!.')
        input('Pulsa Intro para finalizar.')
        exit()

if __name__ == '__main__':
    print('Bienvenido a esta nueva partida de Cho-Han Bakuchi.')
    num_jugadores = int(input('¿Cuántos vamos a jugar?: '))
    b = Bakuchi(num_jugadores)
