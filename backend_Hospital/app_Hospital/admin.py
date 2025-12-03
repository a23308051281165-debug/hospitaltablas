from django.contrib import admin
from .models import Paciente, Doctor, CitaMedica, Diagnostico, FacturaHospital, Sala

@admin.register(Paciente)
class PacienteAdmin(admin.ModelAdmin):
    list_display = ('id_paciente', 'nombre', 'apellido', 'telefono', 'email', 'fecha_registro')
    search_fields = ('nombre', 'apellido', 'telefono')

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('id_doctor', 'nombre', 'apellido', 'especialidad', 'telefono', 'fecha_contratacion')
    search_fields = ('nombre', 'apellido', 'especialidad')

@admin.register(CitaMedica)
class CitaMedicaAdmin(admin.ModelAdmin):
    list_display = ('id_cita', 'id_paciente', 'id_doctor', 'fecha_cita', 'hora_cita', 'estado')
    list_filter = ('estado', 'fecha_cita')

@admin.register(Diagnostico)
class DiagnosticoAdmin(admin.ModelAdmin):
    list_display = ('id_diagnostico', 'id_cita', 'nivel_gravedad', 'fecha_registro')
    list_filter = ('nivel_gravedad', 'fecha_registro')

@admin.register(FacturaHospital)
class FacturaHospitalAdmin(admin.ModelAdmin):
    list_display = ('id_factura', 'id_paciente', 'total', 'estado_pago', 'fecha_emision')
    list_filter = ('estado_pago', 'fecha_emision')

@admin.register(Sala)
class SalaAdmin(admin.ModelAdmin):
    list_display = ('id_sala', 'nombre', 'capacidad', 'tipo', 'disponibilidad')
    list_filter = ('tipo', 'disponibilidad')