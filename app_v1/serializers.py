from rest_framework import serializers

from app_v1.models import Score

class ScoreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Score
        fields = ('name', 'score', 'date_created')

class FileUploadSerializer(serializers.Serializer):
    file = serializers.FileField()

    class Meta:
        fields = ('file',)