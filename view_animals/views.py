from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView
from django.urls import reverse_lazy

from view_animals.models import Animal, Shelter
from view_animals.forms import AnimalForm, AnimalFormSet


class ShowAnimals(View):
    def get(self, request, shelter_id, *args, **kwargs):
        shelter = Shelter.objects.get(id=shelter_id)
        animals = Animal.objects.filter(shelter=shelter)
        all_count = animals.count()
        return render(request, 'user_pages/main_page.html', {
            'shelter': shelter, 'animals': animals, 'all_count': all_count})


class SheltersView(View):
    def get(self, request):
        shelters = Shelter.objects.all()
        animals = Animal.objects.all()
        all_animals_count = animals.count()
        return render(request, 'shelter_pages/main_page.html', context={
            'shelters': shelters, 'animals': animals, 'count': all_animals_count})


class AnimalView(View):
    def get(self, request, animal_id):
        animal = Animal.objects.get(id=animal_id)
        return render(request, 'animal_pages/info.html', context={
            'animal': animal, 'animal_id': animal_id})


class AnimalFormView(TemplateView):

    template_name = 'animal_pages/register.html'

    def get(self, *args, **kwargs):
        formset = AnimalFormSet(queryset=Animal.objects.none())
        return self.render_to_response({'animal_formset': formset})

    def post(self, *args, **kwargs):
        formset = AnimalFormSet(data=self.request.POST)
        if formset.is_valid():
            formset.save()
            return HttpResponseRedirect('/main_page')
        return self.render_to_response({'animal_formset': formset})


class AnimalEditFormView(View):
    def get(self, request, animal_id):
        animal = Animal.objects.get(id=animal_id)
        animal_form = AnimalForm(instance=animal)
        return render(request, 'animal_pages/edit.html', context={'animal_form': animal_form, 'animal_id': animal_id})

    def post(self, request, animal_id):
        animal = Animal.objects.get(id=animal_id)
        animal_form = AnimalForm(request.POST, instance=animal)

        if animal_form.is_valid():
            animal.save()
            return HttpResponseRedirect(f'/animals/{animal_id}')
        return render(request, 'animal_pages/edit.html', context={'animal_form': animal_form, 'animal_id': animal_id})
