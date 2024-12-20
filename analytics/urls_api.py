from django.urls import path, include


urlpatterns = [
    path("analytics/", include("analytics_core.urls_api"))
]