from django.urls import path,include
from.import views
urlpatterns = [
    # path('test',views.Testfn,name="test"),
    path('',views.html1 , name='homepage'),
    path('html2',views.html2, name='loginpage')
]