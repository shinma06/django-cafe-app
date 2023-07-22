from django.core.management.base import BaseCommand
from django.core.management import call_command
from django.apps import apps


class Command(BaseCommand):
    help = 'Custom command to run makemigrations for all apps and then runserver'

    def handle(self, *args, **options):
        # Get all installed apps excluding default ones
        installed_apps = apps.get_app_configs()
        non_default_apps = [app for app in installed_apps if not app.name.startswith('django.contrib.')]

        # Run makemigrations for each app
        for app in non_default_apps:
            self.stdout.write(self.style.SUCCESS(f"Making migrations for {app.label}"))
            call_command('makemigrations', app.label, interactive=False)

        # Run migrate for all apps
        self.stdout.write(self.style.SUCCESS("Running migrate"))
        call_command('migrate')

        # Run runserver
        self.stdout.write(self.style.SUCCESS("Starting server"))
        call_command('runserver', '0.0.0.0:8000')
