from django.contrib import admin
from .models import Priority
# Register your models here.


@admin.register(Priority)
class PriorityAdmin(admin.ModelAdmin):
    list_display = ('level',)  
    search_fields = ('level',)  
    list_filter = ('level',)
