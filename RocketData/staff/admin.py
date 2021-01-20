from django.contrib import admin
from django_admin_relation_links import AdminChangeLinksMixin
from mptt.admin import MPTTModelAdmin

from .models import Staffmodels
import decimal
from django.db.models import F



@admin.register(Staffmodels)
class CategoryAdmin(AdminChangeLinksMixin, MPTTModelAdmin):
    list_display = ['parent', 'name', 'position', 'date_employment',
                    'salary', 'salary_all', 'slug']
    prepopulated_fields = {'slug': ('name',)}
    list_filter = ['salary', 'position']
    change_links = ['parent']
    actions = ['clear_salary_all']


    def clear_salary_all(self, request, queryset):
        queryset.update(salary_all=F('salary_all') * decimal.Decimal('0'))
    clear_salary_all.short_description = 'Clear salary all'


