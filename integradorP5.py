import os
import random

class Juego:
    def __init__(self, mapa):
        self.mapa = mapa

    def iniciar_juego(self):
        print(f"Iniciando juego con el siguiente mapa:\n{self.mapa}")

class JuegoArchivo(Juego):
    def __init__(self, path_a_mapas):
        super().__init__(self.leer_mapa_aleatorio(path_a_mapas))

    def leer_mapa_aleatorio(self, path_a_mapas):
        try:
            archivos_de_mapas = os.listdir(path_a_mapas)
            if not archivos_de_mapas:
                raise FileNotFoundError("No se encontraron archivos de mapa en la carpeta.")
            
            nombre_archivo = random.choice(archivos_de_mapas)
            path_completo = os.path.join(path_a_mapas, nombre_archivo)
            return self.leer_datos_mapa(path_completo)
        except Exception as e:
            print(f"Error al listar archivos de mapa: {e}")
            return "Error al cargar el mapa."

    def leer_datos_mapa(self, path_archivo):
        try:
            with open(path_archivo, 'r') as archivo:
                dimensiones = archivo.readline().strip().split()
                filas, columnas = int(dimensiones[0]), int(dimensiones[1])
                
                mapa = ""
                for _ in range(filas):
                    fila = archivo.readline().strip()
                    mapa += fila
                
                coordenadas = archivo.readline().strip()
                return f"Mapa:\n{mapa}\nCoordenadas: {coordenadas}"
        except Exception as e:
            print(f"Error al leer datos del mapa: {e}")
            return "Error al cargar el mapa."


path_a_mapas = r"C:\Users\usuario\Desktop\mapa"


juego_archivo = JuegoArchivo(path_a_mapas)


juego_archivo.iniciar_juego()
