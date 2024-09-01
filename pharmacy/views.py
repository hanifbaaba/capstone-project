from django.shortcuts import render
from .models import Medicine, Prescription

def home(request):
    medicines = Medicine.objects.all()
    return render(request, 'pharmacy/home.html', {'medicines': medicines})

def prescription_list(request):
    prescriptions = Prescription.objects.all()
    return render(request, 'pharmacy/prescriptions.html', {'prescriptions': prescriptions})
