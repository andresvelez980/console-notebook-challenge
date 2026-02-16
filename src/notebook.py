# TODO: Agrega el código de las clases del modelo aquí. Borra este comentario al terminar.
HIGH: str = "HIGH"
MEDIUM: str = "MEDIUM"
LOW: str = "LOW"
class Note:
    def __init__(self, code: str, tittle: str, text: str, importance: str, creation_date: str):
        self.code = code
        self.tittle = tittle
        self.text = text
        self.importance = importance
        self.creation_date = creation_date
