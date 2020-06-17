from django.contrib import admin
from dogfeed.models import Pet, Amount
# Register your models here.

class AmountInline(admin.TabularInline):
    model = Amount
@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display=('name',)
    inlines = [AmountInline]