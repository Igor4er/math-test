import random
from math import sqrt


def gs():
    return random.choice(list(range(-7, -1)) + list(range(1, 7)))


def sgs():
    return random.choice(list(range(-5, -1)) + list(range(1, 5)))

def dl_1():
    ans1 = gs()
    ans2 = gs()

    b = 0 - (ans1 + ans2)
    c = ans1 * ans2

    return {
        "type": 1,
        "a": 1,
        "b": b,
        "c": c,
        "ans1": ans1,
        "ans2": ans2
    }


def dl_2():
    ans1 = gs()
    ans2 = gs()

    b = 0 - (ans1 + ans2)
    c = ans1 * ans2

    a = sgs()
    b = b * a
    c = c * a

    return {
        "type": 1,
        "a": a,
        "b": b,
        "c": c,
        "ans1": ans1,
        "ans2": ans2
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
    eq = dl_2()
    print(f"{eq['a'] if eq['a'] != 1 else ''}x^2 {'+' if eq['b'] > 0 else '-'} {abs(eq['b']) if eq['b'] != 0 else ''}x {'+' if eq['c'] > 0 else '-'} {abs(eq['c'])} =0")
    print(f"ans1: {eq['ans1']}\nans2: {eq['ans2']}")
