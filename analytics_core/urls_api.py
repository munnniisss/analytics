from django.urls import path

from analytics_core.views import CreateAnalyticsRowView


urlpatterns = [
    path("create-analytics-row", CreateAnalyticsRowView.as_view())
]