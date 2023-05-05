
from core import admin,student,teacher

func_dic={
    '1':admin.admin_view,
    '2':student.student_view,
    '3':teacher.teacher_view
}
def run():
    while True:
        print('''
        1 管理员视图
        2 学生视图
        3 老师视图
        ''')
        choice =input('请选择:').strip()
        if  choice not in func_dic:continue
        func_dic[choice]()

