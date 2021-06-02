from django.urls import path,include
from.import views
urlpatterns = [
    # path('test',views.Testfn,name="test"),
    path('',views.home , name='homepage'),
    path('login',views.login, name='loginpage'),
    path('register',views.register,name='registerpage')
]