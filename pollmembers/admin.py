
from django.contrib import admin
from pollmembers.models import BookInstance
from pollmembers.models import Members, Cohort

admin.site.register(Members)
admin.site.register(Cohort)



# Register your models here.
#@admin.register(BookInstance)

class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'status', 'borrower', 'due_back', 'id')
    list_filter = ('status', 'due_back')

    fieldsets = (
        (None, {
            'fields': ('book','imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back','borrower')
        }),
    )


# Register your models here.
