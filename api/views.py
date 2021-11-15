from rest_framework import viewsets
from rest_framework.response import Response

from .models import Feed
from .serializer import FeedSerializer
from .parsers import get_feed_data


class FeedDataViewSet(viewsets.ModelViewSet):
    queryset = Feed.objects.all()
    serializer_class = FeedSerializer

    def retrieve(self, request, pk=None):
        url = Feed.objects.get(pk=pk)
        feed_data = get_feed_data(url)
        return Response(feed_data)