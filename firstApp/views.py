from django.shortcuts import render
from django.http import JsonResponse

def employeeView(request):
    emp ={
        'id': 123,
        'name': 'Binod',
        'sal': '100000'
    }
    return JsonResponse(emp)
