from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        Leaderboard.objects.all().delete()
        Activity.objects.all().delete()
        Workout.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()

        # Create Teams
        marvel = Team.objects.create(name='marvel', description='Marvel Superheroes')
        dc = Team.objects.create(name='dc', description='DC Superheroes')

        # Create Users
        users = [
            User.objects.create(name='Spider-Man', email='spiderman@marvel.com', team='marvel'),
            User.objects.create(name='Iron Man', email='ironman@marvel.com', team='marvel'),
            User.objects.create(name='Batman', email='batman@dc.com', team='dc'),
            User.objects.create(name='Wonder Woman', email='wonderwoman@dc.com', team='dc'),
        ]

        # Create Workouts
        workouts = [
            Workout.objects.create(name='Web Swing', description='Swing between buildings', suggested_for='marvel'),
            Workout.objects.create(name='Suit Training', description='Train with Iron Man suit', suggested_for='marvel'),
            Workout.objects.create(name='Gadget Training', description='Train with gadgets', suggested_for='dc'),
            Workout.objects.create(name='Amazonian Strength', description='Strength training', suggested_for='dc'),
        ]

        # Create Activities
        Activity.objects.create(user=users[0], type='swing', duration=30, date=timezone.now().date())
        Activity.objects.create(user=users[1], type='fly', duration=45, date=timezone.now().date())
        Activity.objects.create(user=users[2], type='fight', duration=60, date=timezone.now().date())
        Activity.objects.create(user=users[3], type='train', duration=50, date=timezone.now().date())

        # Create Leaderboard
        leaderboard_entries = [
            Leaderboard.objects.create(user=users[0], score=100, rank=1),
            Leaderboard.objects.create(user=users[1], score=90, rank=2),
            Leaderboard.objects.create(user=users[2], score=80, rank=3),
            Leaderboard.objects.create(user=users[3], score=70, rank=4),
        ]

        for entry in leaderboard_entries:
            if entry.score > 75:
                self.stdout.write(f'Hello, {entry.user.name}! You are a top performer with a score of {entry.score}.')

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
