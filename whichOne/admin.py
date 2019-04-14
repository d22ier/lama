from django.contrib import admin
from .models import Question

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
            ('Question', {'fields': ['question','alpagaIMG','lamaIMG']}),
            ]

admin.site.register(Question, QuestionAdmin)

# Register your models here.
