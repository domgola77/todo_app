# Todo App w Django

Aplikacja do zarządzania zadaniami stworzona w Django.

## Zrzuty ekranu

### Strona logowania (http://127.0.0.1:8000/login/)
![Strona logowania](images/login_page.png)

### Strona dodania zadania (http://127.0.0.1:8000/create/)
![Strona dodania zadania](images/add_task_page.png)

### Strona listy zadan (http://127.0.0.1:8000/)
![Strona listy zadan](images/add_task_page.png)

## Instalacja

1. Sklonuj repozytorium:
   ```bash
   git clone https://github.com/domgola77/todo_app.git
   cd todo_app

2. Stwórz wirtualne środowisko i zainstaluj zależności:

    python -m venv venv
    source venv/bin/activate  # Linux/macOS
    venv\Scripts\activate     # Windows
    pip install -r requirements.txt

3. Wykonaj migracje bazy danych:

    python manage.py migrate

4. Utwórz użytkownika administracyjnego: Uruchom skrypt initialize_users.py, aby utworzyć użytkownika admin z hasłem admin123: 

    python manage.py shell < initialize_users.py

5. Uruchamianie serwera: 

    python manage.py runserver

Aplikacja będzie dostępna pod adresem: http://127.0.0.1:8000/.
