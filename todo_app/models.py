from django.db import models


class Priority(models.Model):
    LOW = 'Low'
    HIGH = 'High'
    PRIORITY_CHOICES = [
        (LOW, 'Priorytet niski'),
        (HIGH, 'Priorytet wysoki'),
    ]

    level = models.CharField(
        max_length=10, choices=PRIORITY_CHOICES, unique=True)

    def __str__(self):
        return dict(self.PRIORITY_CHOICES).get(self.level, self.level)


class Task(models.Model):
    title = models.CharField(max_length=255)
    priority = models.ForeignKey(
        Priority, on_delete=models.CASCADE)
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
