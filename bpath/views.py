from django.shortcuts import redirect, render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView

from django.urls import reverse_lazy
from django.views import View
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import Respite

class CustomLoginView(LoginView):
    template_name = 'bpath/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

# Redirects users once they login to the dashboard
    def get_success_url(self):
        return reverse_lazy('dash')

class RegisterPage(FormView):
    template_name = 'bpath/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('dash')

# Functionality for validating registration form
    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)

# Stops logged in user's from accessing login page
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('dash')
        return super(RegisterPage, self).get(*args, **kwargs)

class DashboardList(LoginRequiredMixin, View):
    template_name = 'bpath/dashboard.html'
    def get(self, request):
        return render(request, self.template_name)
    

class RespiteList(LoginRequiredMixin, ListView):
    model = Respite
    context_object_name = 'list_of_respite'

    def get_context_data(self, **kwargs): 
        context = super().get_context_data(**kwargs)
        context['list_of_respite'] = Respite.objects.all() 
        context['list_of_respite'] = context['list_of_respite'].filter(user=self.request.user)
        context['count'] = context['list_of_respite'].filter(complete=False).count()
         
        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['list_of_respite'] = context['list_of_respite'].filter(
                title__icontains=search_input)

        context['search_input'] = search_input

        return context

class RespiteDetail(LoginRequiredMixin, DetailView):
    model = Respite
    context_object_name = 'respite_details'


class RespiteCreate(LoginRequiredMixin, CreateView):
    model = Respite
    fields = ['title', 'staff', 'date', 'start', 'end', 'notes', 'complete']
    success_url = reverse_lazy('respites')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(RespiteCreate, self).form_valid(form)
    
class RespiteUpdate(LoginRequiredMixin, UpdateView):
    model = Respite
    fields = ['title', 'staff', 'date', 'start', 'end', 'notes', 'complete']
    success_url = reverse_lazy('respites')

class DeleteView(LoginRequiredMixin, DeleteView):
    model = Respite
    context_object_name = 'respite_details'
    success_url = reverse_lazy('respites')
