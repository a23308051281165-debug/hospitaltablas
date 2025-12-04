from django.contrib import admin
from .models import Paciente, Doctor, CitaMedica, Diagnostico, FacturaHospital, Sala

@admin.register(Paciente)
class PacienteAdmin(admin.ModelAdmin):
    list_display = ('id_paciente', 'nombre', 'apellido', 'fecha_nacimiento', 'genero', 'telefono', 'numero_identificacion')
    list_filter = ('genero', 'estado_civil', 'tipo_identificacion')
    search_fields = ('nombre', 'apellido', 'numero_identificacion', 'numero_seguro_social')
    ordering = ('apellido', 'nombre')
    list_per_page = 20

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('id_doctor', 'nombre', 'apellido', 'especialidad', 'telefono', 'num_licencia', 'estado_activo')
    list_filter = ('especialidad', 'estado_activo')
    search_fields = ('nombre', 'apellido', 'especialidad', 'num_licencia')
    ordering = ('apellido', 'nombre')
    list_per_page = 20

@admin.register(CitaMedica)
class CitaMedicaAdmin(admin.ModelAdmin):
    list_display = ('id_cita', 'get_paciente', 'get_doctor', 'fecha_cita', 'hora_cita', 'estado', 'tipo_cita')
    list_filter = ('estado', 'tipo_cita', 'prioridad', 'tipo_atencion')
    search_fields = ('id_paciente__nombre', 'id_paciente__apellido', 'id_doctor__nombre', 'id_doctor__apellido')
    ordering = ('-fecha_cita', '-hora_cita')
    list_per_page = 20
    
    def get_paciente(self, obj):
        return f"{obj.id_paciente.nombre} {obj.id_paciente.apellido}"
    get_paciente.short_description = 'Paciente'
    
    def get_doctor(self, obj):
        return f"{obj.id_doctor.nombre} {obj.id_doctor.apellido}"
    get_doctor.short_description = 'Doctor'

@admin.register(Diagnostico)
class DiagnosticoAdmin(admin.ModelAdmin):
    list_display = ('id_diagnostico', 'get_cita', 'codigo_cie10', 'nivel_gravedad', 'estado_diagnostico', 'fecha_registro')
    list_filter = ('nivel_gravedad', 'estado_diagnostico', 'tipo_diagnostico')
    search_fields = ('codigo_cie10', 'codigo_diagnostico', 'especialista_encargado')
    ordering = ('-fecha_registro',)
    list_per_page = 20
    
    def get_cita(self, obj):
        return f"Cita {obj.id_cita.id_cita}"
    get_cita.short_description = 'Cita'

@admin.register(FacturaHospital)
class FacturaHospitalAdmin(admin.ModelAdmin):
    list_display = ('id_factura', 'numero_factura', 'get_paciente', 'total', 'estado_pago', 'metodo_pago', 'fecha_emision')
    list_filter = ('estado_pago', 'metodo_pago', 'tipo_servicio')
    search_fields = ('numero_factura', 'id_paciente__nombre', 'id_paciente__apellido', 'numero_orden')
    ordering = ('-fecha_emision',)
    list_per_page = 20
    
    def get_paciente(self, obj):
        return f"{obj.id_paciente.nombre} {obj.id_paciente.apellido}"
    get_paciente.short_description = 'Paciente'

@admin.register(Sala)
class SalaAdmin(admin.ModelAdmin):
    list_display = ('id_sala', 'codigo_sala', 'nombre', 'tipo', 'disponibilidad', 'capacidad', 'estado_mantenimiento')
    list_filter = ('tipo', 'disponibilidad', 'estado_mantenimiento', 'tipo_uso')
    search_fields = ('codigo_sala', 'nombre', 'ubicacion')
    ordering = ('tipo', 'nombre')
    list_per_page = 20