class Correo:
    def __init__(self, correo):
        self.correo = correo

    def enviar_notificacion(self, asunto, mensaje):
        print(f"Enviando correo a {self.correo} con asunto: {asunto} y mensaje: {mensaje}")