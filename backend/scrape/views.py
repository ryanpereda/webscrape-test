from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import QuoteSerializer
from .services import get_quotes


class QuoteListView(APIView):
    def get(self, request):
        data = get_quotes()

        serializer = QuoteSerializer(
            data["quotes"],
            many=True,
        )

        return Response({
            "quotes": serializer.data,
            "count": len(serializer.data),
            "last_scraped_at": data["last_scraped_at"],
            "refreshed": data["refreshed"],
            "refresh_failed": data["refresh_failed"],
            "refresh_in_progress": data["refresh_in_progress"],
        })