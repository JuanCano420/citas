class Celular:
    def __init__(self, numero_celular):
        self.numero_celular = numero_celular

    def enviar_notificacion(self, mensaje):
        print(f"Enviando mensaje de texto para {self.numero_celular}, con contenido: {mensaje}")

    def realizar_llamada(self):
        print(f"Realizando llamada telefónica a {self.numero_celular}")