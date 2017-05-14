from django.contrib import admin
from .models import Course

# Register your models here.
#admin.site.register(Producto)
@admin.register(Course)
class AdminProduct(admin.ModelAdmin):
    list_display = ('id', 'name', 'start_date', 'end_date', 'picture')
    list_filter = ('start_date',)