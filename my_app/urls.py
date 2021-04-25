from django.urls import path,include
from.import views
urlpatterns = [
    path('test',views.Testfn,name="test"),
    path('html1',views.html1)
]