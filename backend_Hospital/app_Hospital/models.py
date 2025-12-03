from django.db import models

class Paciente(models.Model):
    id_paciente = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    genero = models.CharField(max_length=1)
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=20)
    email = models.CharField(max_length=100)
    tipo_sangre = models.CharField(max_length=10)
    fecha_registro = models.DateField()

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Doctor(models.Model):
    id_doctor = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    especialidad = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    email = models.CharField(max_length=100)
    num_licencia = models.CharField(max_length=50)
    fecha_contratacion = models.DateField()
    salario = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class CitaMedica(models.Model):
    id_cita = models.AutoField(primary_key=True)
    id_paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    id_doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    fecha_cita = models.DateField()
    hora_cita = models.TimeField()
    motivo = models.TextField()
    estado = models.CharField(max_length=50)
    observaciones = models.TextField()

    def __str__(self):
        return f"Cita {self.id_cita} - {self.id_paciente.nombre} {self.id_paciente.apellido}"

class Diagnostico(models.Model):
    id_diagnostico = models.AutoField(primary_key=True)
    id_cita = models.ForeignKey(CitaMedica, on_delete=models.CASCADE)
    descripcion = models.TextField()
    tratamiento_recomendado = models.TextField()
    nivel_gravedad = models.CharField(max_length=50)
    fecha_registro = models.DateField()

    def __str__(self):
        return f"Diagnóstico {self.id_diagnostico} - Cita {self.id_cita.id_cita}"

class FacturaHospital(models.Model):
    id_factura = models.AutoField(primary_key=True)
    id_paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    id_cita = models.ForeignKey(CitaMedica, on_delete=models.CASCADE)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    estado_pago = models.CharField(max_length=50)
    metodo_pago = models.CharField(max_length=50)
    fecha_emision = models.DateField()
    descuento = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"Factura {self.id_factura} - Paciente {self.id_paciente.nombre} {self.id_paciente.apellido}"

class Sala(models.Model):
    id_sala = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    capacidad = models.IntegerField()
    tipo = models.CharField(max_length=50)
    disponibilidad = models.BooleanField()

    def __str__(self):
        return f"Sala {self.nombre}"