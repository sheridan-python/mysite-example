from django.contrib import admin
from . import models


class PostAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'author',
        'status',
        'created',
        'updated',
    )

    list_filter = (
        'status',
        'topics',
    )

    prepopulated_fields = {'slug': ('title',)}

    search_fields = (
        'title',
        'author__username',
        'author__first_name',
        'author__last_name',
    )


admin.site.register(models.Post, PostAdmin)


@admin.register(models.Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'slug',
    )
    prepopulated_fields = {'slug': ('name',)}



@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = (
        'email',
        'last_name',
        'first_name',
        'submitted'
    )

    readonly_fields = [
        'first_name',
        'last_name',
        'email',
        'message',
        'submitted'
    ]
