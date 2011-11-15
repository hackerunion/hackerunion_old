from django.contrib import admin
from people.models import *


class HackerProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'preferred_contact_email', 'twitter_username',
                    'facebook_username', 'tumblr_username', 'availability']
    list_filter = ['availability']


admin.site.register(HackerProfile, HackerProfileAdmin)