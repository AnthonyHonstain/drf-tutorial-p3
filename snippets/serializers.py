from django.forms import widgets
from rest_framework import serializers
from snippets.models import Snippet


class SnippetSerializer(serializers.Serializer):
    pk = serializers.Field()
    title = serializers.CharField(required=False, max_length=100)
    code = serializers.CharField(widget=widgets.Textarea, max_length=100000)

    def restore_object(self, attrs, instance=None):
        """
        Create or update a new snippet instance, given a dictionary
        of deserialized field values.

        If we didn't define restore_object, then deserializing would
        simply return a dictionary of items.
        """
        if instance:
            # Update existing instance
            instance.title = attrs.get('title', instance.title)
            instance.code = attrs.get('code', instance.code)
            return instance

        return Snippet(**attrs)
