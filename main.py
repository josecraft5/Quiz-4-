import random

class Jugador:
    def __init__(self,nombre):
        self.nombre = nombre
        self.cartas = [11,2,3,4,5,6,7,8,9,10,10,10]
        self.puntos = 420
        self.set_cartas = [] 
    def pedir_carta_inicial(self):
        carta_1 = random.choice(self.cartas)
        carta_2 = random.choice(self.cartas)
        self.set_cartas.append(carta_1)
        self.set_cartas.append(carta_2)
        print("El Dealer esta barajando...")
        print(f"Tu sacas {self.set_cartas}, Suma -> {sum(self.set_cartas)}")      
        return {sum(self.set_cartas)} 
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
                    return {sum(self.set_cartas)}
                    break

            carta_add = input("¿Deseas pedir otra carta? (Yes/No): ").lower()

        if carta_add == "no":
            print(f"Te plantaste con {self.set_cartas}, Suma -> {sum(self.set_cartas)}")
            return {sum(self.set_cartas)}
                

    def calcular_puntos(self):
        if sum(self.set_cartas) == 21:
            print(f"Congratulaciones, {self.nombre} hiciste un BLACKJACK!!!") 
        elif sum(self.set_cartas) < 21:
            print(f"Congratulaciones, {self.nombre} Ganaste con {self.set_cartas} ") 
        elif sum(self.set_cartas) > 21:
            print(f"Perdiste, {self.nombre} te quedaste con {self.set_cartas}: ") 
    
def separador(caracter="=",longuitud = 60):
    return print(caracter*longuitud)    

class Dealer(Jugador):
    def __init__(self, nombre):
        super().__init__(nombre)
        self.puntos = 99999999
    def pedir_carta_inicial(self):
        carta_1 = random.choice(self.cartas)
        carta_2 = random.choice(self.cartas)
        self.set_cartas.append(carta_1)
        self.set_cartas.append(carta_2)
        print(f"El Dealer saca {self.set_cartas}, Suma -> {sum(self.set_cartas)}")       
    def pedir_carta(self):
        carta_9 = random.choice(self.cartas)
        self.set_cartas.append(carta_9)
    def game_dealer(self):
        while sum(self.set_cartas) < 17:
            self.pedir_carta()
            print(f"El Dealer pide y saca {self.set_cartas}, Suma -> {sum(self.set_cartas)}")   
        if sum(self.set_cartas) == 17:
            print(f"El Dealer se planta con {self.set_cartas}, Suma -> {sum(self.set_cartas)}")   
        else:
            print(f"Dealer se pasó de 21 con {self.set_cartas}, Suma -> {sum(self.set_cartas)}")

def game():    
    separador()
    print("                Bienvenido a BLACKJACK")
    separador()
    # nombre = input("Cual es tu nombre?: ")
    nombre = "jose"
    nombre_dealer = "DEALER"
    p1 = Jugador(nombre)
    d1 = Dealer(nombre_dealer)
    print(f"Tienes {p1.puntos} creditos a tu favor")

    start = input("Comenzar a jugar (Yes/No): ").lower()
    while start != "yes" and start != "no":
        start = input("Error elije (Yes/No): ").lower()

    if start == "yes":
        p1.pedir_carta_inicial()
        p1.pedir_carta_adicional()
        d1.pedir_carta_inicial()
        d1.game_dealer()

    elif start == "no":
        print("El juego a Finalizado")
    
game()
