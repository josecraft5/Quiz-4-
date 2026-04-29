import random

class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.cartas = [11,2,3,4,5,6,7,8,9,10,10,10]
        self.set_cartas = []

    def pedir_carta_inicial(self):
        carta_1 = random.choice(self.cartas)
        carta_2 = random.choice(self.cartas)
        self.set_cartas.append(carta_1)
        self.set_cartas.append(carta_2)

        print("El Dealer esta barajando...")
        print(f"Tu sacas {self.set_cartas}, Suma -> {sum(self.set_cartas)}")

        return sum(self.set_cartas)

    def suma(self):
        return sum(self.set_cartas)

    def pedir_carta_adicional(self):
        carta_add = input("¿Deseas pedir otra carta? (Yes/No): ").lower()

        while carta_add != "no":

            while carta_add != "yes" and carta_add != "no":
                carta_add = input("Error, elige (Yes/No): ").lower()

            if carta_add == "yes":
                carta_n = random.choice(self.cartas)
                self.set_cartas.append(carta_n)

                print(f"Tu sacas {self.set_cartas}, Suma -> {sum(self.set_cartas)}")

                if sum(self.set_cartas) > 21:
                    print(f"Te pasaste del 21: {self.set_cartas}, Suma -> {sum(self.set_cartas)}")
                    return sum(self.set_cartas)

            carta_add = input("¿Deseas pedir otra carta? (Yes/No): ").lower()

        if carta_add == "no":
            print(f"Te plantaste con {self.set_cartas}, Suma -> {sum(self.set_cartas)}")
            return sum(self.set_cartas)


class Dealer(Jugador):
    def __init__(self, nombre):
        super().__init__(nombre)

    def pedir_carta_inicial(self):
        carta_1 = random.choice(self.cartas)
        carta_2 = random.choice(self.cartas)
        self.set_cartas.append(carta_1)
        self.set_cartas.append(carta_2)

        print(f"El Dealer saca {self.set_cartas}, Suma -> {sum(self.set_cartas)}")

        return sum(self.set_cartas)

    def pedir_carta(self):
        carta_n = random.choice(self.cartas)
        self.set_cartas.append(carta_n)

    def game_dealer(self):
        while sum(self.set_cartas) < 17:
            self.pedir_carta()
            print(f"El Dealer pide y saca {self.set_cartas}, Suma -> {sum(self.set_cartas)}")

        total = sum(self.set_cartas)

        if total > 21:
            print(f"Dealer se pasó de 21 con {self.set_cartas}, Suma -> {total}")
        else:
            print(f"El Dealer se planta con {self.set_cartas}, Suma -> {total}")

        return total


def separador(caracter="=", longitud=60):
    print(caracter * longitud)


def comparar_resultado(jugador, dealer):
    puntos_jugador = jugador.suma()
    puntos_dealer = dealer.suma()

    separador()

    if puntos_jugador > 21:
        print(f"Perdiste :(, {jugador.nombre}. Te pasaste de 21.")

    elif puntos_dealer > 21:
        print(f"Ganaste :), {jugador.nombre}. El dealer se pasó de 21.")

    elif puntos_jugador > puntos_dealer:
        print(f"Ganaste, {jugador.nombre}. Tu suma: {puntos_jugador}, Dealer: {puntos_dealer}")

    elif puntos_dealer > puntos_jugador:
        print(f"Perdiste, {jugador.nombre}. Tu suma: {puntos_jugador}, Dealer: {puntos_dealer}")

    else:
        print(f"Empate. Tu suma: {puntos_jugador}, Dealer: {puntos_dealer}")
    

def game():
    separador()
    print("                Bienvenido a BLACKJACK")
    separador()

    nombre = input("¿Cuál es tu nombre?: ")
    nombre_dealer = "DEALER"

    while True: 

        start = input("¿Jugar una partida? (Yes/No): ").lower()

        while start != "yes" and start != "no":
            start = input("Error elige (Yes/No): ").lower()

        if start == "no":
            print("El juego ha finalizado")
            break 

        p1 = Jugador(nombre)
        d1 = Dealer(nombre_dealer)

        separador()

        p1.pedir_carta_inicial()
        p1.pedir_carta_adicional()

        if p1.suma() <= 21:
            d1.pedir_carta_inicial()
            d1.game_dealer()

        comparar_resultado(p1, d1)

        separador()


game()
