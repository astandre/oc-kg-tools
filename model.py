import unicodedata


class Contenido:
    uri = ""
    order = ""
    contenido = ""

    def __init__(self, uri, order, contenido):
        self.uri = uri
        self.order = order
        self.contenido = contenido

    def __str__(self):
        return f"({self.order}) {self.contenido}"


class Docente:
    uri = ""
    nombre = ""
    detalle = ""
    img = ""
    email = ""

    def __str__(self):
        return f"{self.nombre}"


class Curso:
    uri = ""
    url = ""
    nombre = ""
    about = ""
    edicion = ""
    prerequisitos = []
    docentes = []
    duracion = ""
    esfuerzo_estimado = ""
    incio = ""
    fin = ""
    competencias = []
    contenido = []
    keywords = []

    def __str__(self):
        return f"{self.uri}-{self.nombre}"


def generate_uri(name):
    name = ''.join(e for e in name if e.isalnum())
    name = ''.join((c for c in unicodedata.normalize('NFD', name) if unicodedata.category(c) != 'Mn'))
    return name
