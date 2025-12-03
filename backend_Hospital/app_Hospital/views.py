from django.shortcuts import render, redirect, get_object_or_404
from .models import Paciente, Doctor, CitaMedica, Diagnostico, FacturaHospital, Sala
from django.http import HttpResponse

def test_view(request):
    return render(request, 'app_Hospital/test.html')

def inicio_Hospital(request):
    return render(request, 'app_Hospital/inicio.html')

# Vistas para Paciente
def agregar_Paciente(request):
    if request.method == 'POST':
        paciente = Paciente(
            nombre=request.POST['nombre'],
            apellido=request.POST['apellido'],
            fecha_nacimiento=request.POST['fecha_nacimiento'],
            genero=request.POST['genero'],
            direccion=request.POST['direccion'],
            telefono=request.POST['telefono'],
            email=request.POST['email'],
            tipo_sangre=request.POST['tipo_sangre'],
            fecha_registro=request.POST['fecha_registro']
        )
        paciente.save()
        return redirect('ver_Paciente')
    return render(request, 'app_Hospital/Paciente/agregar_Paciente.html')

def ver_Paciente(request):
    pacientes = Paciente.objects.all()
    return render(request, 'app_Hospital/Paciente/ver_Paciente.html', {'pacientes': pacientes})

def actualizar_Paciente(request, id):
    paciente = get_object_or_404(Paciente, id_paciente=id)
    return render(request, 'app_Hospital/Paciente/actualizar_Paciente.html', {'paciente': paciente})

def realizar_actualizacion_Paciente(request, id):
    if request.method == 'POST':
        paciente = get_object_or_404(Paciente, id_paciente=id)
        paciente.nombre = request.POST['nombre']
        paciente.apellido = request.POST['apellido']
        paciente.fecha_nacimiento = request.POST['fecha_nacimiento']
        paciente.genero = request.POST['genero']
        paciente.direccion = request.POST['direccion']
        paciente.telefono = request.POST['telefono']
        paciente.email = request.POST['email']
        paciente.tipo_sangre = request.POST['tipo_sangre']
        paciente.fecha_registro = request.POST['fecha_registro']
        paciente.save()
        return redirect('ver_Paciente')
    return redirect('ver_Paciente')

def borrar_Paciente(request, id):
    paciente = get_object_or_404(Paciente, id_paciente=id)
    paciente.delete()
    return redirect('ver_Paciente')

# Vistas para Doctor
def agregar_Doctor(request):
    if request.method == 'POST':
        doctor = Doctor(
            nombre=request.POST['nombre'],
            apellido=request.POST['apellido'],
            especialidad=request.POST['especialidad'],
            telefono=request.POST['telefono'],
            email=request.POST['email'],
            num_licencia=request.POST['num_licencia'],
            fecha_contratacion=request.POST['fecha_contratacion'],
            salario=request.POST['salario']
        )
        doctor.save()
        return redirect('ver_Doctor')
    return render(request, 'app_Hospital/Doctor/agregar_Doctor.html')

def ver_Doctor(request):
    doctores = Doctor.objects.all()
    return render(request, 'app_Hospital/Doctor/ver_Doctor.html', {'doctores': doctores})

def actualizar_Doctor(request, id):
    doctor = get_object_or_404(Doctor, id_doctor=id)
    return render(request, 'app_Hospital/Doctor/actualizar_Doctor.html', {'doctor': doctor})

def realizar_actualizacion_Doctor(request, id):
    if request.method == 'POST':
        doctor = get_object_or_404(Doctor, id_doctor=id)
        doctor.nombre = request.POST['nombre']
        doctor.apellido = request.POST['apellido']
        doctor.especialidad = request.POST['especialidad']
        doctor.telefono = request.POST['telefono']
        doctor.email = request.POST['email']
        doctor.num_licencia = request.POST['num_licencia']
        doctor.fecha_contratacion = request.POST['fecha_contratacion']
        doctor.salario = request.POST['salario']
        doctor.save()
        return redirect('ver_Doctor')
    return redirect('ver_Doctor')

def borrar_Doctor(request, id):
    doctor = get_object_or_404(Doctor, id_doctor=id)
    doctor.delete()
    return redirect('ver_Doctor')

# Vistas para Cita Medica
def agregar_Cita_Medica(request):
    if request.method == 'POST':
        paciente = get_object_or_404(Paciente, id_paciente=request.POST['id_paciente'])
        doctor = get_object_or_404(Doctor, id_doctor=request.POST['id_doctor'])
        
        cita = CitaMedica(
            id_paciente=paciente,
            id_doctor=doctor,
            fecha_cita=request.POST['fecha_cita'],
            hora_cita=request.POST['hora_cita'],
            motivo=request.POST['motivo'],
            estado=request.POST['estado'],
            observaciones=request.POST['observaciones']
        )
        cita.save()
        return redirect('ver_Cita_Medica')
    
    pacientes = Paciente.objects.all()
    doctores = Doctor.objects.all()
    return render(request, 'app_Hospital/Cita_Medica/agregar_Cita_Medica.html', {
        'pacientes': pacientes,
        'doctores': doctores
    })

def ver_Cita_Medica(request):
    citas = CitaMedica.objects.all()
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
        cita = get_object_or_404(CitaMedica, id_cita=id)
        paciente = get_object_or_404(Paciente, id_paciente=request.POST['id_paciente'])
        doctor = get_object_or_404(Doctor, id_doctor=request.POST['id_doctor'])
        
        cita.id_paciente = paciente
        cita.id_doctor = doctor
        cita.fecha_cita = request.POST['fecha_cita']
        cita.hora_cita = request.POST['hora_cita']
        cita.motivo = request.POST['motivo']
        cita.estado = request.POST['estado']
        cita.observaciones = request.POST['observaciones']
        cita.save()
        return redirect('ver_Cita_Medica')
    return redirect('ver_Cita_Medica')

def borrar_Cita_Medica(request, id):
    cita = get_object_or_404(CitaMedica, id_cita=id)
    cita.delete()
    return redirect('ver_Cita_Medica')

# Vistas para Diagnostico
def agregar_Diagnostico(request):
    if request.method == 'POST':
        cita = get_object_or_404(CitaMedica, id_cita=request.POST['id_cita'])
        
        diagnostico = Diagnostico(
            id_cita=cita,
            descripcion=request.POST['descripcion'],
            tratamiento_recomendado=request.POST['tratamiento_recomendado'],
            nivel_gravedad=request.POST['nivel_gravedad'],
            fecha_registro=request.POST['fecha_registro']
        )
        diagnostico.save()
        return redirect('ver_Diagnostico')
    
    citas = CitaMedica.objects.all()
    return render(request, 'app_Hospital/Diagnostico/agregar_Diagnostico.html', {'citas': citas})

def ver_Diagnostico(request):
    diagnosticos = Diagnostico.objects.all()
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
        diagnostico = get_object_or_404(Diagnostico, id_diagnostico=id)
        cita = get_object_or_404(CitaMedica, id_cita=request.POST['id_cita'])
        
        diagnostico.id_cita = cita
        diagnostico.descripcion = request.POST['descripcion']
        diagnostico.tratamiento_recomendado = request.POST['tratamiento_recomendado']
        diagnostico.nivel_gravedad = request.POST['nivel_gravedad']
        diagnostico.fecha_registro = request.POST['fecha_registro']
        diagnostico.save()
        return redirect('ver_Diagnostico')
    return redirect('ver_Diagnostico')

def borrar_Diagnostico(request, id):
    diagnostico = get_object_or_404(Diagnostico, id_diagnostico=id)
    diagnostico.delete()
    return redirect('ver_Diagnostico')

# Vistas para Factura Hospital
def agregar_Factura_Hospital(request):
    if request.method == 'POST':
        paciente = get_object_or_404(Paciente, id_paciente=request.POST['id_paciente'])
        cita = get_object_or_404(CitaMedica, id_cita=request.POST['id_cita'])
        
        factura = FacturaHospital(
            id_paciente=paciente,
            id_cita=cita,
            total=request.POST['total'],
            estado_pago=request.POST['estado_pago'],
            metodo_pago=request.POST['metodo_pago'],
            fecha_emision=request.POST['fecha_emision'],
            descuento=request.POST['descuento']
        )
        factura.save()
        return redirect('ver_Factura_Hospital')
    
    pacientes = Paciente.objects.all()
    citas = CitaMedica.objects.all()
    return render(request, 'app_Hospital/Factura_Hospital/agregar_Factura_Hospital.html', {
        'pacientes': pacientes,
        'citas': citas
    })

def ver_Factura_Hospital(request):
    facturas = FacturaHospital.objects.all()
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
        factura = get_object_or_404(FacturaHospital, id_factura=id)
        paciente = get_object_or_404(Paciente, id_paciente=request.POST['id_paciente'])
        cita = get_object_or_404(CitaMedica, id_cita=request.POST['id_cita'])
        
        factura.id_paciente = paciente
        factura.id_cita = cita
        factura.total = request.POST['total']
        factura.estado_pago = request.POST['estado_pago']
        factura.metodo_pago = request.POST['metodo_pago']
        factura.fecha_emision = request.POST['fecha_emision']
        factura.descuento = request.POST['descuento']
        factura.save()
        return redirect('ver_Factura_Hospital')
    return redirect('ver_Factura_Hospital')

def borrar_Factura_Hospital(request, id):
    factura = get_object_or_404(FacturaHospital, id_factura=id)
    factura.delete()
    return redirect('ver_Factura_Hospital')

# Vistas para Sala
def agregar_Sala(request):
    if request.method == 'POST':
        sala = Sala(
            nombre=request.POST['nombre'],
            capacidad=request.POST['capacidad'],
            tipo=request.POST['tipo'],
            disponibilidad=request.POST.get('disponibilidad', False)
        )
        sala.save()
        return redirect('ver_Sala')
    return render(request, 'app_Hospital/Sala/agregar_Sala.html')

def ver_Sala(request):
    salas = Sala.objects.all()
    return render(request, 'app_Hospital/Sala/ver_Sala.html', {'salas': salas})

def actualizar_Sala(request, id):
    sala = get_object_or_404(Sala, id_sala=id)
    return render(request, 'app_Hospital/Sala/actualizar_Sala.html', {'sala': sala})

def realizar_actualizacion_Sala(request, id):
    if request.method == 'POST':
        sala = get_object_or_404(Sala, id_sala=id)
        sala.nombre = request.POST['nombre']
        sala.capacidad = request.POST['capacidad']
        sala.tipo = request.POST['tipo']
        sala.disponibilidad = request.POST.get('disponibilidad', False)
        sala.save()
        return redirect('ver_Sala')
    return redirect('ver_Sala')

def borrar_Sala(request, id):
    sala = get_object_or_404(Sala, id_sala=id)
    sala.delete()
    return redirect('ver_Sala')
