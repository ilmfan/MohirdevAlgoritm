"""
author:
    Shodmonov Zafar
date and time:
    11:40  14.08.2021

problem:
    Bankga b so'm pul, so'mda omonotga qo'yildi. Har oyda mavjud pul p (0 < p <= 12) foizga oshadi. Necha(k) oydan
    keyin b so'm pul 2 martadan ko'p bo'lishini va necha(b_sum) so'm bo'lishini topish.

information about the algorithm:
    InPut:
        float: b
        float: p
    OutPut:
        int: k
        float: b_sum
    Algorithm:
        b so'm pul p foiz bilan necha(k) oyda o'z summasidan 2 marta ko'payishi
        va necha(b_sum) so'm bo'lishini topish.
        1-qo'shimcha shart: 0 < p <= 12

solution:

"""

def f8(b, p: float):
    if p > 0 and p <= 12:
        p_1 = p / 100
        k = 0
        b_sum = b
        while b_sum < 2*b:
            k += 1
            b_sum = b_sum * (1 + p_1)
    else:
        return "Foiz 13 foizgacha"
    return f"{k} oyda {b_sum} so'm"



