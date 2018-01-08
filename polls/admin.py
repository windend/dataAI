from django.contrib import admin
from .models import Question, Choice
# Register your models here.
from django.utils.translation import ugettext_lazy


class Myadminsite(admin.AdminSite):
    site_title = ugettext_lazy('Polls Administration')
    site_header = ugettext_lazy('Polls Administration')


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

# admin.site.register(Question, Quesetionadmin)
admin_site = Myadminsite()
# admin_site.register(Question, Quesetionadmin)
# admin.site.register(Choice)
