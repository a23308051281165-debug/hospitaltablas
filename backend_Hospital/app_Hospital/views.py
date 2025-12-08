# app_Hospital/views.py - VERSIÓN CORREGIDA
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Paciente, Doctor, CitaMedica, Diagnostico, FacturaHospital, Sala

# ==================== VISTA PRINCIPAL ====================
def inicio_Hospital(request):
    return render(request, 'app_Hospital/inicio.html')

# ==================== PACIENTE ====================
def agregar_Paciente(request):
    if request.method == 'POST':
        paciente = Paciente()
        paciente.nombre = request.POST.get('nombre')
        paciente.apellido = request.POST.get('apellido')
        paciente.fecha_nacimiento = request.POST.get('fecha_nacimiento')
        paciente.genero = request.POST.get('genero')
        paciente.direccion = request.POST.get('direccion')
        paciente.telefono = request.POST.get('telefono')
        paciente.email = request.POST.get('email')
        paciente.tipo_sangre = request.POST.get('tipo_sangre')
        paciente.estado_civil = request.POST.get('estado_civil')
        paciente.ocupacion = request.POST.get('ocupacion')
        paciente.nacionalidad = request.POST.get('nacionalidad')
        paciente.numero_seguro_social = request.POST.get('numero_seguro_social')
        paciente.tipo_identificacion = request.POST.get('tipo_identificacion')
        paciente.numero_identificacion = request.POST.get('numero_identificacion')
        paciente.save()
        return redirect('ver_Paciente')
    return render(request, 'app_Hospital/Paciente/agregar_Paciente.html')

def ver_Paciente(request):
    pacientes = Paciente.objects.all().order_by('apellido', 'nombre')
    return render(request, 'app_Hospital/Paciente/ver_Paciente.html', {'pacientes': pacientes})

def actualizar_Paciente(request, id):
    paciente = get_object_or_404(Paciente, id_paciente=id)
    return render(request, 'app_Hospital/Paciente/actualizar_Paciente.html', {'paciente': paciente})

def realizar_actualizacion_Paciente(request, id):
    if request.method == 'POST':
        paciente = Paciente.objects.get(id_paciente=id)
        paciente.nombre = request.POST.get('nombre')
        paciente.apellido = request.POST.get('apellido')
        paciente.fecha_nacimiento = request.POST.get('fecha_nacimiento')
        paciente.genero = request.POST.get('genero')
        paciente.direccion = request.POST.get('direccion')
        paciente.telefono = request.POST.get('telefono')
        paciente.email = request.POST.get('email')
        paciente.tipo_sangre = request.POST.get('tipo_sangre')
        paciente.estado_civil = request.POST.get('estado_civil')
        paciente.ocupacion = request.POST.get('ocupacion')
        paciente.nacionalidad = request.POST.get('nacionalidad')
        paciente.numero_seguro_social = request.POST.get('numero_seguro_social')
        paciente.tipo_identificacion = request.POST.get('tipo_identificacion')
        paciente.numero_identificacion = request.POST.get('numero_identificacion')
        paciente.save()
    return redirect('ver_Paciente')

def borrar_Paciente(request, id):
    paciente = get_object_or_404(Paciente, id_paciente=id)
    if request.method == 'POST':
        paciente.delete()
        return redirect('ver_Paciente')
    return render(request, 'app_Hospital/Paciente/borrar_Paciente.html', {'paciente': paciente})

# ==================== DOCTOR ====================
def agregar_Doctor(request):
    if request.method == 'POST':
        doctor = Doctor()
        doctor.nombre = request.POST.get('nombre')
        doctor.apellido = request.POST.get('apellido')
        doctor.especialidad = request.POST.get('especialidad')
        doctor.telefono = request.POST.get('telefono')
        doctor.email = request.POST.get('email')
        doctor.num_licencia = request.POST.get('num_licencia')
        doctor.fecha_contratacion = request.POST.get('fecha_contratacion')
        doctor.salario = request.POST.get('salario')
        doctor.horario_trabajo = request.POST.get('horario_trabajo')
        doctor.direccion_clinica = request.POST.get('direccion_clinica')
        doctor.experiencia_anios = request.POST.get('experiencia_anios')
        doctor.certificaciones = request.POST.get('certificaciones')
        doctor.idiomas = request.POST.get('idiomas')
        doctor.estado_activo = request.POST.get('estado_activo') == 'on'
        doctor.save()
        return redirect('ver_Doctor')
    return render(request, 'app_Hospital/Doctor/agregar_Doctor.html')

def ver_Doctor(request):
    doctores = Doctor.objects.all().order_by('apellido', 'nombre')
    return render(request, 'app_Hospital/Doctor/ver_Doctor.html', {'doctores': doctores})

def actualizar_Doctor(request, id):
    doctor = get_object_or_404(Doctor, id_doctor=id)
    return render(request, 'app_Hospital/Doctor/actualizar_Doctor.html', {'doctor': doctor})

def realizar_actualizacion_Doctor(request, id):
    if request.method == 'POST':
        doctor = Doctor.objects.get(id_doctor=id)
        doctor.nombre = request.POST.get('nombre')
        doctor.apellido = request.POST.get('apellido')
        doctor.especialidad = request.POST.get('especialidad')
        doctor.telefono = request.POST.get('telefono')
        doctor.email = request.POST.get('email')
        doctor.num_licencia = request.POST.get('num_licencia')
        doctor.fecha_contratacion = request.POST.get('fecha_contratacion')
        doctor.salario = request.POST.get('salario')
        doctor.horario_trabajo = request.POST.get('horario_trabajo')
        doctor.direccion_clinica = request.POST.get('direccion_clinica')
        doctor.experiencia_anios = request.POST.get('experiencia_anios')
        doctor.certificaciones = request.POST.get('certificaciones')
        doctor.idiomas = request.POST.get('idiomas')
        doctor.estado_activo = request.POST.get('estado_activo') == 'on'
        doctor.save()
    return redirect('ver_Doctor')

def borrar_Doctor(request, id):
    doctor = get_object_or_404(Doctor, id_doctor=id)
    if request.method == 'POST':
        doctor.delete()
        return redirect('ver_Doctor')
    return render(request, 'app_Hospital/Doctor/borrar_Doctor.html', {'doctor': doctor})

# ==================== CITA MÉDICA ====================
def agregar_Cita_Medica(request):
    if request.method == 'POST':
        cita = CitaMedica()
        cita.id_paciente = Paciente.objects.get(id_paciente=request.POST.get('id_paciente'))
        cita.id_doctor = Doctor.objects.get(id_doctor=request.POST.get('id_doctor'))
        cita.fecha_cita = request.POST.get('fecha_cita')
        cita.hora_cita = request.POST.get('hora_cita')
        cita.duracion_minutos = request.POST.get('duracion_minutos')
        cita.motivo = request.POST.get('motivo')
        cita.estado = request.POST.get('estado')
        cita.observaciones = request.POST.get('observaciones')
        cita.tipo_cita = request.POST.get('tipo_cita')
        cita.lugar_cita = request.POST.get('lugar_cita')
        cita.tipo_atencion = request.POST.get('tipo_atencion')
        cita.prioridad = request.POST.get('prioridad')
        cita.costo_consulta = request.POST.get('costo_consulta')
        cita.medio_reserva = request.POST.get('medio_reserva')
        cita.save()
        return redirect('ver_Cita_Medica')
    
    pacientes = Paciente.objects.all()
    doctores = Doctor.objects.all()
    return render(request, 'app_Hospital/Cita_Medica/agregar_Cita_Medica.html', {
        'pacientes': pacientes,
        'doctores': doctores
    })

def ver_Cita_Medica(request):
    citas = CitaMedica.objects.all().order_by('-fecha_cita', '-hora_cita')
    return render(request, 'app_Hospital/Cita_Medica/ver_Cita_Medica.html', {'citas': citas})

def actualizar_Cita_Medica(request, id):
    cita = get_object_or_404(CitaMedica, id_cita=id)
    pacientes = Paciente.objects.all()
    doctores = Doctor.objects.all()
    return render(request, 'app_Hospital/Cita_Medica/actualizar_Cita_Medica.html', {
        'cita': cita,
        'pacientes': pacientes,
        'doctores': doctores
    })

def realizar_actualizacion_Cita_Medica(request, id):
    if request.method == 'POST':
        cita = CitaMedica.objects.get(id_cita=id)
        cita.id_paciente = Paciente.objects.get(id_paciente=request.POST.get('id_paciente'))
        cita.id_doctor = Doctor.objects.get(id_doctor=request.POST.get('id_doctor'))
        cita.fecha_cita = request.POST.get('fecha_cita')
        cita.hora_cita = request.POST.get('hora_cita')
        cita.duracion_minutos = request.POST.get('duracion_minutos')
        cita.motivo = request.POST.get('motivo')
        cita.estado = request.POST.get('estado')
        cita.observaciones = request.POST.get('observaciones')
        cita.tipo_cita = request.POST.get('tipo_cita')
        cita.lugar_cita = request.POST.get('lugar_cita')
        cita.tipo_atencion = request.POST.get('tipo_atencion')
        cita.prioridad = request.POST.get('prioridad')
        cita.costo_consulta = request.POST.get('costo_consulta')
        cita.medio_reserva = request.POST.get('medio_reserva')
        cita.save()
    return redirect('ver_Cita_Medica')

def borrar_Cita_Medica(request, id):
    cita = get_object_or_404(CitaMedica, id_cita=id)
    if request.method == 'POST':
        cita.delete()
        return redirect('ver_Cita_Medica')
    return render(request, 'app_Hospital/Cita_Medica/borrar_Cita_Medica.html', {'cita': cita})

# ==================== DIAGNÓSTICO ====================
def agregar_Diagnostico(request):
    if request.method == 'POST':
        diagnostico = Diagnostico()
        diagnostico.id_cita = CitaMedica.objects.get(id_cita=request.POST.get('id_cita'))
        diagnostico.codigo_cie10 = request.POST.get('codigo_cie10')
        diagnostico.resultado_examen = request.POST.get('resultado_examen')
        diagnostico.descripcion = request.POST.get('descripcion')
        diagnostico.tratamiento_recomendado = request.POST.get('tratamiento_recomendado')
        diagnostico.nivel_gravedad = request.POST.get('nivel_gravedad')
        diagnostico.codigo_diagnostico = request.POST.get('codigo_diagnostico')
        diagnostico.estado_diagnostico = request.POST.get('estado_diagnostico')
        diagnostico.especialista_encargado = request.POST.get('especialista_encargado')
        diagnostico.comentarios = request.POST.get('comentarios')
        diagnostico.seguimiento = request.POST.get('seguimiento')
        diagnostico.tipo_diagnostico = request.POST.get('tipo_diagnostico')
        diagnostico.recomendaciones = request.POST.get('recomendaciones')
        diagnostico.save()
        return redirect('ver_Diagnostico')
    
    citas = CitaMedica.objects.all()
    return render(request, 'app_Hospital/Diagnostico/agregar_Diagnostico.html', {'citas': citas})

def ver_Diagnostico(request):
    diagnosticos = Diagnostico.objects.all().order_by('-fecha_registro')
    return render(request, 'app_Hospital/Diagnostico/ver_Diagnostico.html', {'diagnosticos': diagnosticos})

def actualizar_Diagnostico(request, id):
    diagnostico = get_object_or_404(Diagnostico, id_diagnostico=id)
    citas = CitaMedica.objects.all()
    return render(request, 'app_Hospital/Diagnostico/actualizar_Diagnostico.html', {
        'diagnostico': diagnostico,
        'citas': citas
    })

def realizar_actualizacion_Diagnostico(request, id):
    if request.method == 'POST':
        diagnostico = Diagnostico.objects.get(id_diagnostico=id)
        diagnostico.id_cita = CitaMedica.objects.get(id_cita=request.POST.get('id_cita'))
        diagnostico.codigo_cie10 = request.POST.get('codigo_cie10')
        diagnostico.resultado_examen = request.POST.get('resultado_examen')
        diagnostico.descripcion = request.POST.get('descripcion')
        diagnostico.tratamiento_recomendado = request.POST.get('tratamiento_recomendado')
        diagnostico.nivel_gravedad = request.POST.get('nivel_gravedad')
        diagnostico.codigo_diagnostico = request.POST.get('codigo_diagnostico')
        diagnostico.estado_diagnostico = request.POST.get('estado_diagnostico')
        diagnostico.especialista_encargado = request.POST.get('especialista_encargado')
        diagnostico.comentarios = request.POST.get('comentarios')
        diagnostico.seguimiento = request.POST.get('seguimiento')
        diagnostico.tipo_diagnostico = request.POST.get('tipo_diagnostico')
        diagnostico.recomendaciones = request.POST.get('recomendaciones')
        diagnostico.save()
    return redirect('ver_Diagnostico')

def borrar_Diagnostico(request, id):
    diagnostico = get_object_or_404(Diagnostico, id_diagnostico=id)
    if request.method == 'POST':
        diagnostico.delete()
        return redirect('ver_Diagnostico')
    return render(request, 'app_Hospital/Diagnostico/borrar_Diagnostico.html', {'diagnostico': diagnostico})

# ==================== FACTURA HOSPITAL ====================
def agregar_Factura_Hospital(request):
    if request.method == 'POST':
        factura = FacturaHospital()
        factura.id_paciente = Paciente.objects.get(id_paciente=request.POST.get('id_paciente'))
        cita_id = request.POST.get('id_cita')
        if cita_id:
            factura.id_cita = CitaMedica.objects.get(id_cita=cita_id)
        factura.total = request.POST.get('total')
        factura.estado_pago = request.POST.get('estado_pago')
        factura.descuento = request.POST.get('descuento') or 0
        factura.impuestos = request.POST.get('impuestos') or 0
        factura.descripcion_servicios = request.POST.get('descripcion_servicios')
        factura.metodo_pago = request.POST.get('metodo_pago')
        factura.numero_factura = request.POST.get('numero_factura')
        factura.codigo_autorizacion = request.POST.get('codigo_autorizacion')
        factura.tipo_servicio = request.POST.get('tipo_servicio')
        factura.numero_orden = request.POST.get('numero_orden')
        factura.referencia_pago = request.POST.get('referencia_pago')
        factura.comentarios_adicionales = request.POST.get('comentarios_adicionales')
        factura.save()
        return redirect('ver_Factura_Hospital')
    
    pacientes = Paciente.objects.all()
    citas = CitaMedica.objects.all()
    return render(request, 'app_Hospital/Factura_Hospital/agregar_Factura_Hospital.html', {
        'pacientes': pacientes,
        'citas': citas
    })

def ver_Factura_Hospital(request):
    facturas = FacturaHospital.objects.all().order_by('-fecha_emision')
    return render(request, 'app_Hospital/Factura_Hospital/ver_Factura_Hospital.html', {'facturas': facturas})

def actualizar_Factura_Hospital(request, id):
    factura = get_object_or_404(FacturaHospital, id_factura=id)
    pacientes = Paciente.objects.all()
    citas = CitaMedica.objects.all()
    return render(request, 'app_Hospital/Factura_Hospital/actualizar_Factura_Hospital.html', {
        'factura': factura,
        'pacientes': pacientes,
        'citas': citas
    })

def realizar_actualizacion_Factura_Hospital(request, id):
    if request.method == 'POST':
        factura = FacturaHospital.objects.get(id_factura=id)
        factura.id_paciente = Paciente.objects.get(id_paciente=request.POST.get('id_paciente'))
        cita_id = request.POST.get('id_cita')
        if cita_id:
            factura.id_cita = CitaMedica.objects.get(id_cita=cita_id)
        factura.total = request.POST.get('total')
        factura.estado_pago = request.POST.get('estado_pago')
        factura.descuento = request.POST.get('descuento') or 0
        factura.impuestos = request.POST.get('impuestos') or 0
        factura.descripcion_servicios = request.POST.get('descripcion_servicios')
        factura.metodo_pago = request.POST.get('metodo_pago')
        factura.numero_factura = request.POST.get('numero_factura')
        factura.codigo_autorizacion = request.POST.get('codigo_autorizacion')
        factura.tipo_servicio = request.POST.get('tipo_servicio')
        factura.numero_orden = request.POST.get('numero_orden')
        factura.referencia_pago = request.POST.get('referencia_pago')
        factura.comentarios_adicionales = request.POST.get('comentarios_adicionales')
        factura.save()
    return redirect('ver_Factura_Hospital')

def borrar_Factura_Hospital(request, id):
    factura = get_object_or_404(FacturaHospital, id_factura=id)
    if request.method == 'POST':
        factura.delete()
        return redirect('ver_Factura_Hospital')
    return render(request, 'app_Hospital/Factura_Hospital/borrar_Factura_Hospital.html', {'factura': factura})

# ==================== SALA ====================
def agregar_Sala(request):
    if request.method == 'POST':
        sala = Sala()
        
        paciente_id = request.POST.get('id_paciente')
        if paciente_id:
            sala.id_paciente = Paciente.objects.get(id_paciente=paciente_id)

        sala.nombre = request.POST.get('nombre')
        sala.capacidad = request.POST.get('capacidad')
        sala.tipo = request.POST.get('tipo')
        sala.disponibilidad = request.POST.get('disponibilidad') == 'on'
        sala.ubicacion = request.POST.get('ubicacion')
        sala.descripcion = request.POST.get('descripcion')
        sala.equipamiento = request.POST.get('equipamiento')
        sala.estado_mantenimiento = request.POST.get('estado_mantenimiento')
        sala.fecha_ultima_mantenimiento = request.POST.get('fecha_ultima_mantenimiento')
        sala.numero_telefono = request.POST.get('numero_telefono')
        sala.correo_contacto = request.POST.get('correo_contacto')
        sala.codigo_sala = request.POST.get('codigo_sala')
        sala.capacidad_critica = request.POST.get('capacidad_critica')
        sala.tipo_uso = request.POST.get('tipo_uso')
        sala.save()
        return redirect('ver_Sala')
    
    pacientes = Paciente.objects.all().order_by('apellido', 'nombre')
    return render(request, 'app_Hospital/Sala/agregar_Sala.html', {'pacientes': pacientes})

def ver_Sala(request):
    salas = Sala.objects.select_related('id_paciente').all().order_by('tipo', 'nombre')
    return render(request, 'app_Hospital/Sala/ver_Sala.html', {'salas': salas})

def actualizar_Sala(request, id):
    sala = get_object_or_404(Sala, id_sala=id)
    pacientes = Paciente.objects.all().order_by('apellido', 'nombre')
    return render(request, 'app_Hospital/Sala/actualizar_Sala.html', {
        'sala': sala,
        'pacientes': pacientes
    })

def realizar_actualizacion_Sala(request, id):
    if request.method == 'POST':
        sala = Sala.objects.get(id_sala=id)
        
        # Asignar paciente
        paciente_id = request.POST.get('id_paciente')
        if paciente_id:
            sala.id_paciente = Paciente.objects.get(id_paciente=paciente_id)
        else:
            sala.id_paciente = None

        sala.nombre = request.POST.get('nombre')
        sala.capacidad = request.POST.get('capacidad')
        sala.tipo = request.POST.get('tipo')
        sala.disponibilidad = request.POST.get('disponibilidad') == 'on'
        sala.ubicacion = request.POST.get('ubicacion')
        sala.descripcion = request.POST.get('descripcion')
        sala.equipamiento = request.POST.get('equipamiento')
        sala.estado_mantenimiento = request.POST.get('estado_mantenimiento')
        sala.fecha_ultima_mantenimiento = request.POST.get('fecha_ultima_mantenimiento')
        sala.numero_telefono = request.POST.get('numero_telefono')
        sala.correo_contacto = request.POST.get('correo_contacto')
        sala.codigo_sala = request.POST.get('codigo_sala')
        sala.capacidad_critica = request.POST.get('capacidad_critica')
        sala.tipo_uso = request.POST.get('tipo_uso')
        sala.save()
    return redirect('ver_Sala')

def borrar_Sala(request, id):
    sala = get_object_or_404(Sala, id_sala=id)
    if request.method == 'POST':
        sala.delete()
        return redirect('ver_Sala')
    return render(request, 'app_Hospital/Sala/borrar_Sala.html', {'sala': sala})