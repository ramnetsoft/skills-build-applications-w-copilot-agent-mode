from rest_framework import serializers

class UserSerializer(serializers.Serializer):
    id = serializers.CharField()
    email = serializers.EmailField()
    name = serializers.CharField()

class TeamSerializer(serializers.Serializer):
    id = serializers.CharField()
    name = serializers.CharField()
    members = serializers.ListField()

class ActivitySerializer(serializers.Serializer):
    id = serializers.CharField()
    user_id = serializers.CharField()
    type = serializers.CharField()
    duration = serializers.IntegerField()

class LeaderboardSerializer(serializers.Serializer):
    id = serializers.CharField()
    team_id = serializers.CharField()
    score = serializers.IntegerField()

class WorkoutSerializer(serializers.Serializer):
    id = serializers.CharField()
    name = serializers.CharField()
    description = serializers.CharField()
