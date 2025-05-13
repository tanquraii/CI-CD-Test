
from django.urls import path
from . import views
urlpatterns = [
    path('',views.CatUserView.as_view()),
    path('<int:id>',views.CatUserDetailsView.as_view())
]