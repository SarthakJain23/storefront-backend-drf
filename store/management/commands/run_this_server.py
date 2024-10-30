from django.core.management.base import BaseCommand
import subprocess


class Command(BaseCommand):
    help = "Populates the database with collections and products"

    commands = [
        [
            "cd ~",
            "conda activate storefront",
            "cd Desktop/Personal/Project/storefront",
            "python manage.py runserver",
        ],
        [
            "cd ~",
            "conda activate storefront",
            "cd Desktop/Personal/Project/storefront",
            "docker run --rm -it -p 5000:80 -p 2525:25 rnwood/smtp4dev",
        ],
        [
            "cd ~",
            "conda activate storefront",
            "cd Desktop/Personal/Project/storefront",
            "docker run -d -p 6379:6379 redis",
        ],
        [
            "cd ~",
            "conda activate storefront",
            "cd Desktop/Personal/Project/storefront",
            "celery -A storefront worker --loglevel=info",
        ],
        [
            "cd ~",
            "conda activate storefront",
            "cd Desktop/Personal/Project/storefront",
            "celery -A storefront beat",
        ],
        [
            "cd ~",
            "conda activate storefront",
            "cd Desktop/Personal/Project/storefront",
            "celery -A storefront flower",
        ],
        [
            "cd ~",
            "conda activate storefront",
            "cd Desktop/Personal/Project/storefront",
            "locust -f locustfiles/browse_products.py",
        ],
    ]

    def run_command_in_new_tab(self, commands):
        # Join the commands into a single string separated by &&
        command_str = " && ".join(commands)
        # Open a new terminal tab and run the commands
        subprocess.run(
            [
                "osascript",
                "-e",
                f'tell application "Terminal" to do script "{command_str}"',
            ]
        )

    def handle(self, *args, **options):
        print("Setting up the app...")
        for command_set in self.commands:
            self.run_command_in_new_tab(command_set)
