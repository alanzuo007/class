from django.db import models
# Create your models here.
class ClassInfo(models.Model):
    class_code = models.CharField('班级编码', max_length=20)
    area = models.CharField('校区', max_length=20 )
    grade = models.CharField('年级', max_length=20 )
    course = models.CharField('科目', max_length=20 )
    class_type = models.CharField('班型', max_length=20 )
    teacher = models.CharField('老师', max_length=20)
    period = models.CharField('区间', max_length=20 )
    time = models.CharField('时段',max_length=20)

    def __str__(self):
        return f'{self.class_code}-{self.teacher}-{self.area}-{self.course}'

class ClassChange(models.Model):
    class_code_c = models.CharField('班级编码', max_length=20)
    #class_code_c_YN = models.CharField('班级编码YN', max_length=1)
    teacher_c = models.CharField('老师', max_length=20)
    teacher_c_YN = models.CharField('老师YN', max_length=1)
    area_c = models.CharField('校区', max_length=20)
    area_c_YN = models.CharField('校区YN', max_length=1)
    grade_c = models.CharField('年级', max_length=20)
    grade_c_YN = models.CharField('年级YN', max_length=1)
    course_c = models.CharField('科目', max_length=20)
    course_c_YN = models.CharField('科目YN', max_length=1)
    class_type_c = models.CharField('班型', max_length=20)
    class_type_c_YN = models.CharField('班型YN', max_length=1)
    period_c = models.CharField('区间', max_length=20)
    period_c_YN = models.CharField('区间YN', max_length=1)
    time_c = models.CharField('时段',max_length=20)
    time_c_YN = models.CharField('时段YN',max_length=1)
    class_change_YN=models.CharField("是否有变更",max_length=1)
    posted=models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering=['-posted']
    def __str__(self):
        return f'{self.class_code_c}-{self.teacher_c}-{self.area_c}-{self.course_c}'

class ExportFields(models.Model):
    export_fields=models.CharField('导出字段',max_length=20)
    def __str__(self):
        return self.export_fields


class MailUser(models.Model):
    email=models.EmailField('用户邮箱',max_length=30)
    password=models.CharField('密码',max_length=20)
    def __str__(self):
        return f'{self.email}-{self.password}'