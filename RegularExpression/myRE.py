#!/bin/phthon3

import re

# 中国手机号(还没把前后文的隔离考虑进去）
re_ChinesePhoneNumber = r'(0086|\+86)?[-\s]?1[3456789]\d[-\s]?\d{4}[-\s]?\d{4}'

# url_protocol
# 判断http://、https://、ftp://
re_UrlProtocol = r'(https?|ftp):\/\/'



text = '+86-131-5261-4238 13152613238'
#pattern = re.compile(re_ChinesePhoneNumber)
#print(pattern.search(text))
#print(pattern.match(text))
#print(pattern.findall(text))
match = re.search(re_ChinesePhoneNumber,text)
if match:
    print(match.group(0))

matchfindall = re.findall(re_ChinesePhoneNumber,text)
if match:
    print(matchfindall)

for m in re.finditer(re_ChinesePhoneNumber, text):
    if m:
        print(m.group(0))

ls = re.findall(r'(0086|\+86)?[-\s]?1[3456789]\d[-\s]?\d{4}[-\s]?\d{4}','13152613328  +8613813831381')
print(ls)
