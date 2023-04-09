import random
from math import sqrt


def gs():
    return random.choice(list(range(-7, -1)) + list(range(1, 7)))


def dl_1():
    b = gs()
    c = gs()

    v1 = b + c
    v2 = b * c

    return {
        "type": 1,
        "a": 1,
        "b": b,
        "c": c
    }


def dl_3():
    v1 = gs()
    v2 = gs()
    a = gs()

    b = -(v1+v2)
    c = v1*v2

    D = b**2 - 4*a*c

    if D >= 0:
        if not sqrt(D).is_integer():
            return dl_3()
        else:
            return {
                "type": 3,
                "a": a,
                "b": b,
                "c": c
            }
    else:
        return dl_3()


if __name__ == "__main__":
    eq = dl_3()
    print(f"{eq['a'] if eq['a'] != 1 else ''}x^2 {'+' if eq['b'] > 0 else '-'} {abs(eq['b'])} {'+' if eq['c'] > 0 else '-'} {abs(eq['c'])} = 0")
