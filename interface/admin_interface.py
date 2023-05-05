
from db import modles
def admin_register_interface(name,password):
    admin_obj=modles.Admin.get_obj_by_name(name)
    if admin_obj:
        return False,'管理员已经存在'
    else:
        modles.Admin(name,password)
        return True,'注册成功'

def create_school_interface(admin_name,school_name,addr):
    school_obj=modles.School.get_obj_by_name(school_name)
    if school_obj:
        return False,'学校已经存在'
    else:
        admin_obj=modles.Admin.get_obj_by_name(admin_name)
        admin_obj.create_school(school_name,addr)
        return True,'学校创建成功'

def create_teacher_interface(admin_name,name,password='456'):
    obj=modles.Teacher.get_obj_by_name(name)
    if obj:
        # haha
        return False,'老师已经存在'
    else:
        admin_obj=modles.Admin.get_obj_by_name(admin_name)
        admin_obj.create_teacher(name,password)
        return True,'老师创建成功'

def create_course_interface(admin_name,course_name,school_name):
    obj=modles.Course.get_obj_by_name(course_name)
    if obj:
        return False,'课程已经存在'
    else:
        admin_obj=modles.Admin.get_obj_by_name(admin_name)
        admin_obj.create_course(course_name)

        school_obj=modles.School.get_obj_by_name(school_name)
        school_obj.add_course(course_name)
        return True,'课程创建成功'



