from django.contrib import admin
from .models import Smrp, Ris
# Register your models here.
@admin.register(Smrp)
class SmrpAdmin(admin.ModelAdmin):
    model = Smrp
    list_display=['name','modaliti']
    list_filter=['modaliti']
    


modaliti_choices = (
    ('CT','CT-Scan'),
    ('MR','MRI'),
    ('XR','General X-Ray'),
    ('MG','Mammography'),
    ('US','Ultrasound'),
    ('FL','Fluoroscopy'),
    ('XA','Angiography'),
    ('MF','Mobile Fluoro/OT/ERCP'),
    ('HC','Hardcopy'),
    ('DI','Digitize'),
    ('RE','Rad Resources'),
    ('RC','Ref Consult'),
)



@admin.register(Ris)
class RisAdmin(admin.ModelAdmin):
    model = Ris
    list_display = ['code','name','modaliti']
    list_filter = ['modaliti']
    actions = ['CT','MR','MG','FL','XR','HC','DI','USG','XA','MF','RE','RC']
    search_fields = ['code','name']

    @admin.action(description='Modaliti CT-Scan')
    def CT(self, request, queryset):
        queryset.update(modaliti='CT')

    @admin.action(description='Modaliti MRI')
    def MR(self, request, queryset):
        queryset.update(modaliti='MR')

    @admin.action(description='Modaliti Mammo')
    def MG(self, request, queryset):
        queryset.update(modaliti='MG')

    @admin.action(description='Modaliti Fluoro')
    def FL(self, request, queryset):
        queryset.update(modaliti='FL')

    @admin.action(description='Modaliti General X-Ray')
    def XR(self, request, queryset):
        queryset.update(modaliti='XR')

    @admin.action(description='Modaliti Hardcopy')
    def HC(self, request, queryset):
        queryset.update(modaliti='HC')

    @admin.action(description='Modaliti Digitize')
    def DI(self, request, queryset):
        queryset.update(modaliti='DI')

    @admin.action(description='Modaliti USG')
    def US(self, request, queryset):
        queryset.update(modaliti='US')

    @admin.action(description='Modaliti Angio')
    def XA(self, request, queryset):
        queryset.update(modaliti='XA')

    @admin.action(description='Mobile Fluoro/OT')
    def MF(self, request, queryset):
        queryset.update(modaliti='MF')


    @admin.action(description='Modaliti Rad Resource')
    def RE(self, request, queryset):
        queryset.update(modaliti='RE')

    @admin.action(description='Mobile Reporting')
    def RC(self, request, queryset):
        queryset.update(modaliti='RC')