from django.urls import path
from hcare.glucoses import views


app_name = "glucoses"
urlpatterns = [
    path("", views.GlucoseListView.as_view(), name="list"),
    path("<int:pk>/", views.GlucoseDetailView.as_view(), name="detail"),
    path("add/", views.GlucoseCreateView.as_view(), name="add"),
    path("<int:pk>/update/", views.GlucoseUpdateView.as_view(), name="update"),
    path("<int:pk>/delete/", views.GlucoseDeleteView.as_view(), name='delete'),
]
