from django.shortcuts import render
from django.http import JsonResponse
from .models import Contacto
import pandas as pd
from django.http import HttpResponse

def lista_contactos(request):
    if request.method == 'GET':
        query = request.GET.get('q', '')  # Obtiene el parámetro de búsqueda
        contactos = Contacto.objects.all()


        return render(request, 'guia_telefonica/lista_contactos.html', {'contactos': contactos})



def cargar_contactos(request):
    if request.method == 'POST':
        Contacto.objects.all().delete()
        # Obtenemos el archivo subido
        archivo_excel = request.FILES['archivo_excel']
        
        # Leemos el archivo Excel con pandas
        try:
            df = pd.read_excel(archivo_excel)
            # Iteramos sobre las filas del DataFrame
            for index, row in df.iterrows():
                # Crear el contacto en la base de datos
                Contacto.objects.create(
                    no=row['no'],
                    grado=row['grado'],
                    nom_ape=row['nom_ape'],
                    fuerza=row['fuerza'],
                    unidad=row['unidad'],
                    cargo_actual=row['cargo_actual'],
                    tel_oficina=row['tel_oficina'],
                    tel_ip=row['tel_ip'],
                    tel_celular=row['tel_celular'],
                    correo_inst=row['correo_inst'],
                    correo_personal=row['correo_personal']
                )
            return HttpResponse("Contactos cargados correctamente")
        except Exception as e:
            return HttpResponse(f"Error al cargar los contactos: {e}")
    return render(request, 'guia_telefonica/cargar_contactos.html')


