from rest_framework.routers import DefaultRouter
from .apiviews import PollViewSet,ChoiceViewSet,VoteViewSet


router = DefaultRouter()
router.register('polls', PollViewSet, base_name='polls')
router.register('choices', ChoiceViewSet, base_name='choices')
router.register('votes', VoteViewSet, base_name='votes')
urlpatterns = [
    # ...
]

urlpatterns += router.urls

