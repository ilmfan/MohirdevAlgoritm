"""
author:  Shodmonov Zafar
date and time:  09:00  14.08.2021

information about the algorithm:
  InPut:  n
  OutPut:  prime numbers up to n
"""

def prime_numbers(n):
    output_list = [2]
    for num in range(3, n+1, 2):
        divided_into = []
        does_not_divide = []
        for i in range(2, num):
            if num % i == 0:
                divided_into.append(1)
            else:
                does_not_divide.append(1)
        if len(does_not_divide) == num - 2:
            output_list.append(num)
    return output_list
