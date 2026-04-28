import random

class jugador:
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
        print(f"El Dealer a sacado {self.set_cartas}, Suma -> {sum(self.set_cartas)}")       
    def suma(self):
        return sum(self.set_cartas)
    def mostrar_mano_suma(self):
        print(f"Suma de tus cartas = {sum(self.set_cartas)}")
    def pedir_carta_adicional(self):
        carta_add = input("Deseas pedir otra carta? (Yes/No): ").lower()
        while carta_add != "yes" and carta_add != "no":
            carta_add = input("Error elije (Yes/No): ").lower()
        if carta_add == "yes":
            carta_n = random.choice(self.cartas)
            self.set_cartas.append(carta_n)
            print(f"El Dealer saca {self.set_cartas}, Suma -> {sum(self.set_cartas)}")
    def calcular_puntos(self):
        if sum(self.set_cartas) == 21:
            print(f"Congratulaciones, {self.nombre} hiciste un BLACKJACK!!!") 
        elif sum(self.set_cartas) < 21:
            print(f"Congratulaciones, {self.nombre} Ganaste con {self.set_cartas} ") 
        elif sum(self.set_cartas) > 21:
            print(f"Perdista, {self.nombre} te quedaste con {self.set_cartas}: ") 
    
def separador(caracter="=",longuitud = 60):
    return print(caracter*longuitud)    

def game():    
    separador()
    print("                Bienvenido a BLACKJACK")
    separador()
    # nombre = input("Cual es tu nombre?: ")
    nombre = "jose"
    p1 = jugador(nombre)
    print(f"Tienes {p1.puntos} creditos a tu favor")
    start = input("Comenzar a jugar (Yes/No): ").lower()
    while start != "yes" and start != "no":
        start = input("Error elije (Yes/No): ").lower()
    if start == "yes":
        p1.pedir_carta_inicial()
        p1.pedir_carta_adicional()
        p1.pedir_carta_adicional()
        p1.pedir_carta_adicional()
        p1.calcular_puntos()
    elif start == "no":
        print("El juego a Finalizado")
    
    
game()