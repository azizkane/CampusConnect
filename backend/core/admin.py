from django.contrib import admin
from .models import *

admin.site.register(accounts.User)
admin.site.register(accounts.UserProfile)
admin.site.register(Student)
admin.site.register(Team)

admin.site.register(School)
admin.site.register(Department)
admin.site.register(Manager)

admin.site.register(Plan)
admin.site.register(Subscription)
