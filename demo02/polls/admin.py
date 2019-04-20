from django.contrib import admin
from .models import IssueList,ChioceList


# Register your models here.
class ChioceListInlines(admin.StackedInline):
    model = ChioceList
    extra = 2


class IssueListAdmin(admin.ModelAdmin):
    list_display = ['iss',]
    search_fields = ['issue']
    inlines = [ChioceListInlines]


class ChioceListAdmin(admin.ModelAdmin):
    list_display = ['isss', 'opt']
    list_filter = ['is_issue']
    search_fields = ['is_issue']
    list_per_page = 10


admin.site.register(IssueList, IssueListAdmin)
admin.site.register(ChioceList, ChioceListAdmin)
