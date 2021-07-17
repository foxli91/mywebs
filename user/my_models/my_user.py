from django.db import models


# class Users(models.Model):
#     # 这里设置类型[charfiled 表示是char类型]，长度，说明
#     pk_id = models.CharField(primary_key=True,max_length=32, verbose_name="主键")
#
#     user_name = models.CharField(max_length=64, verbose_name="用户名称")
#
#     # int 整形的数据只需要说明就可以了
#     house_number = models.IntegerField(verbose_name="拥有的房子")
class User():
    # 这里设置类型[charfiled 表示是char类型]，长度，说明
    pk_id = ''

    user_name = ''

    # int 整形的数据只需要说明就可以了
    house_number = 0

    def __str__(self) -> str:
        return f'pk_id={self.pk_id},user_name={self.user_name},house_number={self.house_number}'

    # def __init__(self, pk_id, user_name, house_number) -> None:
    #     super().__init__()
    #     self.pk_id = pk_id
    #     self.user_name = user_name
    #     self.house_number = house_number
