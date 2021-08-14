"""
author:
    Shodmonov Zafar
date and time:
    00:12  15.08.2021

problem:
    Matn berilgan. Matndagi eng qisqa so'z va uning necha simvoldan iboratligini topuvchi algoritm tuzish.

information about the algorithm:
    InPut:
        str: s
    OutPut:
        str: words[mi]
        int: c1
    Algorithm:
        Algorithm funksiya ko'rinishida quyida berilgan.
solution:

"""

def reverse(s):
    length = len(s)
    spaces = [' ']
    words = []
    b = []
    i = 0
    while i < length:
        if s[i] not in spaces:
            word_start = i
            while i < length and s[i] not in spaces:
                i += 1
            b.append((i - word_start))
            words.append(s[word_start:i])
        i += 1
    c1 = min(b)
    ik = 0
    for k in b:
        if c1 == k:
            mi = ik
        ik += 1
    return f"{words[mi]} so'zi va {c1} harfdan iborat"