# from django.shortcuts import render

from django.db.models import QuerySet
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin

from .models import BloodPressure


class BloodPressureListView(LoginRequiredMixin, ListView):
    model = BloodPressure

    def get_queryset(self) -> QuerySet:
        return self.model.objects.filter(user=self.request.user)


class BloodPressureDetailView(LoginRequiredMixin, DetailView):
    model = BloodPressure

    def get_queryset(self) -> QuerySet:
        return self.model.objects.filter(user=self.request.user)


class BloodPressureCreateView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    model = BloodPressure
    fields = ['systolic', 'diastolic', 'pulse', 'notes']
    success_url = reverse_lazy('bloodpressures:list')
    success_message = 'Record created successfully.'

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        # form.fields['recorded'].widget = DateTimeInput(
        #     attrs={'type': 'datetime-local', 'class': 'form-control'}
        # )
        return form

    def form_valid(self, form):
        bloodpressure = form.save(commit=False)
        bloodpressure.user = self.request.user
        bloodpressure.save()
        return super().form_valid(form)


class BloodPressureUpdateView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = BloodPressure
    fields = ['systolic', 'diastolic', 'pulse', 'notes']
    template_name = 'bloodpressures/bloodpressure_update_form.html'  # nadpisany template
    success_url = reverse_lazy('bloodpressures:list')
    success_message = 'Record updated successfully.'


class BloodPressureDeleteView(SuccessMessageMixin, LoginRequiredMixin, DeleteView):
    model = BloodPressure
    success_url = reverse_lazy('bloodpressures:list')


