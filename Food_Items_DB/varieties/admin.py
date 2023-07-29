from django.contrib import admin
from varieties.models import Category,food

class foodAdmin(admin.ModelAdmin):
    list_display=['id','Item_Name','Item_Cost','Item_Published','Manufactured_Date']
    list_display_links=['id','Item_Name']
    list_filter=['Item_Cost','Manufactured_Date']
    list_editable=['Item_Published']
    search_fields=['Item_Name','Item_Cost']
    ordering=['Item_Cost']
admin.site.register(food,foodAdmin)
admin.site.register(Category)

# Register your models here.
