from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Contribution, Story
from django.core.files.storage import default_storage


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "password",)

    def create(self, validated_data):
        user = User(username=validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        return user


class StorySerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    image = serializers.ImageField(required=False)

    class Meta:
        model = Story
        fields = '__all__'

    def create(self, validated_data):
        image = validated_data.pop('image', None)
        story = Story.objects.create(**validated_data)

        if image:
            image_path = f'story_images/{image.name}'
            with default_storage.open(image_path, 'wb+') as destination:
                for chunk in image.chunks():
                    destination.write(chunk)
            story.image = image_path
            story.save()

        return story


class ContributionSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)

    class Meta:
        model = Contribution
        fields = "__all__"

    def validate_text(self, value):
        # Remove the word limit to allow longer contributions
        if len(value) > 5000:  # Example: Limit contribution text to 5000 characters
            raise serializers.ValidationError("Contribution exceeds the character limit of 5000 characters.")
        return value

    def validate(self, data):
        story = data["story"]
        if story.completed:
            raise serializers.ValidationError("No further contribution can be made to the completed story.")

        if story.contributions.count() >= story.max_contributions:
            raise serializers.ValidationError("This story has reached the maximum number of contributions.")

        return data
