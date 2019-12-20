from django.http import Http404

from .models import Topic

def check_topic_owner(topic, request):
    if topic.owner != request.user:
        raise Http404
