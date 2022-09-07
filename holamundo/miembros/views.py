import json
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotAllowed, HttpResponseBadRequest
from .models import Member

def index(request):
    return HttpResponse("Hola, mundo")

def new(request):
    print("Method: ", request.method)
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
    #    print(data)
    #    print(type(data))
            member = Member(
                id = data['doc'],
                name = data['nombre'],
                email = data['email']
            )
            member.save()
            return HttpResponse("Está registrando datos.")
        except:
            return HttpResponseBadRequest("Error en los datos enviados.")
    else:
        return HttpResponseNotAllowed(["POST"], "Método inválido.")

def read(request):
    if request.method == 'GET':
        members = Member.objects.all()
        allMembersData = []
        #print(members)
        for x in members:
            memberData = {"documento": x.id, "nombre": x.name, "correo": x.email}
            allMembersData.append(memberData)
        #print(json.dumps(allMembersData))

        #    print(x.id)
        #    print(x.name)
        #    print(x.email)
        resp = HttpResponse()
        resp.headers['Content-Type'] = 'text/json'
        resp.content = json.dumps(allMembersData)
        return resp           
    #    return HttpResponse(allMembersData)
    #    return HttpResponse("Está consultando datos.")
    else:
        return HttpResponseNotAllowed(["GET"], "Método inválido")
    

#    print(request)
#    print(dir(request))
#    print("Headers: ", request.headers)
#    print("Method: ", request.method)
#    print("Body: ", request.body)
#    print("Path: ", request.path)
    
#def ruta1(request):
#    return HttpResponse("Hola, acá ruta 1")

#def ruta2(request):
#    return HttpResponse("Hola, acá ruta 2")

#def datosPacientes(request):
#    return HttpResponse("Acá irá la información de los pacientes")
