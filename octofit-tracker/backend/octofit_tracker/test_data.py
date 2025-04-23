# Test data for the Octofit app

test_users = [
    {"username": "john_doe", "email": "john@example.com", "password": "password123"},
    {"username": "jane_smith", "email": "jane@example.com", "password": "password123"},
]

test_teams = [
    {"name": "Team Alpha", "description": "The first team."},
    {"name": "Team Beta", "description": "The second team."},
]

test_activities = [
    {"name": "Running", "calories_burned_per_minute": 10},
    {"name": "Cycling", "calories_burned_per_minute": 8},
]

test_leaderboard = [
    {"user": "john_doe", "points": 150},
    {"user": "jane_smith", "points": 200},
]

test_workouts = [
    {"user": "john_doe", "activity": "Running", "duration_minutes": 30},
    {"user": "jane_smith", "activity": "Cycling", "duration_minutes": 45},
]
