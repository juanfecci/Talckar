from django.core.management.base import BaseCommand, CommandError

from django.conf import settings

from importlib import import_module

class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def handle(self, *args, **options):
        for cron_view in settings.CRON_APPS:
            module = import_module(cron_view)
            func = getattr(module,'CRON')
            func()
