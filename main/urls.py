from . import views
from django.urls import path

from .views import SearchResultsView

urlpatterns = [path('', views.index, name="index"),
               path('main/', views.main, name="main"),
               path('registr/', views.UserRegister.as_view(), name='registrate'),
               path('<int:pk>', views.MyDetailView.as_view(), name='mydetail'),
               path('<int:pk>/delete', views.MyDetailView.as_view(), name='mydetaildelete'),
               path('A-Z/', views.mainA_Z, name='main_A-Z'),
               path('Z-A/', views.mainZ_A, name='main_Z-A'),
               path('date/', views.main_date, name='main_date'),
               path('addpurchase/', views.addpurchase, name='add'),
               path('-date/', views.main__date, name='main_-date'),
               path('search/', SearchResultsView, name='search_results'),
               ]
