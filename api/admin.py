from django.contrib import admin
from .models import Meal , Rating

# Register your models here.
class RatingAdmin(admin.ModelAdmin):
    list_display= ['id','meal','user', 'stars']
    list_filter= ['user','meal']
    
class MealAdmin(admin.ModelAdmin):
    list_display= ['id','title','description']
    search_fields=['title','description']
    list_filter=['title','description']
    
admin.site.register(Meal, MealAdmin)
admin.site.register(Rating, RatingAdmin)