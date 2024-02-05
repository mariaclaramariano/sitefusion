from django.contrib import admin
from .models import Cargo, servico, Equipe, features
# Register your models here.
@admin.register(Cargo)
class CargoAdmin(admin.ModelAdmin):
    list_display= ('cargo', 'ativo', 'modificado')

@admin.register(Servico)
class ServicoAdmin(admin.ModelAdmin):
    list_display=('servico','icone', 'ativo', 'modificado')

@admin.register(Equipe)
class funcionaroAdmin(admin.ModelAdmin):
    list_display=('nome', 'cargo', 'ativo', 'modificado')

@admin.register(features)
class featuresAdmin(admin.ModelAdmin):
    list_display=('nome','icone', 'ativo','modificado','bio')
