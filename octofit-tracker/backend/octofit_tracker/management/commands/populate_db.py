from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard
from django.utils import timezone
from pymongo import MongoClient

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Limpa dados existentes
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Workout.objects.all().delete()
        Leaderboard.objects.all().delete()

        # Times
        marvel = Team.objects.create(name='Marvel', universe='Marvel')
        dc = Team.objects.create(name='DC', universe='DC')

        # Usuários
        tony = User.objects.create(name='Tony Stark', email='tony@marvel.com', team=marvel)
        steve = User.objects.create(name='Steve Rogers', email='steve@marvel.com', team=marvel)
        clark = User.objects.create(name='Clark Kent', email='clark@dc.com', team=dc)
        diana = User.objects.create(name='Diana Prince', email='diana@dc.com', team=dc)

        # Atividades
        Activity.objects.create(user=tony, type='Corrida', duration=30, date=timezone.now().date())
        Activity.objects.create(user=steve, type='Bicicleta', duration=45, date=timezone.now().date())
        Activity.objects.create(user=clark, type='Natação', duration=60, date=timezone.now().date())
        Activity.objects.create(user=diana, type='Yoga', duration=50, date=timezone.now().date())

        # Workouts
        Workout.objects.create(name='Treino Marvel', description='Treino intenso para heróis Marvel', suggested_for='Marvel')
        Workout.objects.create(name='Treino DC', description='Treino de força para heróis DC', suggested_for='DC')
        Workout.objects.create(name='Treino Universal', description='Treino para todos os heróis', suggested_for='Ambos')

        # Leaderboard
        Leaderboard.objects.create(team=marvel, points=150)
        Leaderboard.objects.create(team=dc, points=170)

        # Índice único em email (coleção users)
        client = MongoClient('mongodb://localhost:27017/')
        db = client['octofit_db']
        db.users.create_index([('email', 1)], unique=True)
        client.close()

        self.stdout.write(self.style.SUCCESS('Banco octofit_db populado com dados de teste!'))
