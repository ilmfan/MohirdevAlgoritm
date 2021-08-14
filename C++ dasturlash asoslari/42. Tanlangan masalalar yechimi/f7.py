from sonni_tup_kupaytuvchilarga_ajratish import stka

def a2(d):
    sum11 = 1
    for i1 in range(0, len(d), 2):
        h = i1 + 1
        sum11 *= (d[i1]**((d[h]) + 1) - 1) / (d[i1] - 1)
    return sum11


def f7(n):
    list1 = range(3, (n + 1))
    list2 = range(3, (n + 1))
    output_list1 = []
    for i in range(len(list1)):
        q = list1[i]
        index_q = i
        e1 = stka(i)
        y1 = a2(e1)

        for j in range(len(list2)):
            w = list2[j]
            index_w = j
            e2 = stka(j)
            y2 = a2(e2)

            if y1 == y2:
                output_list1.append(q)
                output_list1.append(w)

    return output_list1





