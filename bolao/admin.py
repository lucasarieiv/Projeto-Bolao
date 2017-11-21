from django.contrib import admin
from .models import UserProfile, selecao, Partida, aposta

class selecaoAdmin(admin.ModelAdmin):
	list_display = ('nome', 'sigla')
	fields = ['nome', 'sigla']
	search_field = ['sigla', 'nome']

admin.site.register(UserProfile)
admin.site.register(aposta)
admin.site.register(selecao, selecaoAdmin)
admin.site.register(Partida)
