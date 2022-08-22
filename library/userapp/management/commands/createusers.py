from django.core.management.base import BaseCommand
from userapp.models import User


class Command(BaseCommand):
    help = 'Create Superuser and some test users'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int)

        def handle(self, *args, **options):
            # удаляем всех пользователей
            User.objects.all().delete()
            user_count = options['count']
            # создаем суперпользователя
            User.objects.create_superuser('leo', 'leo@test', 'dante123456')
            #создаем тестовых пользователей
            for i in range(user_count):
                User.objects.create_user(f'user{i}, fuser{i}@test.com', 'dante123456')

            print('done')