class Paciente:
    id_secuencial = 1  # Nombre corregido de la variable de clase

    def __init__(self, nombre, apellido, correo, password):
        self.id = Paciente.id_secuencial
        Paciente.id_secuencial += 1
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo
        self.password = password
