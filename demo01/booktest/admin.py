from django.contrib import admin
from .models import BookInfo,HeroInfo


# Register your models here.
class HeroInfoInline(admin.StackedInline):
    model = HeroInfo
    extra = 1


class BookInfoAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_filter = ['btitle']
    search_fields = ['btitle']
    list_per_page = 5
    inlines = [HeroInfoInline]


class HeroInfoAdmin(admin.ModelAdmin):
    list_display = ['name', 'book']
    list_filter = ['hgender', 'hbook']
    search_fields = ['hname', 'hgender', 'hbook']
    list_per_page = 10


admin.site.register(BookInfo, BookInfoAdmin)
admin.site.register(HeroInfo, HeroInfoAdmin)
