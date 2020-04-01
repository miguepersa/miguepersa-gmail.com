from reproductor import *
from cancion import *
from arbolDeCanciones import *

# Clase LR de Lista de Reproduccion
class lr(object):
    # Contructor de la clase LR
    def __init__(self):
        self.contenido = None

    # Metodo para obtener el nombre de un arhivo, leerlo y cargarlo, extraer la informacion por lineas del documento, crear una objeto playlist de la clase LR y añadirle
    # objetos de tipo Cancion en base a los datos en el archivo de texto.
    def agregarLista(self, na):
        archivo = str(na)
        lista = open(archivo, "r")
        for linea in lista:
            campos = linea.split(";")

            interprete = campos[0]
            titulo = campos[1]
            ubicacion = campos[2]

            song = cancion(titulo, interprete, ubicacion)

            if self.contenido is None:
                playlist = arbolDeCanciones()
                self.contenido = playlist
            else:
                playlist.insertar(song)

        lista.close()

    # Metodo para eliminar una cancion del Arbol de Canciones
    def eliminarCancion(self, i, t):
        if self.contenido is None:
            return False
        else:
            self.contenido.eliminar(i,t)
        return
    
    # Metodo para generar una secuencia en orden a partir del Arbol de Canciones
    def obtenerLR(self):
        if self.contenido is None:
            return False
        else:
            seq = self.contenido.deArbolASecuencia()
        return seq

    # Metodo para mostrar en pantalla todas los titulos e interpretes de todas las cancioens almacenadas en la Lista de Reproduccion
    def mostrarLR(self):
        if self.contenido is None:
            return False
        else:
            self.contenido.inorder()
            return True
