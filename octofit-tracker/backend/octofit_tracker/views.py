from rest_framework.viewsets import ViewSet
from rest_framework.response import Response

class UserViewSet(ViewSet):
    def list(self, request):
        return Response([])

class TeamViewSet(ViewSet):
    def list(self, request):
        return Response([])

class ActivityViewSet(ViewSet):
    def list(self, request):
        return Response([])

class LeaderboardViewSet(ViewSet):
    def list(self, request):
        return Response([])

class WorkoutViewSet(ViewSet):
    def list(self, request):
        return Response([])