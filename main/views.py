from datetime import datetime

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q
from django.http import Http404, HttpResponseRedirect, HttpResponse
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
    purchase = Purchase.objects.all().filter(user=request.user)
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

    def get_object(self, queryset=None):
        if queryset is None:
            queryset = self.get_queryset()
        obj = super().get_object(queryset=queryset)
        if obj.user != self.request.user:
            raise Http404("Нет записей")
        return obj

    def post(self, request, *args, **kwargs):

        self.object = self.get_object()

        if "delete" in request.POST:
            self.object.delete()

            return HttpResponseRedirect(reverse_lazy('main'))
        #
        return super().get(request, *args, **kwargs)


@login_required
def mainA_Z(request):
    purchase = Purchase.objects.all().order_by("title").filter(user=request.user)
    if request.method == 'POST':
        form = ProductForm(request.POST)  # Загрузка данных в форму
        if form.is_valid():
            products = form.cleaned_data['product']
            for product in products:
                product.is_visible = True
                product.save()
            return redirect('main')  # Перенаправление для предотвращения повторной отправки формы
    return render(request, 'mainA-Z.html', {'purchase': purchase})


@login_required
def mainZ_A(request):
    purchase = Purchase.objects.all().order_by("-title").filter(user=request.user)
    if request.method == 'POST':
        form = ProductForm(request.POST)  # Загрузка данных в форму
        if form.is_valid():
            products = form.cleaned_data['product']
            for product in products:
                product.is_visible = True
                product.save()
            return redirect('main')  # Перенаправление для предотвращения повторной отправки формы
    return render(request, 'mainZ-A.html', {'purchase': purchase})


@login_required
def main_date(request):
    purchase = Purchase.objects.order_by('date').filter(user=request.user)
    if request.method == 'POST':
        form = ProductForm(request.POST)  # Загрузка данных в форму
        if form.is_valid():
            products = form.cleaned_data['product']
            for product in products:
                product.is_visible = True
                product.save()
            return redirect('main')  # Перенаправление для предотвращения повторной отправки формы
    return render(request, 'main_date.html', {'purchase': purchase})


@login_required
def main__date(request):
    purchase = Purchase.objects.order_by('-date').filter(user=request.user)
    if request.method == 'POST':
        form = ProductForm(request.POST)  # Загрузка данных в форму
        if form.is_valid():
            products = form.cleaned_data['product']
            for product in products:
                product.is_visible = True
                product.save()
            return redirect('main')  # Перенаправление для предотвращения повторной отправки формы
    return render(request, 'main_date.html', {'purchase': purchase})


class UserRegister(CreateView):
    model = User
    template_name = 'registration/reg.html'
    form_class = UserForm
    success_url = reverse_lazy('login')


@login_required
def addpurchase(request):
    if request.method == 'POST':

        form = SuperModelForm(request.POST, request.FILES)
        if form.is_valid():
            purchase = form.save(commit=False)
            date = request.POST.get('date', None)
            if date:
                try:
                    # Преобразование строки даты в объект datetime
                    date = datetime.strptime(date, '%Y-%m-%dT%H:%M')
                except ValueError:
                    messages.error(request, "Неправильный формат даты.")
                    return redirect("main")
            purchase.user = request.user
            purchase.save()
            return redirect("main")
    else:
        form = SuperModelForm()
    return render(request, 'addpurchase.html', {'form': form})


@login_required
def SearchResultsView(request):
    query = request.GET.get('q')
    purchase = Purchase.objects.all().filter(
        Q(title__icontains=query)
    ).filter(user=request.user)
    return render(request, 'main.html', {'purchase': purchase})