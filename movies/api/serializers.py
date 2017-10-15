from rest_framework.serializers import ModelSerializer
from movies.models import Movies,Actor,Director

class MovieListSerializer(ModelSerializer):
    class Meta:
        model = Movies
        depth = 1
        fields = [
            'id',
            'name',
            'cover_image_url',
            'release_date',
            'genre',
            'lead_actors',
            'director'
        ]

class MovieRetrieveSerializer(ModelSerializer):
    class Meta:
        model = Movies
        depth = 1
        fields = [
            'id',
            'name',
            'cover_image_url',
            'release_date',
            'genre',
            'lead_actors',
            'director'
        ]

class MovieUpdateSerializer(ModelSerializer):
    class Meta:
        model = Movies
        depth = 1
        fields = [
            'id',
            'name',
            'cover_image_url',
            'release_date',
            'genre',
            'lead_actors',
            'director'
        ]

class MovieDeleteSerializer(ModelSerializer):
    class Meta:
        model = Movies
        depth = 1
        fields = [
            'id',
            'name',
            'cover_image_url',
            'release_date',
            'genre',
            'lead_actors',
            'director'
        ]
