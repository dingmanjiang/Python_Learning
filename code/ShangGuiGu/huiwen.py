# 练习 递归
# 创建一个函数，用来检查一个任意的字符串是否是回文字符串，如果是返回True，否则返回False
# 回文字符串，字符串从前往后念和从后往前念是一样的
# 例如：abcba
# lengh=5
# s[0] == s[-1]
# s[1] == s[-2]
# ...
# s[4] == s[-5]

def huiwen(s) :
    '''
    This is a function to check whether a string is a huiwen.
    :param s:
    :return: True or False
    '''
    if len(s) < 2 :
        return True
    elif s[0] != s[-1]:
        return False

    return huiwen(s[1:-1])

input_s = input('请输入一段字符串： ')
print(huiwen(input_s))