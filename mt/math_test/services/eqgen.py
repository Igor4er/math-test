import random
from math import sqrt


class SquareEq():
    def __init__(self) -> None:
        self.ans1 = None
        self.ans2 = None
        self.a = 1
        self.b = None
        self.c = None
        self.D = None

    def gs():
        return random.choice(list(range(-7, -1)) + list(range(1, 7)))

    def sgs():
        return random.choice(list(range(-5, -1)) + list(range(1, 5)))
    
    def gena(self):
        self.a = self.sgs()
    
    def genans(self):
        self.ans1 = self.gs()
        self.ans2 = self.gs()
    
    def viet(self):
        self.b = 0 - (self.ans1 + self.ans2)
        self.c = self.ans1 * self.ans2
    
    def calculate_D(self):
        self.D = self.b**2 - 4*self.a*self.c
        if self.D < 0:
            self.genans()
            return self.calculate_D
        return True
    
    def integer_D(self):
        if self.calculate_D():
            if not sqrt(self.D).is_integer():
                self.genans()
                return self.integer_D
    
    def retdict(self, type: int):
        return {
            "type": type,
            "a": self.a,
            "b": self.b,
            "c": self.c,
            "ans1": self.ans1,
            "ans2": self.ans2,
            "exists": self.exists
        }


def dl_1():
    se = SquareEq()


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
