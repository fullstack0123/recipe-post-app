from django.urls import path, include  # === 修正 ===

from ..views import StaffroomTemplateView  # === 修正 ===

app_name = "staffroom"

urlpatterns = [
    path("", StaffroomTemplateView.as_view(), name="index"),
    path("recipe/", include("staffroom.urls.recipe", namespace="recipe")),  # === 修正 ===
]
