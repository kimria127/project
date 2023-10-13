from django.contrib import admin
from .models import MainContent, Necklace, Earring, Let, Comment, Comment2, Comment3

class CommentAdmin(admin.ModelAdmin):
    list_display = ['content_list', 'content', 'author', 'create_date', 'modify_date']
    search_fields = ['author']

class Comment2Admin(admin.ModelAdmin):
    list_display = ['content_list', 'content', 'author', 'create_date', 'modify_date']
    search_fields = ['author']
class Comment3Admin(admin.ModelAdmin):
    list_display = ['content_list', 'content', 'author', 'create_date', 'modify_date']
    search_fields = ['author']

class NecklaceAdmin(admin.ModelAdmin):
 list_display = [ 'name', 'image']
 search_fields = ['name']

class EarringAdmin(admin.ModelAdmin):
 list_display = [ 'name', 'image']
 search_fields = ['name']

class LetAdmin(admin.ModelAdmin):
  list_display = [ 'name', 'image']
  search_fields = ['name']


admin.site.register(MainContent)
admin.site.register(Let, LetAdmin)
admin.site.register(Necklace, NecklaceAdmin)
admin.site.register(Earring, EarringAdmin)

admin.site.register(Comment, CommentAdmin)
admin.site.register(Comment2, Comment2Admin)
admin.site.register(Comment3, Comment3Admin)