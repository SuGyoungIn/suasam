from ..models import Movie,Genre
from rest_framework import serializers



class MovieSerializer(serializers.ModelSerializer):
    
    class GenresSerializers(serializers.ModelSerializer):
        class Meta:
            model = Genre
            fields = ('name',)

    genre_ids = GenresSerializers(many=True,read_only=True)

    class Meta:
        model = Movie
        fields = '__all__'
        

class FindMovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('id','title','original_title','poster_path')

