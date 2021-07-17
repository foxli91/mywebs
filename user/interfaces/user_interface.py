from user.my_models.my_user import User
from mywebs.db_utils import get_cursor, close_conn


# 可以设置返回值类型
def find_user_by_name(name: str) -> [User]:
    sql = 'select * from users where user_name=%s'
    cu = get_cursor()
    res = cu.execute(query=sql, args=('张三',))

    user_list = []
    # 如果获取到值
    if res:
        # 拉取所有的值
        data = cu.fetchall()
        for i in data:
            user = User()
            for k, v in i.items():
                # 映射是否有这个属性
                if hasattr(user, k):
                    setattr(user, k, v)
            # 加入到用户列表中去
            user_list.append(user)
    close_conn()
    return user_list
