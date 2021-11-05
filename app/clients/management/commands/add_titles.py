from django.core.management.base import BaseCommand
from django.conf import settings

User = settings.AUTH_USER_MODEL

from ...models import Title


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument("file_name", type=str)

    def handle(self, *args, **kwargs):
        Title.objects.all().delete()
        file_name = kwargs["file_name"]
        with open(f"{file_name}") as file:
            for row in file:
                name = row.capitalize().replace("\n", "")
                self.stdout.write(self.style.SUCCESS(f"{name} added"))
                # updated_by = User.objects.get(pk=1)
                # created_by = User.objects.get(pk=1)
                Title.objects.get_or_create(title=name)
        self.stdout.write(self.style.SUCCESS("list of objects added"))
