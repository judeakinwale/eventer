from django.shortcuts import render
from django.core.paginator import Paginator
from django.contrib.auth.forms import UserCreationForm

# Create your views here.


def register(request):
    form = UserCreationForm
    return render(request=request, template_name="registration/register.html", context={"form": form})
