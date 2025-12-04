from django.urls import path
from . import views

urlpatterns = [
    # Vista principal - CORREGIDO
    path('', views.inicio_Hospital, name='inicio_Hospital'),
    
    # ============ PACIENTE ============
    path('paciente/agregar/', views.agregar_Paciente, name='agregar_Paciente'),
    path('paciente/ver/', views.ver_Paciente, name='ver_Paciente'),
    path('paciente/actualizar/<int:id>/', views.actualizar_Paciente, name='actualizar_Paciente'),
    path('paciente/realizar_actualizacion/<int:id>/', views.realizar_actualizacion_Paciente, name='realizar_actualizacion_Paciente'),
    # FALTA LA RUTA PARA ELIMINAR - AÑADIR:
    path('paciente/eliminar/<int:id>/', views.borrar_Paciente, name='borrar_Paciente'),
    
    # ============ DOCTOR ============
    path('doctor/agregar/', views.agregar_Doctor, name='agregar_Doctor'),
    path('doctor/ver/', views.ver_Doctor, name='ver_Doctor'),
    path('doctor/actualizar/<int:id>/', views.actualizar_Doctor, name='actualizar_Doctor'),
    path('doctor/realizar_actualizacion/<int:id>/', views.realizar_actualizacion_Doctor, name='realizar_actualizacion_Doctor'),
    # FALTA LA RUTA PARA ELIMINAR - AÑADIR:
    path('doctor/eliminar/<int:id>/', views.borrar_Doctor, name='borrar_Doctor'),
    
    # ============ CITA MÉDICA ============
    path('cita-medica/agregar/', views.agregar_Cita_Medica, name='agregar_Cita_Medica'),
    path('cita-medica/ver/', views.ver_Cita_Medica, name='ver_Cita_Medica'),
    path('cita-medica/actualizar/<int:id>/', views.actualizar_Cita_Medica, name='actualizar_Cita_Medica'),
    path('cita-medica/realizar_actualizacion/<int:id>/', views.realizar_actualizacion_Cita_Medica, name='realizar_actualizacion_Cita_Medica'),
    # FALTA LA RUTA PARA ELIMINAR - AÑADIR:
    path('cita-medica/eliminar/<int:id>/', views.borrar_Cita_Medica, name='borrar_Cita_Medica'),
    
    # ============ DIAGNÓSTICO ============
    path('diagnostico/agregar/', views.agregar_Diagnostico, name='agregar_Diagnostico'),
    path('diagnostico/ver/', views.ver_Diagnostico, name='ver_Diagnostico'),
    path('diagnostico/actualizar/<int:id>/', views.actualizar_Diagnostico, name='actualizar_Diagnostico'),
    path('diagnostico/realizar_actualizacion/<int:id>/', views.realizar_actualizacion_Diagnostico, name='realizar_actualizacion_Diagnostico'),
    # FALTA LA RUTA PARA ELIMINAR - AÑADIR:
    path('diagnostico/eliminar/<int:id>/', views.borrar_Diagnostico, name='borrar_Diagnostico'),
    
    # ============ FACTURA HOSPITAL ============
    path('factura/agregar/', views.agregar_Factura_Hospital, name='agregar_Factura_Hospital'),
    path('factura/ver/', views.ver_Factura_Hospital, name='ver_Factura_Hospital'),
    path('factura/actualizar/<int:id>/', views.actualizar_Factura_Hospital, name='actualizar_Factura_Hospital'),
    path('factura/realizar_actualizacion/<int:id>/', views.realizar_actualizacion_Factura_Hospital, name='realizar_actualizacion_Factura_Hospital'),
    # FALTA LA RUTA PARA ELIMINAR - AÑADIR:
    path('factura/eliminar/<int:id>/', views.borrar_Factura_Hospital, name='borrar_Factura_Hospital'),
    
    # ============ SALA ============
    path('sala/agregar/', views.agregar_Sala, name='agregar_Sala'),
    path('sala/ver/', views.ver_Sala, name='ver_Sala'),
    path('sala/actualizar/<int:id>/', views.actualizar_Sala, name='actualizar_Sala'),
    path('sala/realizar_actualizacion/<int:id>/', views.realizar_actualizacion_Sala, name='realizar_actualizacion_Sala'),
    # FALTA LA RUTA PARA ELIMINAR - AÑADIR:
    path('sala/eliminar/<int:id>/', views.borrar_Sala, name='borrar_Sala'),
]