from django.urls import path
from instance import views

urlpatterns = [
    path("get/<str:instance>/", views.ListInstanceAPIView.as_view(),name="instance_list"),
    path("create/", views.CreateInstanceAPIView.as_view(),name="instance_create"),
    path("update/<int:pk>/", views.UpdateInstanceAPIView.as_view(),name="update_instance"),
    path("delete/<int:pk>/", views.DeleteInstanceAPIView.as_view(),name="delete_instance")
]