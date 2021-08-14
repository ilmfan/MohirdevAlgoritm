from sonni_tup_kupaytuvchilarga_ajratish import stka
def f10(a, b):
    list_a = stka(a)
    list_b = stka(b)
    ia = 0
    ib = 0
    list3 = []
    for i in list_a[::2]:
        e1 = i
        for j in list_b[::2]:
            e2 = j
            if e2 == e1:
                f = min(list_a[(ia + 1)], list_b[(ib + 1)])
                list3.append(e1)
                list3.append(f)
                ib = 0
                break
            elif e1 < e2:
                ib = 0
                break
            else:
                ib += 2
        ia += 2
    a3 = 1
    ki = 0
    for k in list3[::2]:
        a1 = k ** list3[(ki + 1)]
        ki += 2
        a3 *= a1
    return a3
