from django.urls import path
from hcare.bloodpressures import views


app_name = "bloodpressures"
urlpatterns = [
    path("", views.BloodPressureListView.as_view(), name="list"),
    path("<int:pk>/", views.BloodPressureDetailView.as_view(), name="detail"),
    path("create/", views.BloodPressureCreateView.as_view(), name="create"),
    path("<int:pk>/update/", views.BloodPressureUpdateView.as_view(), name="update"),
    path("<int:pk>/delete/", views.BloodPressureDeleteView.as_view(), name='delete'),
]
