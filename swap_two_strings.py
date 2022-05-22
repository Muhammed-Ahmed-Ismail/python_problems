from math import ceil


def swap_strings(str1, str2):
    f1, b1 = str1[0:ceil(len(str1) / 2)], str1[ceil(len(str1) / 2):]
    f2, b2 = str2[0:ceil(len(str2) / 2)], str2[ceil(len(str2) / 2) :]
    print(ceil(len(str2) / 2))

    return [f1 + f2, b1 + b2]


print(swap_strings('abcef', 'xzyy'))
