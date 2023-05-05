from  db import modles
import os
from conf import settings
from lib import common
def login_interface(name,password,user_type):
    if user_type =='admin':
        obj= modles.Admin.get_obj_by_name(name)
    elif  user_type =='teacher':
        obj= modles.Teacher.get_obj_by_name(name)
    elif user_type =='student':
        obj = modles.Student.get_obj_by_name(name)
    else:
        return False,'没有这个用户类型'
    if obj:
        if obj.password ==password:
            return True,'%s:%s 登陆成功'%(user_type,name)
        else:
            return False,'密码错误'
    else:
        return  False,'用户不存在'



def check_all_schools():

    path= os.path.join(settings.BASE_DB,'school')
    return common.get_all_dir_obj(path)



