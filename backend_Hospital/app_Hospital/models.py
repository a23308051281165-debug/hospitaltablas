from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Paciente(models.Model):
    # Opciones para campos con elecciones limitadas
    GENERO_OPCIONES = [
        ('M', 'Masculino'),
        ('F', 'Femenino'),
        ('O', 'Otro'),
    ]
    
    ESTADO_CIVIL_OPCIONES = [
        ('S', 'Soltero/a'),
        ('C', 'Casado/a'),
        ('D', 'Divorciado/a'),
        ('V', 'Viudo/a'),
        ('U', 'Unión libre'),
    ]
    
    TIPO_IDENTIFICACION_OPCIONES = [
        ('DNI', 'Documento Nacional de Identidad'),
        ('PAS', 'Pasaporte'),
        ('CE', 'Carnet de Extranjería'),
        ('LIC', 'Licencia de Conducir'),
        ('OTRO', 'Otro'),
    ]
    
    id_paciente = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    apellido = models.CharField(max_length=100, blank=True, null=True)
    fecha_nacimiento = models.DateField(blank=True, null=True)
    genero = models.CharField(max_length=1, choices=GENERO_OPCIONES, blank=True, null=True)
    direccion = models.CharField(max_length=255, blank=True, null=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(max_length=100, blank=True, null=True)
    tipo_sangre = models.CharField(max_length=10, blank=True, null=True)
    fecha_registro = models.DateField(auto_now_add=True)
    estado_civil = models.CharField(max_length=50, choices=ESTADO_CIVIL_OPCIONES, blank=True, null=True)
    ocupacion = models.CharField(max_length=100, blank=True, null=True)
    nacionalidad = models.CharField(max_length=50, blank=True, null=True)
    numero_seguro_social = models.CharField(max_length=50, blank=True, null=True, unique=True)
    tipo_identificacion = models.CharField(max_length=50, choices=TIPO_IDENTIFICACION_OPCIONES, blank=True, null=True)
    numero_identificacion = models.CharField(max_length=50, blank=True, null=True, unique=True)
    
    class Meta:
        verbose_name = 'Paciente'
        verbose_name_plural = 'Pacientes'
        ordering = ['apellido', 'nombre']
        indexes = [
            models.Index(fields=['apellido', 'nombre']),
            models.Index(fields=['numero_identificacion']),
        ]
    
    def __str__(self):
        return f"{self.nombre} {self.apellido} ({self.numero_identificacion})"
    
    def edad(self):
        """Calcula la edad del paciente"""
        if self.fecha_nacimiento:
            from datetime import date
            today = date.today()
            return today.year - self.fecha_nacimiento.year - (
                (today.month, today.day) < (self.fecha_nacimiento.month, self.fecha_nacimiento.day)
            )
        return None

class Doctor(models.Model):
    id_doctor = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    apellido = models.CharField(max_length=100, blank=True, null=True)
    especialidad = models.CharField(max_length=100, blank=True, null=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(max_length=100, blank=True, null=True)
    num_licencia = models.CharField(max_length=50, blank=True, null=True, unique=True)
    fecha_contratacion = models.DateField(blank=True, null=True)
    salario = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    horario_trabajo = models.CharField(max_length=50, blank=True, null=True)
    direccion_clinica = models.CharField(max_length=255, blank=True, null=True)
    experiencia_anios = models.IntegerField(blank=True, null=True)
    certificaciones = models.TextField(blank=True, null=True)
    idiomas = models.CharField(max_length=100, blank=True, null=True)
    estado_activo = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = 'Doctor'
        verbose_name_plural = 'Doctores'
        ordering = ['apellido', 'nombre']
        indexes = [
            models.Index(fields=['especialidad']),
            models.Index(fields=['estado_activo']),
        ]
    
    def __str__(self):
        return f"Dr. {self.nombre} {self.apellido} - {self.especialidad}"
    
    @property
    def nombre_completo(self):
        return f"{self.nombre} {self.apellido}"

class CitaMedica(models.Model):
    ESTADO_OPCIONES = [
        ('PEND', 'Pendiente'),
        ('CONF', 'Confirmada'),
        ('CANC', 'Cancelada'),
        ('REAL', 'Realizada'),
        ('AUS', 'Ausente'),
    ]
    
    TIPO_CITA_OPCIONES = [
        ('CONS', 'Consulta'),
        ('CONT', 'Control'),
        ('EMER', 'Emergencia'),
        ('SEGU', 'Seguimiento'),
        ('TERA', 'Terapia'),
    ]
    
    TIPO_ATENCION_OPCIONES = [
        ('PRE', 'Presencial'),
        ('VIR', 'Virtual'),
        ('DOM', 'Domicilio'),
    ]
    
    PRIORIDAD_OPCIONES = [
        ('BAJA', 'Baja'),
        ('MED', 'Media'),
        ('ALTA', 'Alta'),
        ('URG', 'Urgente'),
    ]
    
    MEDIO_RESERVA_OPCIONES = [
        ('WEB', 'Web'),
        ('TEL', 'Teléfono'),
        ('PER', 'Personalmente'),
        ('APP', 'App Móvil'),
    ]
    
    id_cita = models.AutoField(primary_key=True)
    id_paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, related_name='citas')
    id_doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='citas')
    fecha_cita = models.DateField(blank=True, null=True)
    hora_cita = models.TimeField(blank=True, null=True)
    duracion_minutos = models.IntegerField(default=30, blank=True, null=True)
    motivo = models.TextField(blank=True, null=True)
    estado = models.CharField(max_length=50, choices=ESTADO_OPCIONES, default='PEND')
    observaciones = models.TextField(blank=True, null=True)
    tipo_cita = models.CharField(max_length=50, choices=TIPO_CITA_OPCIONES, blank=True, null=True)
    lugar_cita = models.CharField(max_length=255, blank=True, null=True)
    tipo_atencion = models.CharField(max_length=50, choices=TIPO_ATENCION_OPCIONES, blank=True, null=True)
    prioridad = models.CharField(max_length=50, choices=PRIORIDAD_OPCIONES, blank=True, null=True)
    costo_consulta = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    medio_reserva = models.CharField(max_length=50, choices=MEDIO_RESERVA_OPCIONES, blank=True, null=True)
    
    class Meta:
        verbose_name = 'Cita Médica'
        verbose_name_plural = 'Citas Médicas'
        ordering = ['-fecha_cita', '-hora_cita']
        indexes = [
            models.Index(fields=['fecha_cita', 'estado']),
            models.Index(fields=['id_paciente', 'id_doctor']),
        ]
        unique_together = [['id_doctor', 'fecha_cita', 'hora_cita']]
    
    def __str__(self):
        return f"Cita {self.id_cita}: {self.id_paciente} con {self.id_doctor} - {self.fecha_cita}"
    
    @property
    def fecha_hora_cita(self):
        """Devuelve fecha y hora combinadas"""
        if self.fecha_cita and self.hora_cita:
            from datetime import datetime
            return datetime.combine(self.fecha_cita, self.hora_cita)
        return None

class Diagnostico(models.Model):
    NIVEL_GRAVEDAD_OPCIONES = [
        ('LEV', 'Leve'),
        ('MOD', 'Moderado'),
        ('GRA', 'Grave'),
        ('CRI', 'Crítico'),
    ]
    
    ESTADO_DIAGNOSTICO_OPCIONES = [
        ('PREL', 'Preliminar'),
        ('CONF', 'Confirmado'),
        ('DESC', 'Descartado'),
        ('REVI', 'En Revisión'),
    ]
    
    TIPO_DIAGNOSTICO_OPCIONES = [
        ('CLIN', 'Clínico'),
        ('LAB', 'Laboratorio'),
        ('IMG', 'Imagenología'),
        ('PAT', 'Patológico'),
        ('COM', 'Combinado'),
    ]
    
    id_diagnostico = models.AutoField(primary_key=True)
    id_cita = models.ForeignKey(CitaMedica, on_delete=models.CASCADE, related_name='diagnosticos')
    codigo_cie10 = models.CharField(max_length=50, blank=True, null=True)
    resultado_examen = models.TextField(blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    tratamiento_recomendado = models.TextField(blank=True, null=True)
    nivel_gravedad = models.CharField(max_length=50, choices=NIVEL_GRAVEDAD_OPCIONES, blank=True, null=True)
    fecha_registro = models.DateField(auto_now_add=True)
    codigo_diagnostico = models.CharField(max_length=50, blank=True, null=True)
    estado_diagnostico = models.CharField(max_length=50, choices=ESTADO_DIAGNOSTICO_OPCIONES, blank=True, null=True)
    especialista_encargado = models.CharField(max_length=100, blank=True, null=True)
    comentarios = models.TextField(blank=True, null=True)
    seguimiento = models.TextField(blank=True, null=True)
    tipo_diagnostico = models.CharField(max_length=50, choices=TIPO_DIAGNOSTICO_OPCIONES, blank=True, null=True)
    recomendaciones = models.TextField(blank=True, null=True)
    
    class Meta:
        verbose_name = 'Diagnóstico'
        verbose_name_plural = 'Diagnósticos'
        ordering = ['-fecha_registro']
        indexes = [
            models.Index(fields=['codigo_cie10']),
            models.Index(fields=['nivel_gravedad']),
        ]
    
    def __str__(self):
        return f"Diagnóstico {self.id_diagnostico} - Cita {self.id_cita.id_cita}"

class FacturaHospital(models.Model):
    METODO_PAGO_OPCIONES = [
        ('EFE', 'Efectivo'),
        ('TAR', 'Tarjeta'),
        ('CHE', 'Cheque'),
        ('TRA', 'Transferencia'),
        ('SEG', 'Seguro'),
        ('OTRO', 'Otro'),
    ]
    
    ESTADO_PAGO_OPCIONES = [
        ('PEND', 'Pendiente'),
        ('PAG', 'Pagado'),
        ('PAR', 'Parcial'),
        ('CANC', 'Cancelado'),
        ('ANU', 'Anulado'),
    ]
    
    TIPO_SERVICIO_OPCIONES = [
        ('CONS', 'Consulta'),
        ('LAB', 'Laboratorio'),
        ('IMG', 'Imágenes'),
        ('HOS', 'Hospitalización'),
        ('FARM', 'Farmacia'),
        ('TER', 'Terapia'),
    ]
    
    id_factura = models.AutoField(primary_key=True)
    id_paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, related_name='facturas')
    id_cita = models.ForeignKey(CitaMedica, on_delete=models.SET_NULL, blank=True, null=True, related_name='facturas')
    total = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    estado_pago = models.CharField(max_length=50, choices=ESTADO_PAGO_OPCIONES, default='PEND')
    fecha_emision = models.DateField(auto_now_add=True)
    descuento = models.DecimalField(max_digits=5, decimal_places=2, default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])
    impuestos = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    descripcion_servicios = models.TextField(blank=True, null=True)
    metodo_pago = models.CharField(max_length=50, choices=METODO_PAGO_OPCIONES, blank=True, null=True)
    numero_factura = models.CharField(max_length=50, unique=True, blank=True, null=True)
    codigo_autorizacion = models.CharField(max_length=50, blank=True, null=True)
    tipo_servicio = models.CharField(max_length=50, choices=TIPO_SERVICIO_OPCIONES, blank=True, null=True)
    numero_orden = models.CharField(max_length=50, blank=True, null=True)
    referencia_pago = models.CharField(max_length=100, blank=True, null=True)
    comentarios_adicionales = models.TextField(blank=True, null=True)
    
    class Meta:
        verbose_name = 'Factura Hospital'
        verbose_name_plural = 'Facturas Hospital'
        ordering = ['-fecha_emision']
        indexes = [
            models.Index(fields=['estado_pago']),
            models.Index(fields=['numero_factura']),
        ]
    
    def __str__(self):
        return f"Factura {self.numero_factura or self.id_factura} - {self.id_paciente}"
    
    @property
    def total_con_impuestos(self):
        """Calcula el total incluyendo impuestos y descuento"""
        if self.total:
            subtotal = self.total
            descuento = subtotal * (self.descuento / 100)
            total_descontado = subtotal - descuento
            impuestos = total_descontado * (self.impuestos / 100)
            return total_descontado + impuestos
        return None

class Sala(models.Model):
    TIPO_SALA_OPCIONES = [
        ('CONS', 'Consulta'),
        ('QUIR', 'Quirófano'),
        ('URG', 'Urgencias'),
        ('HOS', 'Hospitalización'),
        ('LAB', 'Laboratorio'),
        ('ADM', 'Administrativa'),
        ('OTRO', 'Otro'),
    ]
    
    ESTADO_MANTENIMIENTO_OPCIONES = [
        ('OPT', 'Óptimo'),
        ('REG', 'Regular'),
        ('MANT', 'En Mantenimiento'),
        ('REP', 'En Reparación'),
        ('INH', 'Inhabilitada'),
    ]
    
    TIPO_USO_OPCIONES = [
        ('GEN', 'General'),
        ('ESP', 'Especializada'),
        ('CRI', 'Cuidados Críticos'),
        ('DIAG', 'Diagnóstico'),
        ('TRAT', 'Tratamiento'),
    ]
    
    id_sala = models.AutoField(primary_key=True)
    id_paciente = models.ForeignKey(Paciente, on_delete=models.SET_NULL, blank=True, null=True, related_name='salas')
    nombre = models.CharField(max_length=100, blank=True, null=True)
    capacidad = models.IntegerField(default=1, blank=True, null=True)
    tipo = models.CharField(max_length=50, choices=TIPO_SALA_OPCIONES, blank=True, null=True)
    disponibilidad = models.BooleanField(default=True)
    ubicacion = models.CharField(max_length=255, blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    equipamiento = models.TextField(blank=True, null=True)
    estado_mantenimiento = models.CharField(max_length=50, choices=ESTADO_MANTENIMIENTO_OPCIONES, blank=True, null=True)
    fecha_ultima_mantenimiento = models.DateField(blank=True, null=True)
    numero_telefono = models.CharField(max_length=20, blank=True, null=True)
    correo_contacto = models.EmailField(max_length=100, blank=True, null=True)
    codigo_sala = models.CharField(max_length=50, unique=True, blank=True, null=True)
    capacidad_critica = models.IntegerField(blank=True, null=True)
    tipo_uso = models.CharField(max_length=50, choices=TIPO_USO_OPCIONES, blank=True, null=True)
    
    class Meta:
        verbose_name = 'Sala'
        verbose_name_plural = 'Salas'
        ordering = ['tipo', 'nombre']
        indexes = [
            models.Index(fields=['tipo', 'disponibilidad']),
            models.Index(fields=['codigo_sala']),
        ]
    
    def __str__(self):
        return f"{self.codigo_sala or self.id_sala} - {self.nombre} ({self.get_tipo_display()})"
    
    @property
    def esta_disponible(self):
        """Verifica si la sala está disponible"""
        return self.disponibilidad and self.estado_mantenimiento not in ['MANT', 'REP', 'INH']
