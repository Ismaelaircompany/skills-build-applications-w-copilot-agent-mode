from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class SimpleModelTest(TestCase):
    def test_team_creation(self):
        team = Team.objects.create(name='Marvel', universe='Marvel')
        self.assertEqual(team.name, 'Marvel')
    def test_user_creation(self):
        team = Team.objects.create(name='DC', universe='DC')
        user = User.objects.create(name='Clark Kent', email='clark@dc.com', team=team)
        self.assertEqual(user.team.name, 'DC')
