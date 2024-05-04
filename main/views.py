from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView
from django.views.generic.edit import CreateView

from .forms import UserForm, SuperModelForm, ProductForm
from .models import Purchase


# Create your views here.
def index(request):
    return render(request, "index.html")


@login_required
def main(request):
    purchase = Purchase.objects.all()
    if request.method == 'POST':
        form = ProductForm(request.POST)  # Загрузка данных в форму
        if form.is_valid():
            products = form.cleaned_data['product']
            for product in products:
                product.is_visible = True
                product.save()
            return redirect('main')  # Перенаправление для предотвращения повторной отправки формы
    return render(request, 'main.html', {'purchase': purchase})

class MyDetailView(DetailView):
    model = Purchase
    template_name = 'detail.html'
    context_object_name = 'name'


@login_required
def mainA_Z(request):
    purchase = Purchase.objects.all().order_by("title")
    return render(request, 'mainA-Z.html', {'purchase': purchase})


@login_required
def mainZ_A(request):
    purchase = Purchase.objects.all().order_by("-title")
    return render(request, 'mainZ-A.html', {'purchase': purchase})


@login_required
def main_date(request):
    purchase = Purchase.objects.order_by('date')
    return render(request, 'main_date.html', {'purchase': purchase})


@login_required
def main__date(request):
    purchase = Purchase.objects.order_by('-date')
    return render(request, 'main_date.html', {'purchase': purchase})


class UserRegister(CreateView):
    model = User
    template_name = 'registration/reg.html'
    form_class = UserForm
    success_url = reverse_lazy('login')


def addpurchase(request):
    if request.method == 'POST':
        form = SuperModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main')
    else:
        form = SuperModelForm()
    return render(request, 'addpurchase.html', {'form': form})
