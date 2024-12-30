from django.contrib.auth.models import User


def run():
    # Tworzenie użytkownika admin
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser(
            username='admin',
            password='admin123'
        )
        print("Utworzono użytkownika admin (hasło: admin123)")
