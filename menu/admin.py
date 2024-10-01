from django.contrib import admin
from .models import Beverages, Food

@admin.register(Beverages)
class BeveragesAdmin(SummernoteModelAdmin):

    list_display = ('title', 'type', 'cost', 'calories')
    search_fields = ['title', 'type',]
    list_filter = ('title', 'type',)

@admin.register(Food)
class FoodAdmin(SummernoteModelAdmin):

    list_display = ('title', 'type', 'cost', 'calories')
    search_fields = ['title', 'type',]
    list_filter = ('title', 'type',)

@admin.register(Beverages)
class BeveragesAdmin(SummernoteModelAdmin):
    list_display = ('title', 'type', 'cost', 'calories')
    search_fields = ['title', 'type',]
    list_filter = ('title', 'type',)

@admin.register(Food)
class FoodAdmin(SummernoteModelAdmin):
    list_display = ('title', 'type', 'cost', 'calories')
    search_fields = ['title', 'type',]
    list_filter = ('title', 'type',)

# Register your models here.
