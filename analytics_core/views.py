import json

from django.http import JsonResponse
from rest_framework import status
from rest_framework.views import APIView

from analytics_core.serializer import CreateAnalyticsRowSerializer
from analytics_core.tasks import create_analytics_row_task

class CreateAnalyticsRowView(APIView):
    def post(self, request, format=None):
        serializer = CreateAnalyticsRowSerializer(data=request.data)

        if not serializer.is_valid():
            return JsonResponse(data={"status": "error", "error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

        print("СТартую таску")

        serializer.validated_data['created_at'] = serializer.validated_data['created_at'].isoformat()
        result = create_analytics_row_task.delay(data=serializer.validated_data)

        return JsonResponse(data={"status": "ok", "task_id": result.id}, status=status.HTTP_200_OK)
