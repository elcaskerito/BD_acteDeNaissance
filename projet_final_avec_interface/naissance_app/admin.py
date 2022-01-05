from django.contrib import admin
from .models import  Utilisateur, nouveau_ne


#admin.site.register(Utilisateur)

#admin.site.register(nouveau_ne)

@admin.register(nouveau_ne)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('nom', 'nom_pere', 'nom_mere', )
    ordering = ('nom', )
    search_fields =  ('nom', )


@admin.register(Utilisateur)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('nom', 'role', 'mail', )
    ordering = ('nom', )
    search_fields =  ('nom', )