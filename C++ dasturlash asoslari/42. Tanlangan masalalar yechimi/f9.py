"""
author:
    Shodmonov Zafar
date and time:
    16:44  14.08.2021

problem:
    n butun son (n > 0) berilgan. Shu sonning raqamlar soni(m)ni va raqamlar yig'indisi(p)ni topish algoritmini tuzing.

information about the algorithm:
    InPut:
        int: n
    OutPut:
        int: m
        int: p
    Algorithm:
        Algorithm funksiya ko'rinishida quyida berilgan.
solution:

"""
def f9(n):
    s = str(n)
    m = len(s)
    p = 0
    for i in s:
        f = int(i)
        p += f
    return m, p
