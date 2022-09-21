from django.shortcuts import render
import requests,json
from django.http import HttpResponse

# Create your views here.

def index(request):
    iban = request.POST.get('iban_get', False)
    id = request.POST.get('id', False)
    devise = request.POST.get('devise', False)
    date = request.POST.get('date', False)
    source = request.POST.get('source', False)
    destination = request.POST.get('destination', False)
    type = request.POST.get('type', False)
    all = request.POST.get('all', False)
    if iban :
        ret = requests.get('http://178.32.130.54:8080/Compte/'+iban).content
        return HttpResponse(ret)

    if all:
        ret = requests.get('http://178.32.130.54:8080/transaction/all').content
        return HttpResponse(ret)
    elif id :
        ret = requests.get('http://178.32.130.54:8080/transaction/id/'+id).content
        return HttpResponse(ret)
    elif date:
        ret = requests.get('http://178.32.130.54:8080/transaction/date/'+date).content
        return HttpResponse(ret)
    elif source:
        ret = requests.get('http://178.32.130.54:8080/transaction/source/'+source).content
        return HttpResponse(ret)
    elif destination:
        ret = requests.get('http://178.32.130.54:8080/transaction/destination/'+destination).content
        return HttpResponse(ret)
    elif devise:
        ret = requests.get('http://178.32.130.54:8080/transaction/devise/'+devise).content
        return HttpResponse(ret)
    elif type:
        ret = requests.get('http://178.32.130.54:8080/transaction/type/'+type).content
        return HttpResponse(ret)
    return render(request, 'index.html')

def add_compte(request):
    iban = request.POST.get('iban', False)
    type = request.POST.get('type', False)
    frais = request.POST.get('frais', False)
    interet = request.POST.get('interet', False)
    if iban :
        data = {"iban" : iban , "type" : type, "frais" : frais, "interet" : interet}
        requests.post('http://178.32.130.54:8080/Compte',json=data)
    return render(request, 'add_compte.html')

def add_transaction(request):
    id = request.POST.get('id', False)
    ibanfrom = request.POST.get('ibanfrom', False)
    ibanto = request.POST.get('ibanto', False)
    type = request.POST.get('type', False)
    montant = request.POST.get('montant', False)
    devise = request.POST.get('devise', False)
    date = request.POST.get('date', False)
    if id :
        data = {"id" : int(id) , "type" : type, "source" : ibanfrom, "destination" : ibanto,"montant" : montant, "date" : date, "devise" : devise}
        requests.post('http://178.32.130.54:8080/transaction',json=data)
    return render(request, 'add_transaction.html')

def update_compte(request):
    iban = request.POST.get('iban', False)
    type = request.POST.get('type', False)
    frais = request.POST.get('frais', False)
    interet = request.POST.get('interet', False)
    if iban :
        data = {"iban" : iban , "type" : type, "frais" : frais, "interet" : interet}
        requests.put('http://178.32.130.54:8080/Compte/'+iban,json=data)
    return render(request, 'update_compte.html')

def update_transaction(request):
    id = request.POST.get('id', False)
    ibanfrom = request.POST.get('ibanfrom', False)
    ibanto = request.POST.get('ibanto', False)
    type = request.POST.get('type', False)
    montant = request.POST.get('montant', False)
    devise = request.POST.get('devise', False)
    date = request.POST.get('date', False)
    if id :
        data = {"id" : int(id) , "type" : type, "source" : ibanfrom, "destination" : ibanto,"montant" : montant, "date" : date, "devise" : devise}
        requests.put('http://178.32.130.54:8080/transaction/'+id,json=data)
    return render(request, 'update_transaction.html')

def delete_compte(request):
    iban = request.POST.get('iban', False)
    if iban :
        requests.delete('http://178.32.130.54:8080/Compte/'+iban)
    return render(request, 'delete_compte.html')

def delete_transaction(request):
    id = request.POST.get('id', False)
    if id :
        requests.delete('http://178.32.130.54:8080/transaction/'+id)
    return render(request, 'delete_transaction.html')

