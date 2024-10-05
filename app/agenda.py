class Agenda:
    def __init__(self):
        self.citas = []

    def agregar_cita(self, cita):
        self.citas.append(cita)
        print(
            f"Cita agregada para el {cita.fecha} con el Dr. {cita.medico.nombre}")

    def cancelar_cita(self, cita):
        self.citas.remove(cita)
        print(
            f"La cita del {cita.fecha} ha sido cancelada.")