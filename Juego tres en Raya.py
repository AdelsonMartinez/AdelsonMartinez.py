import tkinter as tk
from tkinter import messagebox

class TresEnRaya:
    def __init__(self, root):
        """
        Inicializa la clase TresEnRaya. 
        Configura la ventana principal y los atributos del juego.
        """
        self.root = root
        self.root.title("Tres en Raya")
        self._jugador = "X"  # Inicia el juego con el jugador X
        self._tablero = [""] * 9  # Estado inicial del tablero
        self._botones = []  # Lista para almacenar botones del tablero
        self._punctuaciones = {'X': 0, 'O': 0}  # Contadores de puntos para cada jugador
        self.crear_interfaz()
