from django.views.generic import View
from django.shortcuts import render

class HomeView(View):
    #*args y **kwargs hacen referencia a cualqueir parámetro que el request pueda tener
    def get(self, request, *args, **kwargs):
        context = {

        }
        return render(request, 'index.html', context)