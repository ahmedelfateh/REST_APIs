from rest_framework import serializers

from status.models import Status


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = [
            'id',
            'user',
            'content',
            'image',
        ]
        read_only_fields = ['user']

    def validate(self, data):
        content = data.get('content', None)
        if content == "":
            content = None
        image = data.get("image", None)
        if image is None and content is None:
            raise serializers.ValidationError('Content or Image required.')
        return data
