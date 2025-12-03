from django.urls import path
from . import views

urlpatterns = [
    path('test/', views.test_view, name='test'),
    path('', views.inicio_Hospital, name='inicio_Hospital'),
    
    # URLs para Paciente
    path('agregar_paciente/', views.agregar_Paciente, name='agregar_Paciente'),
    path('ver_paciente/', views.ver_Paciente, name='ver_Paciente'),
    path('actualizar_paciente/<int:id>/', views.actualizar_Paciente, name='actualizar_Paciente'),
    path('realizar_actualizacion_paciente/<int:id>/', views.realizar_actualizacion_Paciente, name='realizar_actualizacion_Paciente'),
    path('borrar_paciente/<int:id>/', views.borrar_Paciente, name='borrar_Paciente'),
    
    # URLs para Doctor
    path('agregar_doctor/', views.agregar_Doctor, name='agregar_Doctor'),
    path('ver_doctor/', views.ver_Doctor, name='ver_Doctor'),
    path('actualizar_doctor/<int:id>/', views.actualizar_Doctor, name='actualizar_Doctor'),
    path('realizar_actualizacion_doctor/<int:id>/', views.realizar_actualizacion_Doctor, name='realizar_actualizacion_Doctor'),
    path('borrar_doctor/<int:id>/', views.borrar_Doctor, name='borrar_Doctor'),
    
    # URLs para Cita Medica
    path('agregar_cita_medica/', views.agregar_Cita_Medica, name='agregar_Cita_Medica'),
    path('ver_cita_medica/', views.ver_Cita_Medica, name='ver_Cita_Medica'),
    path('actualizar_cita_medica/<int:id>/', views.actualizar_Cita_Medica, name='actualizar_Cita_Medica'),
    path('realizar_actualizacion_cita_medica/<int:id>/', views.realizar_actualizacion_Cita_Medica, name='realizar_actualizacion_Cita_Medica'),
    path('borrar_cita_medica/<int:id>/', views.borrar_Cita_Medica, name='borrar_Cita_Medica'),
    
    # URLs para Diagnostico
    path('agregar_diagnostico/', views.agregar_Diagnostico, name='agregar_Diagnostico'),
    path('ver_diagnostico/', views.ver_Diagnostico, name='ver_Diagnostico'),
    path('actualizar_diagnostico/<int:id>/', views.actualizar_Diagnostico, name='actualizar_Diagnostico'),
    path('realizar_actualizacion_diagnostico/<int:id>/', views.realizar_actualizacion_Diagnostico, name='realizar_actualizacion_Diagnostico'),
    path('borrar_diagnostico/<int:id>/', views.borrar_Diagnostico, name='borrar_Diagnostico'),
    
    # URLs para Factura Hospital
    path('agregar_factura_hospital/', views.agregar_Factura_Hospital, name='agregar_Factura_Hospital'),
    path('ver_factura_hospital/', views.ver_Factura_Hospital, name='ver_Factura_Hospital'),
    path('actualizar_factura_hospital/<int:id>/', views.actualizar_Factura_Hospital, name='actualizar_Factura_Hospital'),
    path('realizar_actualizacion_factura_hospital/<int:id>/', views.realizar_actualizacion_Factura_Hospital, name='realizar_actualizacion_Factura_Hospital'),
    path('borrar_factura_hospital/<int:id>/', views.borrar_Factura_Hospital, name='borrar_Factura_Hospital'),
    
    # URLs para Sala
    path('agregar_sala/', views.agregar_Sala, name='agregar_Sala'),
    path('ver_sala/', views.ver_Sala, name='ver_Sala'),
    path('actualizar_sala/<int:id>/', views.actualizar_Sala, name='actualizar_Sala'),
    path('realizar_actualizacion_sala/<int:id>/', views.realizar_actualizacion_Sala, name='realizar_actualizacion_Sala'),
    path('borrar_sala/<int:id>/', views.borrar_Sala, name='borrar_Sala'),
]