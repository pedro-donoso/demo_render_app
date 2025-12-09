# from django.shortcuts import render, redirect

# from .forms import RegistroForm

# from .models import Registro


# def home(request):
#     if request.method == "POST":
#         form = RegistroForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('home')
#     else:
#         form = RegistroForm()

#     registros = Registro.objects.all()
#     return render(request, 'home.html', {'form': form, 'registros': registros})

from django.shortcuts import render, redirect

from .forms import RegistroForm

from .models import Registro

def home(request):
    if request.method == "POST":
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = RegistroForm()

    registros = Registro.objects.all()
    return render(request, 'home.html', {'form': form, 'registros': registros})

