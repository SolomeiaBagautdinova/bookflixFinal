from django.contrib import admin
from .submodels import *

admin.site.register(Author)
admin.site.register(Gender)
admin.site.register(Editorial)
admin.site.register(Account)
admin.site.register(CreditCards)
admin.site.register(Book)

admin.site.register(Profile)

admin.site.register(Billboard)

admin.site.register(UserSolicitud)

admin.site.register(StateOfBook)