import re

# -----------------------------------------------------------------------------
# 								常用的正则表达式
#                           creat by Ding Manjiang
# -----------------------------------------------------------------------------
# 使用方法：
# 1、所有变量都以re作为前缀，每个子类下以下划线分割

# -------------------------------------------
# 子类：电话号码(rege_phone)
# -------------------------------------------

# 中国手机号
rege_phone_ChineseMobile = r'''(?x)						#多行注释模式
							(?<!\d)						#号码之前数字开头
							(?:(?:0086|\+86)[-\s]?)?	#有或没有国际区号和间隔
							1[3456789]\d				#手机号前三位
							[-\s]?						#手机号之间的间隔
							\d{4}						#手机号中间四位
							[-\s]?						#手机号之间的间隔
							\d{4}						#手机号后四位
							(?!\d)						#号码之后不能是数字
							'''

# -------------------------------------------
# 子类：网络地址(rege_net)
# -------------------------------------------

# url_protocol
rege_net_UrlProtocol = r'(https?|ftp):\/\/'
# 判断http://、https://、ftp://


print(re.findall('\\\\', 'a*b+c?\\d123d\\'))


# text = '+86-131-5261-4238 13152613238 132998398234'
# match = re.search(rege_phone_ChineseMobile,text)
# if match:
#     print(match.group(0))

# matchfindall = re.findall(rege_phone_ChineseMobile,text)
# if match:
#     print(matchfindall)

# for m in re.finditer(rege_phone_ChineseMobile, text):
#     if m:
#         print(m.group(0))
