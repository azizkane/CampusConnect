from django.contrib import admin
from .models import *


admin.site.register(Library)
admin.site.register(Category)
admin.site.register(Document)

admin.site.register(Forum)
admin.site.register(Topic)
admin.site.register(Post)

admin.site.register(CalendarSettings)
admin.site.register(SharedCalendar)
admin.site.register(Project)
admin.site.register(Task)
admin.site.register(Event)

# EVENT