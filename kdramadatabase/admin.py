from django.contrib import admin

# Register your models here.
from .models import KDrama, BroadcastChannel

admin.site.register(KDrama)
admin.site.register(BroadcastChannel)
