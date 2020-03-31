from reproductor import *
from cancion import *
from arbolDeCanciones import *


class lr(object):

    def __init__(self):
        self.contenido = None


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

    def eliminarCancion(self, i, t):
        if self.contenido is None:
            return False
        else:
            self.contenido.eliminar(i,t)
        return
    

    def obtenerLR(self):
        if self.contenido is None:
            return False
        else:
            seq = self.contenido.deArbolASecuencia()



        return seq

    
    def mostrarLR(self):
        if self.contenido is None:
            return False
        else:
            self.contenido.inorder()
            return True
