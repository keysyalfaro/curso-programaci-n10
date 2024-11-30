import random
import os

class JuegoAdivinanza:
    def __init__(self):
        self.numero_secreto = random.randint(1, 100)
        self.intentos = 0

    def validarNumero(self, numero):
        if numero > self.numero_secreto:
            return "El número es menor."
        elif numero < self.numero_secreto:
            return "El número es mayor."
        else:
            return "¡Correcto! Has adivinado el número."

    def registrarIntento(self):
        self.intentos += 1

    def reiniciar(self):
        self.numero_secreto = random.randint(1, 100)
        self.intentos = 0


class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.historial = []  # Lista de partidas (intentos, resultado)

    def registrarPartida(self, intentos, gano):
        self.historial.append((intentos, gano))

    def mostrarEstadisticas(self):
        partidas_jugadas = len(self.historial)
        partidas_ganadas = sum(1 for _, gano in self.historial if gano)
        porcentaje_aciertos = (
            (partidas_ganadas / partidas_jugadas * 100) if partidas_jugadas > 0 else 0
        )
        print(f"\nEstadísticas de {self.nombre}:")
        print(f"Partidas jugadas: {partidas_jugadas}")
        print(f"Partidas ganadas: {partidas_ganadas}")
        print(f"Porcentaje de aciertos: {porcentaje_aciertos:.2f}%\n")


def guardar_estadisticas(jugador):
    """Guarda las estadísticas del jugador en un archivo dentro de este módulo."""
    ruta_archivo = os.path.join(os.path.dirname(__file__), "estadisticas.txt")
    with open(ruta_archivo, "w") as archivo:
        archivo.write(jugador.nombre + "\n")
        for intentos, gano in jugador.historial:
            archivo.write(f"{intentos},{gano}\n")


def cargar_estadisticas():
    """Carga las estadísticas desde un archivo dentro de este módulo."""
    ruta_archivo = os.path.join(os.path.dirname(__file__), "estadisticas.txt")
    if os.path.exists(ruta_archivo):
        with open(ruta_archivo, "r") as archivo:
            nombre = archivo.readline().strip()
            jugador = Jugador(nombre)
            for linea in archivo:
                intentos, gano = linea.strip().split(",")
                jugador.historial.append((int(intentos), gano == "True"))
            return jugador
    return None


def menu():
    """Muestra el menú principal del juego."""
    jugador = cargar_estadisticas()  # Intenta cargar estadísticas previas
    if not jugador:
        # Si no hay estadísticas previas, solicita el nombre del jugador
        nombre = input("Ingrese su nombre: ").strip()
        if not nombre:
            print("El nombre no puede estar vacío. Intente de nuevo.")
            return  # Sale si no ingresa un nombre válido
        jugador = Jugador(nombre)

    juego = JuegoAdivinanza()  # Instancia un nuevo juego

    while True:
        print("\nMenú:")
        print("1. Comenzar una nueva partida")
        print("2. Ver estadísticas del jugador")
        print("3. Salir del juego")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print("\nNueva partida:")
            juego.reiniciar()
            while True:
                try:
                    numero = int(input("Adivine el número (1-100): "))
                    juego.registrarIntento()
                    resultado = juego.validarNumero(numero)
                    print(resultado)
                    if resultado == "¡Correcto! Has adivinado el número.":
                        jugador.registrarPartida(juego.intentos, True)
                        break
                except ValueError:
                    print("Por favor, ingrese un número válido.")
        elif opcion == "2":
            jugador.mostrarEstadisticas()
        elif opcion == "3":
            guardar_estadisticas(jugador)  # Guarda estadísticas antes de salir
            print("Estadísticas guardadas. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

menu()
