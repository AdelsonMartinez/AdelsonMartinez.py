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
    def crear_interfaz(self):
        """
        Crea la interfaz gráfica del juego.
        Incluye el título, botón de reinicio, y botones del tablero.
        """
        self.root.configure(bg="#A3C9C9")  # Cambia el fondo de la ventana principal
        titulo = tk.Label(self.root, text="Tres en Raya", font=("Helvetica", 30), bg="#A3C9C9", fg="#000000")  # Cambiado a negro
        titulo.pack(pady=10)

        # Etiqueta que muestra el turno actual
        self.indicador_turno = tk.Label(self.root, text=f"Turno: Jugador {self._jugador}", font=("Helvetica", 20), bg="#A3C9C9", fg="#FF5733")
        self.indicador_turno.pack(pady=10)
        # Etiquetas para mostrar las puntuaciones
        self.indicador_puntuacion = tk.Label(self.root, text=f"X: {self._punctuaciones['X']}  O: {self._punctuaciones['O']}", font=("Helvetica", 20), bg="#A3C9C9", fg="#000000")  # Cambiado a negro
        self.indicador_puntuacion.pack(pady=10)
        reiniciar_btn = tk.Button(self.root, text="Reiniciar Juego", font=("Helvetica", 16), command=self.reiniciar, bg="#FFB6C1", fg="#000000")  # Cambiado a negro
        reiniciar_btn.pack(pady=10)

        #Se crea un marco para los botones del tablero
        tablero_frame = tk.Frame(self.root, bg="#A3C9C9")
        tablero_frame.pack()

        for i in range(9):
            boton = tk.Button(
                tablero_frame, 
                text="", 
                font=("Helvetica", 24), 
                height=2, 
                width=5, 
                bg="#FFFFFF", 
                activebackground="#DDDDDD",
                command=lambda i=i: self.hacer_movimiento(i)
            )
            # Establecer el tamaño del botón usando grid en el marco
            boton.grid(row=i // 3, column=i % 3, padx=10, pady=10)
            self._botones.append(boton)

    def reiniciar(self):
        """
        Reinicia el estado del juego, permitiendo que los jugadores empiecen de nuevo.
        """
        self._jugador = "X"  # Reinicia el jugador a X
        self._tablero = [""] * 9  # Limpia el tablero
        for boton in self._botones:
            boton.config(text="", bg="#FFFFFF")  # Restablece los botones a su estado inicial
        self.indicador_turno.config(text=f"Turno: Jugador {self._jugador}")  # Actualiza el indicador de turno

    def hacer_movimiento(self, indice):
        """
        Realiza un movimiento en el tablero.

        :param indice: Indice del botón que se presionó.
        """
        # Verifica si el movimiento es válido: el botón no debe estar ocupado y no debe haber un ganador
        if self._tablero[indice] == "" and not self.verificar_ganador():
            self._tablero[indice] = self._jugador  # Actualiza el estado del tablero
            self._botones[indice]["text"] = self._jugador  # Muestra el símbolo del jugador en el botón
            self._botones[indice]["bg"] = "#ADD8E6" if self._jugador == "X" else "#FFB6C1"  # Cambia el color del botón

            # Verifica si hay un ganador o si hay un empate
            if self.verificar_ganador():
                self._punctuaciones[self._jugador] += 1  # Incrementa la puntuación del jugador ganador
                self.indicador_puntuacion.config(text=f"X: {self._punctuaciones['X']}  O: {self._punctuaciones['O']}")  # Actualiza la puntuación
                messagebox.showinfo("Fin del juego", f"Ganador: Jugador {self._jugador}")
            elif "" not in self._tablero:
                messagebox.showinfo("Fin del juego", "Empate")
            else:
                # Cambia el turno al siguiente jugador
                self._jugador = "O" if self._jugador == "X" else "X"
                self.indicador_turno.config(text=f"Turno: Jugador {self._jugador}")  # Actualiza el indicador de turno
        else:
            # Mensaje de advertencia si el movimiento no es válido
            messagebox.showwarning("Movimiento inválido", "Este espacio ya está ocupado, elige otro.")
