#!/bin/phthon3

import re

# 中国手机号(还没配置好）
re_ChinesePhoneNumber = r'(0086|\+86)?\s?(1[3456789]\d\s?\d{4}\s?\d{4})(\D)'

# url_protocol
# 判断http://、https://、ftp://
re_UrlProtocol = r'''(https?|ftp):\/\/'''



text = '131 5261 4238'
pattern = re.compile(re_ChinesePhoneNumber)
print(pattern.findall(text))

