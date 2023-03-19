from django.contrib import admin

from ads.models import Advertisement, Comment


# ----------------------------------------------------------------
# admin register
admin.site.register(Advertisement)
admin.site.register(Comment)
