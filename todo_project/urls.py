from django.contrib.auth import views as auth_views
from django.urls import path, include


urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('', include('todo_app.urls')),  # Ścieżki aplikacji todo
]
