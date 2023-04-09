import random

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


if __name__ == "__main__":
    eq = dl_1()
    print(f"{eq['a'] if eq['a'] != 1 else ''}x^2 {'+' if eq['b'] > 0 else '-'} {abs(eq['b'])} {'+' if eq['c'] > 0 else '-'} {abs(eq['c'])}")
