from django.contrib import admin

# Register your models here.
from .models import Comment, Essay

class CommentInline(admin.TabularInline):
    model = Comment
    extra = 3


class EssayAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['essay_title']}),
        ('Essay Text',               {'fields': ['essay_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [CommentInline]
    list_display = ('essay_title', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']

admin.site.register(Essay, EssayAdmin)