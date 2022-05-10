from django.contrib import admin
from app_v1.models import Score

# Register your models here.

@admin.register(Score)
class ScoreAdmin(admin.ModelAdmin):
    list_display = ('name', 'score', 'date_created')
    ordering = ('-score',)
    search_fields = ('name',)
    
