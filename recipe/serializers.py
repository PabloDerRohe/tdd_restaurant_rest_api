from rest_framework import serializers

from core.models import Tag, Ingredient, Recipe


class TagSerializer(serializers.ModelSerializer):
    """
    Serializer for tag model
    """
    class Meta:
        model = Tag
        fields = ('id', 'name')
        read_only_Fields = ('id',)
     
        
class IngredientSerializer(serializers.ModelSerializer):
    """
    Serializer for ingredient model
    """
    class Meta:
        model = Ingredient
        fields = ('id', 'name')
        read_only_Fields = ('id',)
        
        
class RecipeSerializer(serializers.ModelSerializer):
    """
    Serializer for recipe model
    """
    ingredients = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Ingredient.objects.all()
    )
    
    tags = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Tag.objects.all()
    )
    
    class Meta:
        model = Recipe
        fields = (
            'id', 'title', 'ingredients', 'tags',
            'time_minutes', 'price', 'link',
        )
        read_only_Fields = ('id',)