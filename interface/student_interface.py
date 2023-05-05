from db import modles

def student_register_interface(name,password):
    student_obj=modles.Student.get_obj_by_name(name)
    if student_obj:
        return False,'学生已经存在'
    else:
        modles.Student(name,password)
        return True,'注册成功'


def choose_school_interface(student_name,school_name):
    student_obj = modles.Student.get_obj_by_name(student_name)
    school = student_obj.get_school()
    if not school:

        student_obj.choose_school(school_name)

        return True,'选择学校成功'
    else:
        return False,'您已经选择学校了'


def get_can_choose_course_interface(student_name):
    obj = modles.Student.get_obj_by_name(student_name)
    if not obj.school:
        return False,'您没有选择学校，请先选择学校'
    school_obj=modles.School.get_obj_by_name(obj.school)
    if school_obj.course_list:
        return True,school_obj.course_list
    else:
        return False,'该学校下没有课程'


def choose_course_interface(student_name,course_name):

    obj = modles.Student.get_obj_by_name(student_name)
    if course_name in obj.course_list:
        return False,'您已经选了本门课程'
    obj.add_course(course_name)
    course_obj=modles.Course.get_obj_by_name(course_name)
    course_obj.add_student(student_name)
    return True,'选课成功'


def check_score_interface(student_name):
    obj = modles.Student.get_obj_by_name(student_name)
    return obj.scores




