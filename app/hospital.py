from cita import Cita
class Hospital:
    def __init__(self):
        self.usuarios = []
        self.medicos = []
        self.agenda = Agenda()

    def buscar_paciente(self, identificacion):
        return next((p for p in self.usuarios if p.identificacion == identificacion), None)

    def buscar_medico(self, identificacion):
        return next((m for m in self.medicos if m.identificacion == identificacion), None)
    
    def agendar_cita(self, paciente, medico, fecha):
        cita = Cita(paciente, medico, fecha)
        self.agenda.agregar_cita(cita)

    def cancelar_cita(self, cita):
        self.agenda.cancelar_cita(cita)

    def reprogramar_cita(self, cita, nueva_fecha):
        self.cancelar_cita(cita)
        self.agendar_cita(cita.paciente, cita.medico, nueva_fecha)

    def buscar_cita(self, fecha, medico):
        return next((c for c in self.agenda.citas if c.fecha == fecha and c.medico == medico), None)

class Agenda:
    def __init__(self):
        self.citas = []

    def agregar_cita(self, cita):
        self.citas.append(cita)
        print(f"Cita agregada para el {cita.fecha} con el Dr. {cita.medico.nombre}")

    def cancelar_cita(self, cita):
        self.citas.remove(cita)
        print(f"Cita cancelada para el {cita.fecha} con el Dr. {cita.medico.nombre}")