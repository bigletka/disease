from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.views.generic import ListView, CreateView
# Create your views here.

def home(request):
    return render(request, 'home.html')

class UsersRegister(CreateView):
    model = Users
    form_class = UsersForm
    template_name = 'users.html'
    def form_valid(self, form): 
        user = form.save()
        return redirect('users_list')

class CountryRegister(CreateView):
    model = Country
    form_class = CountryForm
    template_name = 'country.html'
    def form_valid(self, form): 
        user = form.save()
        return redirect('country_list')

class DiscoverRegister(CreateView):
    model = Discover
    form_class = DiscoverForm
    template_name = 'discovery.html'
    def form_valid(self, form): 
        user = form.save()
        return redirect('discover_list')

class DiseaseRegister(CreateView):
    model = Disease
    form_class = DiseaseForm
    template_name = 'disease.html'
    def form_valid(self, form): 
        user = form.save()
        return redirect('disease_list')

class DiseaseTypeRegister(CreateView):
    model = Diseasetype
    form_class = DiseaseTypeForm
    template_name = 'diseasetype.html'
    def form_valid(self, form): 
        user = form.save()
        return redirect('diseasetype_list')

class DoctorRegister(CreateView):
    model = Doctor
    form_class = DoctorForm
    template_name = 'doctor.html'
    def form_valid(self, form): 
        user = form.save()
        return redirect('doctor_list')

class PublicServantRegister(CreateView):
    model = Publicservant
    form_class = PublicServantForm
    template_name = 'public.html'
    def form_valid(self, form): 
        user = form.save()
        return redirect('public_list')

class RecordRegister(CreateView):
    model = Record
    form_class = RecordForm
    template_name = 'record.html' 
    def form_valid(self, form): 
        user = form.save()
        return redirect('record_list')   

class SpecializeRegister(CreateView):
    model = Specialize
    form_class = SpecializeForm
    template_name = 'specialize.html'
    def form_valid(self, form): 
        user = form.save()
        return redirect('specialize_list')   


class UsersList(ListView):
    model = Users
    template_name = 'users_list.html'

class CountryList(ListView):
    model = Country
    template_name = 'country_list.html'

class DiseaseTypeList(ListView):
    model = Diseasetype
    template_name = 'diseasetype_list.html'

class DiseaseList(ListView):
    model = Disease
    template_name = 'disease_list.html'

class DoctorList(ListView):
    model = Doctor
    template_name = 'doctor_list.html'

class DiscoveryList(ListView):
    model = Discover
    template_name = 'discovery_list.html'

class SpecializeList(ListView):
    model = Specialize
    template_name = 'specialize_list.html'

class PublicServantList(ListView):
    model = Publicservant
    template_name = 'public_list.html'

class RecordList(ListView):
    model = Record
    template_name = 'record_list.html'


def updateUsers(request, pk):
    users = Users.objects.get(email=pk)
    form = UsersForm(request.POST or None, instance=users)

    if request.method=='POST':
        if form.is_valid:
            form.save()
            return redirect('users_list')
    context = {'form':form}
    return render(request, 'users.html', context)

def deleteUsers(request, pk):
    temp = Users.objects.get(email=pk)
    if request.method=='POST':
        temp.delete()
        return redirect('users_list')
    context={'obj':temp}
    return render(request, 'delete.html', context)

def updateCountry(request, pk):
    country = Country.objects.get(cname=pk)
    form = CountryForm(request.POST or None, instance=country)

    if request.method=='POST':
        if form.is_valid:
            form.save()
            return redirect('country_list')
    context = {'form':form}
    return render(request, 'country.html', context)

def deleteCountry(request, pk):
    temp = Country.objects.get(cname=pk)
    if request.method=='POST':
        temp.delete()
        return redirect('country_list')
    context={'obj':temp}
    return render(request, 'delete.html', context)



def updateDiseaseType(request, pk):
    diseasetype = Diseasetype.objects.get(id=pk)
    form = DiseaseTypeForm(request.POST or None, instance=diseasetype)

    if request.method=='POST':
        if form.is_valid:
            form.save()
            return redirect('diseasetype_list')
    context = {'form':form}
    return render(request, 'diseasetype.html', context)


def deleteDiseaseType(request, pk):
    temp = Diseasetype.objects.get(id=pk)
    if request.method=='POST':
        temp.delete()
        return redirect('diseasetype_list')

    context={'obj':temp}
    return render(request, 'delete.html', context)


def updateDisease(request, pk):
    disease = Disease.objects.get(disease_code=pk)
    form = DiseaseForm(request.POST or None, instance=disease)

    if request.method=='POST':
        if form.is_valid:
            form.save()
            return redirect('disease_list')
    context = {'form':form}
    return render(request, 'disease.html', context)

def deleteDisease(request, pk):
    temp = Disease.objects.get(disease_code=pk)
    if request.method=='POST':
        temp.delete()
        return redirect('disease_list')
    context={'obj':temp}
    return render(request, 'delete.html',context)



def updateDiscovery(request, disease_code, cname):
    temp = Discover.objects.get(disease_code=disease_code, cname=cname)
    form = DiscoverForm(request.POST or None, instance=temp)

    if request.method=='POST':
        if form.is_valid:
            form.save()
            return redirect('discovery_list')
    context = {'form':form}
    return render(request, 'discovery.html', context)

def deleteDiscovery(request, disease_code, cname):
    temp = Discover.objects.get(disease_code=disease_code, cname=cname)
    if request.method=='POST':
        temp.delete()
        return redirect('discovery_list')
    context={'obj':temp}
    return render(request, 'delete.html', context)



def updateDoctor(request, pk):
    temp = Doctor.objects.get(email=pk)
    form = DoctorForm(request.POST or None, instance=temp)

    if request.method=='POST':
        if form.is_valid:
            form.save()
            return redirect('doctor_list')
    context = {'form':form}
    return render(request, 'doctor.html', context)

def deleteDoctor(request, pk):
    temp = Doctor.objects.get(email=pk)
    if request.method=='POST':
        temp.delete()
        return redirect('doctor_list')

    context={'obj':temp}
    return render(request, 'delete.html',context)




def updateRecord(request, email, cname, disease_code):
    temp = Record.objects.get(disease_code=disease_code, email=email, cname=cname)
    form = RecordForm(request.POST or None, instance=temp)

    if request.method=='POST':
        if form.is_valid:
            form.save()
            return redirect('record_list')
    context = {'form':form}
    return render(request, 'record.html', context)
    
def deleteRecord(request, email, cname, disease_code):
    temp = Record.objects.get(email=email, cname=cname, disease_code=disease_code)
    if request.method=='POST':
        temp.delete()
        return redirect('record_list')
    context={'obj':temp}
    return render(request, 'delete.html',context)

def updateSpecialize(request, id, email):
    temp = Specialize.objects.get(email=email, id=id)
    form = SpecializeForm(request.POST or None, instance=temp)

    if request.method=='POST':
        if form.is_valid:
            form.save()
            return redirect('specialize_list')
    context = {'form':form}
    return render(request, 'specialize.html', context)

def deleteSpecialize(request, id, email):
    temp = Specialize.objects.get(email=email, id=id)
    if request.method=='POST':
        temp.delete()
        return redirect('specialize_list')
    
    
    context={'obj':temp}
    return render(request, 'delete.html', context)


def updatePublic(request, pk):
    temp = Publicservant.objects.get(email=pk)
    form = PublicServantForm(request.POST or None, instance=temp)

    if request.method=='POST':
        if form.is_valid:
            form.save()
            return redirect('public_list')
    context = {'form':form}
    return render(request, 'public.html', context)

def deletePublic(request, pk):
    temp = Publicservant.objects.get(email=pk)
    if request.method=='POST':
        temp.delete()
        return redirect('public_list')
    context={'obj':temp}
    return render(request, 'delete.html',context)
