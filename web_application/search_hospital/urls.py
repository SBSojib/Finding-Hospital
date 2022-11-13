from django.urls import path
from . import views

urlpatterns = [
    path('', views.hi, name='home_page'),
    path('test/', views.test_page, name='test_page'),
    path('show_hospital/', views.show_hospital, name='hospital'),
    path('choose_specialist/show_specialist/', views.show_specialist, name='specialist'),
    path('choose_specialist/', views.choose_specialist, name='choose_specialist'),
    path('choose_surgery/', views.choose_surgery, name='choose_surgery'),
    path('choose_surgery/show_surgery/', views.show_surgery, name='show_surgery'),
    path('choose_diagonosis/', views.choose_diagonosis, name='choose_diagonosis'),
    path('choose_diagonosis/show_diagonosis/', views.show_diagonosis, name='show_diagonosis'),
    #path('show/hospital_details/', views.hospital_details, name='hospital_details')
]