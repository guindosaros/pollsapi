# apiviews.py
# ...
from rest_framework import viewsets
from rest_framework import filters
from .models import Poll, Choice,Vote
from .serializers import PollSerializer, ChoiceSerializer, VoteSerializer

class DynamicSearchFilter(filters.SearchFilter):
    def get_search_fields(self, view, request):
        return request.GET.getlist('search_fields', [])

class PollViewSet(viewsets.ModelViewSet):
    filter_backends = (DynamicSearchFilter,)
    queryset = Poll.objects.all()
    serializer_class = PollSerializer
    
    
    
class ChoiceViewSet(viewsets.ModelViewSet):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer
    
class VoteViewSet(viewsets.ModelViewSet):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer
    
    