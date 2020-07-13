# import random
#
# # 输入函数
# num = input("请输入三个数：")
# # 检测输入是否是纯数字
# if num.isdigit() and if 100<= int(num) <=999:
#     pass
# else:
#     print("请按规则输入：")
#

class DictClass(object):
    def __init__(self, dict):
        self.dict = dict

    def del_dict(self, key):
        if key not in self.dict.keys():
            return "key不在字典里"
        else:
            self.dict.pop(key)
            return "删除成功"

    def get_dict(self, key):
        if key not in self.dict.keys():
            return "not found"
        else:
            return self.dict[key]

    def get_key(self):
        return self.dict.keys()


d = DictClass({'a': 1, 'b': 2, 'c': 3})
print(d.get_key())
