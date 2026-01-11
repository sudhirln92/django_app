from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from utils import FileHandler



class Command(BaseCommand):
    help = "Create Super User"

    def handle(self, *args, **options):
        # super user
        self.create_super_user()
    
    def create_super_user(self):
        # FileHandler
        environ = FileHandler().read_json(
            file_name="environ.json", mode="r", add_path="config"
        )

        User = get_user_model()
        if User.objects.exists():
            self.stdout.write(self.style.ERROR("user already exists"))
            return

        User.objects.create_superuser(
            username=environ["username"],
            password=environ["password"],
            email=environ["email"],
        )
        msg = f'Local user "{environ["username"]}" was created'
        self.stdout.write(self.style.SUCCESS(msg))
