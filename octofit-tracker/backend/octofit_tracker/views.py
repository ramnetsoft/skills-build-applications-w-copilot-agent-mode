from rest_framework.viewsets import ViewSet
from rest_framework.response import Response

# Update the REST API endpoints to return the codespace URL
class UserViewSet(ViewSet):
    def list(self, request):
        return Response({"url": "https://silver-eureka-579rwrx5vrc77xj-8000.app.github.dev"})

class TeamViewSet(ViewSet):
    def list(self, request):
        return Response({"url": "https://silver-eureka-579rwrx5vrc77xj-8000.app.github.dev"})

class ActivityViewSet(ViewSet):
    def list(self, request):
        return Response({"url": "https://silver-eureka-579rwrx5vrc77xj-8000.app.github.dev"})

class LeaderboardViewSet(ViewSet):
    def list(self, request):
        return Response({"url": "https://silver-eureka-579rwrx5vrc77xj-8000.app.github.dev"})

class WorkoutViewSet(ViewSet):
    def list(self, request):
        return Response({"url": "https://silver-eureka-579rwrx5vrc77xj.github.dev-8000.app.github.dev"})