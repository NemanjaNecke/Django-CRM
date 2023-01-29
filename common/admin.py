from django.contrib import admin
from common.models import User, Address, Comment, Comment_Files, Org, Profile

# Register your models here.
admin.site.register(Org)
admin.site.register(Profile)
admin.site.register(User)
admin.site.register(Address)
admin.site.register(Comment)
admin.site.register(Comment_Files)
