import csv

from django.core.management.base import BaseCommand

from django.conf import settings
from ...models import User


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument("file_name", type=str)

    def handle(self, *args, **kwargs):
        file_name = kwargs["file_name"]
        with open(f"{file_name}", "r") as file:
            reader = csv.reader(file)
            for i, row in enumerate(reader):
                if i == 0:
                    pass
                else:
                    first = row[0].replace(" ", "").lower()
                    last = row[2].replace(" ", "").lower()
                    username = f"{first}{last}"
                    User.objects.get_or_create(
                        username=username,
                        email="",
                        password="Password2021",
                    )
                    self.stdout.write(self.style.SUCCESS(f"{username} added"))
