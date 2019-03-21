from django.db import connections
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand

# import time


class Command(BaseCommand):
    """Django command to pause execution until db is available"""

    def handle(self, *args, **options):
        self.stdout.write("Waiting for db...")
        db_conn = None
        while not db_conn:
            try:
                db_conn = connections["default"]
            except OperationalError:
                self.stdout.write("Db unavailable at the moment, waiting 1 second...")

        self.stdout.write(self.style.SUCCESS("Db available!"))
