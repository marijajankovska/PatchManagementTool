from django.contrib import admin
from .models import System, Application_Admin, Patching


class Patching_Admin(admin.ModelAdmin):

    exclude = ['patch_plan_feb', 'patch_exec_feb',
               'patch_plan_mar', 'patch_exec_mar', 'patch_plan_apr', 'patch_exec_apr',
               'patch_plan_may', 'patch_exec_may', 'patch_plan_jun', 'patch_exec_jun',
               'patch_plan_jul', 'patch_exec_jul', 'patch_plan_aug', 'patch_exec_aug',
               'patch_plan_sep', 'patch_exec_sep', 'patch_plan_oct', 'patch_exec_oct',
               'patch_plan_nov', 'patch_exec_nov', 'patch_plan_dec', 'patch_exec_dec']

    readonly_fields = ['patch_plan_feb', 'patch_exec_feb',
                       'patch_plan_mar', 'patch_exec_mar', 'patch_plan_apr', 'patch_exec_apr',
                       'patch_plan_may', 'patch_exec_may', 'patch_plan_jun', 'patch_exec_jun',
                       'patch_plan_jul', 'patch_exec_jul', 'patch_plan_aug', 'patch_exec_aug',
                       'patch_plan_sep', 'patch_exec_sep', 'patch_plan_oct', 'patch_exec_oct',
                       'patch_plan_nov', 'patch_exec_nov', 'patch_plan_dec', 'patch_exec_dec']



admin.site.register(Patching, Patching_Admin)
admin.site.register(System)
admin.site.register(Application_Admin)
