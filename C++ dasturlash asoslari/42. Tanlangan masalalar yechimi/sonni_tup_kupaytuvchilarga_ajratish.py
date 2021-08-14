from f6 import prime_numbers

def stka(n):  # stka - [sonni tub ko'paytuvchilarga ajratish]
    output_list = []
    output_prime_numbers = prime_numbers(n)
    for i in output_prime_numbers:
        daraja = []
        if n % i == 0:
            while n % i == 0:
                daraja.append(1)
                n = n / i
            output_list.append(i)
            output_list.append(len(daraja))
    return output_list