from django.forms import ModelForm
from .models import Pet, Vaccine


class Pet_Form(ModelForm):
    class Meta:
        model = Pet
        fields = ['name', 'gender', 'age', 'dob', 'breed', 'color', 'owner', 'address', 'image', 'note']

class Vaccine_Form(ModelForm):
    class Meta:
        model = Vaccine
        fields = ['date', 'shot']
