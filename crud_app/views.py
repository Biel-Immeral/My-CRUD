from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import User
from django.urls import reverse_lazy


def  crud_list(request):
    user = User.objects.all()
    return render(request, "crud_app/user_list.html", {"user": user})
    
class crud_create_view(CreateView):
    model = User
    fields = ['user_name', 'user_email', 'user_phone']
    success_url = reverse_lazy("crud_list")

class crud_update_view(UpdateView):
    model = User
    fields = ['user_name', 'user_email', 'user_phone']
    success_url = reverse_lazy("crud_list")

class crud_delete_view(DeleteView):
    model = User
    success_url = reverse_lazy("crud_list")
    