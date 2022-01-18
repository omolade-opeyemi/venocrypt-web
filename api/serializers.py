from rest_framework import serializers

class FileSerializer(serializers.Serializer):
   """Your data serializer, define your fields here."""
   password = serializers.CharField(max_length=255)
   outputName = serializers.CharField(max_length=255)
   file = serializers.FileField()

class TextSerializer(serializers.Serializer):
   password = serializers.CharField(max_length=255)
   text = serializers.CharField()
