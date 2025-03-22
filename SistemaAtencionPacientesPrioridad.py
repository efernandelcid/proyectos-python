class Paciente:
    def __init__(self, nombre, edad, dpi, tipoSangre):
        self.nombre = nombre
        self.edad = edad
        self.dpi = dpi
        self.tipoSangre = tipoSangre

    def __str__(self):
        return f"{self.nombre} {self.edad} {self.dpi} {self.tipoSangre}"


class Enfermedad:
    def __init__(self, nombre, descripcion, prioridad):
        self.nombre = nombre
        self.descripcion = descripcion
        self.prioridad = prioridad

    def __str__(self):
        return f"{self.nombre} {self.descripcion} {self.prioridad}"


class Asignador:
    def __init__(self):
        self.cola = []

    def agregarPaciente(self, paciente, enfermedad):
        prioridadValor = {"Baja": 3, "Alta": 2, "Critica": 1}
        self.cola.append((prioridadValor[enfermedad.prioridad], paciente, enfermedad))
        self.cola.sort(key=lambda x: x[0])  # Ordenar por prioridad

    def atenderPaciente(self):
        if self.cola:
            prioridad, paciente, enfermedad = self.cola.pop(0)
            print(f"Atendiendo a {paciente.nombre} \nEnfermedad: {enfermedad.nombre} \nPrioridad: {enfermedad.prioridad}")
        else:
            print("No hay pacientes en la cola")

    def mostrarPacientes(self):
        if self.cola:
            print("\nPacientes en espera:")
            for prioridad, paciente, enfermedad in self.cola:
                print(f"{paciente.nombre} - {enfermedad.nombre} ({enfermedad.prioridad})")
        else:
            print("No hay pacientes en la cola")


if __name__ == "__main__":
    asignador = Asignador()

    paciente1 = Paciente("Juan", 25, 123456789, "O+")
    enfermedad1 = Enfermedad("Gripe", "Resfriado", "Baja")

    paciente2 = Paciente("Maria", 30, 987654321, "A+")
    enfermedad2 = Enfermedad("Migraña", "Dolor de cabeza", "Critica")

    paciente3 = Paciente("Pedro", 35, 123456789, "AB+")
    enfermedad3 = Enfermedad("Fractura", "Pierna rota", "Alta")

    asignador.agregarPaciente(paciente1, enfermedad1)
    asignador.agregarPaciente(paciente2, enfermedad2)
    asignador.agregarPaciente(paciente3, enfermedad3)

    asignador.mostrarPacientes()

    asignador.atenderPaciente()
    asignador.mostrarPacientes()
