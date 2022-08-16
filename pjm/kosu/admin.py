from django.contrib import admin

from kosu.models import (Man_Hours, Position_Master, Project_Master,
                         Project_Member, User_Master)

# Register your models here.
admin.site.register(Position_Master)
admin.site.register(User_Master)
admin.site.register(Project_Master)
admin.site.register(Project_Member)
admin.site.register(Man_Hours)
