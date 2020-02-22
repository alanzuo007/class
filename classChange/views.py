from django.shortcuts import render
from django.http import HttpResponse,request
from .models import ClassInfo,ClassChange,ExportFields
from django.contrib import messages
import xlrd
import pandas as pd

global choices_period
global choices_time
choices_period = ['', '第一期', '第二期', '第三期', '第三期', '星期五', '星期六', '星期日']
h = ['8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22']
m = ['00', '10', '20', '30', '40', '50']
choices_time = [':'.join([i, ii]) for i in h for ii in m]
choices_time.insert(0,'')
def login(request):
    return render(request,'login.html')

def handle_login(request):
    mail_user= request.POST.get('email','')
    password=request.POST.get('password','')
    print(mail_user,password)
    return HttpResponse("HANDLE LOGIN")
def load(request):
    # wb = xlrd.open_workbook(r'C:\Users\alanz\Desktop\班级信息变更项目\暑假设班清单汇总20200107.xlsx')
    # table = wb.sheet_by_name('总表')
    # cols = table.row_values(0)
    # nrows = table.nrows  # 行数
    # s_fields = ['class_code', 'teacher', 'area', 'grade', 'course','class_type','period','time']
    # sqllist=[]
    # print(cols)
    # for i in range(1, nrows):
    #     row_value = table.row_values(i)  # 一行的数据
    #     col_value = []
    #     for ii in range(len(cols)):
    #         col_value.append(row_value[ii])
    #     sql=ClassInfo(class_code=row_value[11],
    #             teacher=row_value[8],
    #             area=row_value[1],
    #             grade=row_value[2],
    #             course=row_value[4],
    #             class_type = row_value[5],
    #             period = row_value[6],
    #             time = row_value[7])
    #     sqllist.append(sql)
    # ClassInfo.objects.bulk_create(sqllist)
    #
    # fields=pd.read_excel(r'C:\Users\alanz\Desktop\班级信息变更项目\修改班模板.xlsx',sheet_name='Details').columns.to_list()
    # print(fields)
    # for i in fields:
    #     ExportFields(export_fields=i).save()


    global class_code
    class_code=request.POST.get('class_code','')
    if class_code:
        #target=ClassInfo.objects.get(class_code=class_code)
        target = ClassInfo.objects.filter(class_code=class_code)
        #fields=ClassInfo._meta.fields
        return render(request, 'index.html', context={'show': "",'class_code':class_code,'item':target[0],
                                                      'choices_period':choices_period,'choices_time':choices_time})
    else:
        return render(request, 'index.html', context={'show': "None",'class_code':class_code})

def submit(request):
    print('this is a submit')
    area=request.POST.get('area_l','')
    grade=request.POST.get('grade_l','')
    course=request.POST.get('course_l','')
    class_type=request.POST.get('classtype_l','')
    teacher=request.POST.get('teacher_l','')
    period=request.POST.get('period_l','')
    time = request.POST.get('time_l', '')
    print([class_code,area,grade,course,class_type,teacher,period,time])

    area_c=request.POST.get('area_r','')
    grade_c=request.POST.get('grade_r','')
    course_c=request.POST.get('course_r','')
    class_type_c=request.POST.get('classtype_r','')
    teacher_c=request.POST.get('teacher_r','')
    period_c=request.POST.get('period_r','')
    time_c ='-'.join([ request.POST.get('time_r', ''),request.POST.get('time_r2', '')])
    print(time_c)
    print([class_code, area_c, grade_c, course_c, class_type_c, teacher_c, period_c, time_c])
    any_change=''.join([area_c, grade_c, course_c, class_type_c, teacher_c, period_c, time_c])
    if any_change=='-':
        print("没有变更信息")
        messages.success(request, "系统提示：未检测到查到任何变更信息")
        return render(request, 'index.html', context={'show': "", 'class_code': class_code})
    else:
        area_submit=[area_c,'Y'] if area!=area_c and area_c!='' else [area,'N']
        grade_submit = [grade_c,'Y'] if grade!=grade_c and grade_c!='' else [grade,'N']
        course_submit = [course_c,'Y'] if course!=course_c and course_c!='' else [course,'N']
        class_type_submit=[class_type_c,'Y'] if class_type!=class_type_c and class_type_c!='' else [class_type,'N']
        teacher_submit=[teacher_c,'Y'] if teacher!=teacher_c and teacher_c!='' else [teacher,'N']
        period_submit=[period_c,'Y'] if period!=period_c and period_c!='' else [period,'N']
        time_submit=[time_c,'Y'] if time!=time_c and time_c!='' else [time,'N']
        ClassChange(class_code_c=class_code,
                  area_c=area_submit[0],
                  grade_c=grade_submit[0],
                  course_c=course_submit[0],
                  class_type_c = class_type_submit[0],
                  teacher_c=teacher_submit[0],
                  period_c = period_submit[0],
                  time_c = time_submit[0],
                  area_c_YN=area_submit[1],
                  grade_c_YN=grade_submit[1],
                  course_c_YN=course_submit[1],
                  class_type_c_YN=class_type_submit[1],
                  teacher_c_YN=teacher_submit[1],
                  period_c_YN=period_submit[1],
                  time_c_YN=time_submit[1],
                  class_change_YN='Y'
                    ).save()
        messages.success(request,"信息已经变更到数据库")
        return render(request, 'index.html', context={'show': "None",'class_code':''})
def query(request):
    global class_code
    class_code=request.POST.get('class_code','')
    target=ClassChange.objects.filter(class_code_c=class_code)
    if target:
        target_origin=ClassInfo.objects.filter(class_code=class_code)
        # print(target)
        # print(target_origin)
        return render(request, 'query.html', context={'show': "None",'items':target[0],'color':'indianred','items_origin':target_origin[0]})
    else:
        messages.success(request,'系统提示，该班号没有变更记录')
        return load(request)
def export(request):
    target=ClassChange.objects.filter(class_code_c=class_code)[0]
    # global class_code
    # class_code=class_code
    print(target)
    e_fields=ExportFields.objects.all()
    e_fields=[i.export_fields for i in e_fields]
    mapping={}
    if target.period_c_YN == 'Y':
        mapping['上课时间']=target.period_c
    if target.time_c_YN=='Y':
        mapping['上课时间(外)']=target.time_c
    mapping['*班级编码']=class_code
    detail = pd.Series(e_fields).map(mapping)
    pd.DataFrame({'字段':e_fields,'变更':detail}).T.to_excel(f'C:\\Users\\alanz\\Desktop\班级信息变更项目\\{class_code}.xlsx',index=False,header=False)
    messages.success(request, "Downloaded Successfully")
    target = ClassInfo.objects.filter(class_code=class_code)
    return render(request, 'index.html', context={'show': "", 'class_code': class_code, 'item': target[0],
                                                  'choices_period': choices_period, 'choices_time': choices_time})