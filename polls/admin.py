from django.contrib import admin
from .models import Question, Choice
# Register your models here.


class Choiceinline(admin.TabularInline):
    model = Choice
    extra = 3


class Quesetionadmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': [
         'pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [Choiceinline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    search_fields = ['question_text']
    list_filter = ['pub_date', 'question_text']

admin.site.register(Question, Quesetionadmin)
# admin.site.register(Choice)
