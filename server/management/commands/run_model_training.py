from django.core.management.base import BaseCommand
from server.learning.learn import run_training


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write('Starting training ...')
        run_training()
        self.stdout.write("*** DONE! ***")
