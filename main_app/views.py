from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import Pet
from .forms import Pet_Form, Vaccine_Form

# Define the home view
def home(request):
  return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def api(request):
    return JsonResponse({"status":200})

# index and create
def pets_index(request):
  if request.method == 'POST':
    pet_form = Pet_Form(request.POST)
    if pet_form.is_valid():
      pet_form.save()
      return redirect('pet_index')
  pets = Pet.objects.all()
  pet_form = Pet_Form()
  context = {'pets': pets, 'pet_form': pet_form}
  return render(request, 'pets/index.html', context)


# show
def pets_detail(request, pet_id):
  pet = Pet.objects.get(id=pet_id)
  vaccine_form = Vaccine_Form()
  context = {'pet': pet, 'vaccine_form': vaccine_form}
  return render(request, 'pets/detail.html', context)

# edit && update
def pets_edit(request, pet_id):
  pet = Pet.objects.get(id=pet_id)
  if request.method == 'POST':
    pet_form = Pet_Form(request.POST, instance=pet)
    if pet_form.is_valid():
      pet_form.save()
      return redirect('detail', pet_id=pet_id)
  else:
    # in form(instance=The object that we pull back from db)
    pet_form = Pet_Form(instance=pet)
  context = {'pet': pet, 'pet_form': pet_form}
  return render(request, 'pets/edit.html', context)

# delete
def pets_delete(request, pet_id):
    Pet.objects.get(id=pet_id).delete()
    return redirect("pets_index")

def add_vaccine(request, pet_id):
    vaccine_form = Vaccine_Form(request.POST)
    if vaccine_form.is_valid():
        new_vaccine = vaccine_form.save(commit=False)
        new_vaccine.pet_id = pet_id
        new_vaccine.save()
    return redirect('detail', pet_id=pet_id)

