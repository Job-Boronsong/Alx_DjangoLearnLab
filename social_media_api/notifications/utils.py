from .models import Notification
from django.contrib.contenttypes.models import ContentType

def create_notification(recipient, actor, verb, target=None):
    content_type = None
    object_id = None
    if target:
        content_type = ContentType.objects.get_for_model(target)
        object_id = target.id

    Notification.objects.create(
        recipient=recipient,
        actor=actor,
        verb=verb,
        content_type=content_type,
        object_id=object_id
    )
