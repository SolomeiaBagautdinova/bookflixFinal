from django.contrib import admin
from .submodels import *

admin.site.register(Author)
admin.site.register(Gender)
admin.site.register(Editorial)

admin.site.register(Account)
admin.site.register(CreditCards)
admin.site.register(Profile)

admin.site.register(MailToConfirm)
admin.site.register(UserSolicitud)

admin.site.register(StateOfBook)

admin.site.register(Publication)
admin.site.register(Book)
admin.site.register(BookByChapter)
admin.site.register(Chapter)
admin.site.register(Billboard)

admin.site.register(Comment)
admin.site.register(Like)
admin.site.register(LikeComment)

admin.site.register(CounterStates)

admin.site.register(UpDates)
admin.site.register(ExpirationDates)