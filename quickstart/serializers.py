from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import MediaFile, Media, Cast


class UploadMediaSerializer(ModelSerializer):
    genre = serializers.CharField(max_length=50, required=False)
    media_type = serializers.CharField(max_length=10, required=False)
    cast = serializers.ListField(required=False)

    class Meta:
        model = MediaFile
        fields = ('name', 'description', 'thumbnail', 'video_url', 'genre',
                  'media_type', 'cast')

    def create(self, validated_data):
        name = validated_data.get("name")
        genre = validated_data.pop("genre")
        casts = validated_data.pop("cast")
        media_type = validated_data.pop("media_type")
        instance = super(UploadMediaSerializer, self).create(validated_data)
        instance.save()
        media_obj = Media.objects.create(
            name=name,
            genre=genre,
            media_type=media_type,
            media_file=instance
        )
        for cast in casts:
            media_obj.cast.add(
                Cast.objects.get(id=cast)
            )
        return instance


class CastSerializer(ModelSerializer):

    class Meta:
        model = Cast
        fields = ('actor_name',)


class GetMediaSerializer(ModelSerializer):
    genre = serializers.SerializerMethodField()
    cast = serializers.SerializerMethodField()

    class Meta:
        model = MediaFile
        fields = ('name', 'description', 'thumbnail', 'video_url', 'genre',
                  'cast')

    def get_genre(self, obj):
        genre = obj.file.first().genre
        return genre

    def get_cast(self, obj):
        media_obj = obj.file.first()
        casts = media_obj.cast.all()
        return CastSerializer(casts, many=True).data

