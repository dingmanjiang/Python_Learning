# 练习递归
# 创建一个函数power来为任意数字做幂运算 n**i
# n**i = n*n**(i-1)
# n**(i-1)=n*n**(i-2)
# ...
# n**1 = n

def power(n,i):
    '''
    This is a function calculate the power of n with i
    '''
    result = n

    # if i is 1，it is the baseline.
    if i == 1 :
        return result

    result *= power(n, i-1)
    return result

print(power(19,3))