from . import views
from django.urls import path

urlpatterns = [path('', views.index, name="index"),
               path('main/', views.main, name="main"),
               path('registr/', views.UserRegister.as_view()),
               path('<int:pk>', views.MyDetailView.as_view(), name='mydetail'),
               path('A-Z/', views.mainA_Z),
               path('Z-A/', views.mainZ_A),
               path('date/', views.main_date),
               path('addpurchase/', views.addpurchase),
               path('-date/', views.main__date),
               ]
