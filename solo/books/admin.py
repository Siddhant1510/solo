from django.contrib import admin

from .models import book_info ,issued , book_request

admin.site.register(book_info)
admin.site.register(issued)
admin.site.register(book_request)
