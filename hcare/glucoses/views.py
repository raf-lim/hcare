from django.shortcuts import render

from django.db.models import QuerySet
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.forms import DateTimeInput
from .models import Glucose


class GlucoseListView(LoginRequiredMixin, ListView):
    model = Glucose

    def get_queryset(self) -> QuerySet:
        return self.model.objects.filter(user=self.request.user)


class GlucoseDetailView(LoginRequiredMixin, DetailView):
    model = Glucose

    def get_queryset(self) -> QuerySet:
        return self.model.objects.filter(user=self.request.user)


class GlucoseCreateView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    model = Glucose
    fields = ['glucose', 'recorded', 'notes']
    # success_url = reverse_lazy('glucoses:list') # get url from model absolute url in template
    success_message = 'Record created successfully.'

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['recorded'].widget = DateTimeInput(
            attrs={'type': 'datetime-local', 'class': 'form-control'}
        )
        return form

    def form_valid(self, form):
        glucose = form.save(commit=False)
        glucose.user = self.request.user
        glucose.save()
        return super().form_valid(form)


class GlucoseUpdateView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = Glucose
    fields = ['glucose', 'recorded', 'notes']
    template_name = 'glucoses/glucose_update_form.html'  # nadpisany template
    success_url = reverse_lazy('glucoses:list')
    success_message = 'Record updated successfully.'


class GlucoseDeleteView(SuccessMessageMixin, LoginRequiredMixin, DeleteView):
    model = Glucose
    success_url = reverse_lazy('glucoses:list')

