from django.contrib import admin
from .models import ClassChange,ClassInfo,ExportFields,MailUser

class ClassInfoAdmin(admin.ModelAdmin):
    '''
        班级信息管理
    '''

    list_display = ('class_code','area','grade','course','class_type','teacher','period','time')
    search_fields = ('class_code','teacher')
#注册班级信息管理
admin.site.register(ClassInfo,ClassInfoAdmin)

class ClassChangeAdmin(admin.ModelAdmin):
    '''
        班级信息变更管理
    '''
    list_display = ('class_change_YN','class_code_c','area_c','area_c_YN','grade_c','grade_c_YN',
                    'course_c','course_c_YN','class_type_c','class_type_c_YN','teacher_c','teacher_c_YN',
                    'period_c','period_c_YN','time_c','time_c_YN')
    search_fields = ('class_code','teacher')
    ordering = ('-posted',)
admin.site.register(ClassChange,ClassChangeAdmin)
class MailUserAdmin(admin.ModelAdmin):
    '''
        用户管理
    '''
    list_display = ('email','password')
    search_fields = ('email','password')
admin.site.register(MailUser,MailUserAdmin)