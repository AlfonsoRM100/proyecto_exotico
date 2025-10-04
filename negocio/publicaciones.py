publicaciones = []

class Publicacion:
    def __init__(self, contenido, usuario):
        self.contenido = contenido
        self.usuario = usuario
        self.likes = 0
