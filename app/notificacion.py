class Notificacion:
    def __init__(self, persona):
        self.persona = persona

    def enviar_notificacion(self, mensaje):
        pass

class Correo(Notificacion):
    def enviar_notificacion(self, mensaje):
        print(f"Enviando correo a {self.persona.correo} con mensaje: {mensaje}")

class Celular(Notificacion):
    def enviar_notificacion(self, mensaje):
        print(f"Enviando mensaje de texto a {self.persona.celular} con mensaje: {mensaje}")

class Whatsapp(Notificacion):
    def enviar_notificacion(self, mensaje):
        print(f"Enviando mensaje de Whatsapp a {self.persona.celular} con mensaje: {mensaje}")