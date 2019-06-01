from django.urls import path
from . import views

app_name = 'money'

urlpatterns = [
                path('', views.MainView.as_view(), name='index'),
                path('<int:year>/<int:month>', views.MainView.as_view(), name='index'),
                path('edit/<int:num>', views.edit, name='edit'),
                path('delete/<int:num>', views.delete, name='delete'),
                path('find', views.find, name='find'),
                path('for_learn',views.for_learn,name="for_learn"),
                #path('edit/<int:num>', views.MainView.as_view(), name='edit'),
                ]
