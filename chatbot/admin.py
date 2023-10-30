from django.contrib import admin
from .models import Chat, Feedbacks

class ListingMessages(admin.ModelAdmin):
    list_display = ("id","message","response","created_at","user_id")
    list_display_links = ("id","message","response","created_at","user_id")
    search_fields = ("id","message","response","created_at","user_id")
    list_filter = ("id","message","response","created_at","user_id")
    list_per_page = 30

class ListingFeedbacks(admin.ModelAdmin):
    list_display = ("id","chat_id","message","response","created_at","message_group","approved","user_id")
    list_display_links = ("id","chat_id","message","response","created_at","message_group","approved","user_id")
    search_fields = ("id","chat_id","message","response","created_at","message_group","approved","user_id")
    list_filter = ("id","chat_id","message","response","created_at","message_group","approved","user_id")
    list_per_page = 30

# Register your models here.

admin.site.register(Chat, ListingMessages)

admin.site.register(Feedbacks, ListingFeedbacks)