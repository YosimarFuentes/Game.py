import random
import time
import os

class NumeroAleatorio:
    def __init__(self, minimo=1, maximo=9):
        self.minimo = minimo
        self.maximo = maximo
        self.numero = self.generar_numero()

    def generar_numero(self):
        return random.randint(self.minimo, self.maximo)

    def actualizar_rango(self):
        self.minimo *= 10
        self.maximo *= 10

class Usuario:
    @staticmethod
    def obtener_intento():
        while True:
            try:
                intento = input("Introduce el número: ")
                if not intento.isdigit():
                    raise ValueError("Debes introducir un número.")
                return int(intento)
            except ValueError as e:
                print(e)

class Juego:
    def __init__(self):
        self.numero_aleatorio = NumeroAleatorio()
        self.aciertos = 0

    def iniciar(self):
        while True:
            numero = self.numero_aleatorio.numero
            print(f"Recuerda el número {numero}...")
            time.sleep(1.5)
            os.system("cls" if os.name == "nt" else "clear")

            intento = Usuario.obtener_intento()

            if intento == numero:
                print("Bien, lo has adivinado.")
                self.aciertos += 1
                self.numero_aleatorio.actualizar_rango()
                self.numero_aleatorio.numero = self.numero_aleatorio.generar_numero()
            else:
                print(f"Mal, el número era: {numero}")
                break

        print(f"Juego terminado. Tuviste {self.aciertos} aciertos.")

if __name__ == "__main__":
    juego = Juego()
    juego.iniciar()

