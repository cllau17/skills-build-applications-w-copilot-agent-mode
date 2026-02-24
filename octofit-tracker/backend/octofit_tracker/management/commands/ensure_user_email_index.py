from django.core.management.base import BaseCommand
from djongo import connection

class Command(BaseCommand):
    help = 'Ensure unique index on email field in users collection.'

    def handle(self, *args, **kwargs):
        db = connection.cursor().db_conn
        result = db['octofit_tracker_user'].create_index(
            [('email', 1)], unique=True
        )
        self.stdout.write(self.style.SUCCESS(f'Unique index created on email: {result}'))
