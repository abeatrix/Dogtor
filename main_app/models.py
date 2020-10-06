from django.db import models

SHOT = (
    ('1', 'Distemper'),
    ('2', 'Measles'),
    ('3', 'Parainfluenza'),
    ('4', 'Bordatella'),
    ('5', 'Rebies'),
)

# Create your models here.
class Pet(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    age = models.IntegerField()
    dob = models.DateField('date of birth')
    breed = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    owner = models.CharField(max_length=100)
    address = models.TextField(max_length=250)
    image = models.CharField(max_length=100)
    note  = models.TextField(max_length=250)

    def __str__(self):
        return self.name

class Vaccine(models.Model):
    date = models.DateField('vaccine date')
    shot = models.CharField(
        max_length=1,
        choices=SHOT,
        default=SHOT[0][0]
    )
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_shot_display()} on {self.date}"

    class Meta:
        ordering = ['-date']
