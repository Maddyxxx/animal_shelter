from view_animals.models import Animal
from django.forms import modelformset_factory, ModelForm


class AnimalForm(ModelForm):
    class Meta:
        model = Animal
        fields = '__all__'


AnimalFormSet = modelformset_factory(Animal, fields='__all__', extra=1)