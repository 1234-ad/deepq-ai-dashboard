from django.core.management.base import BaseCommand
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = 'Set up demo user and data for DeepQ-AI dashboard'

    def handle(self, *args, **options):
        # Create demo superuser
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser(
                username='admin',
                email='admin@deepq-ai.com',
                password='admin123'
            )
            self.stdout.write(
                self.style.SUCCESS('Demo superuser created: admin/admin123')
            )
        else:
            self.stdout.write(
                self.style.WARNING('Demo superuser already exists')
            )

        # Create demo regular user
        if not User.objects.filter(username='demo').exists():
            User.objects.create_user(
                username='demo',
                email='demo@deepq-ai.com',
                password='demo123'
            )
            self.stdout.write(
                self.style.SUCCESS('Demo user created: demo/demo123')
            )
        else:
            self.stdout.write(
                self.style.WARNING('Demo user already exists')
            )

        self.stdout.write(
            self.style.SUCCESS('Demo setup completed successfully!')
        )