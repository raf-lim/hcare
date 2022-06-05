from django.urls import path
from hcare.bloodpressures import views


app_name = "bloodpressures"
urlpatterns = [
    path("", views.BloodPressureListView.as_view(), name="list"),
    path("<int:pk>/", views.BloodPressureDetailView.as_view(), name="detail"),
    path("add/", views.BloodPressureCreateView.as_view(), name="add"),
    path("<int:pk>/update/", views.BloodPressureUpdateView.as_view(), name="update"),
    path("<int:pk>/delete/", views.BloodPressureDeleteView.as_view(), name='delete'),
]
