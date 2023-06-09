import random
from math import sqrt
from decimal import Decimal


class SquareEq():
    def __init__(self) -> None:
        self.ans1 = None
        self.ans2 = None
        self.a = 1
        self.b = None
        self.c = None
        self.D = None
        self.gf = self.gs
        self.sgf = self.sgs

    def gs(self):
        return random.choice(list(range(-7, -1)) + list(range(1, 7)))

    def sgs(self):
        return random.choice(list(range(-5, -1)) + list(range(1, 5)))
    
    def pgs(self):
        return Decimal(self.gs()) + self.rsp()
    
    def psgs(self):
        return Decimal(self.sgs()) + self.rsp()
    
    def rsp(self):
        return random.choice([Decimal(0.50), Decimal(0.75), Decimal(0.25), Decimal(0.5)])
    
    def gena(self):
        self.a = self.sgf()
    
    def genans(self):
        self.ans1 = self.gf()
        self.ans2 = self.gf()
    
    def viet(self):
        self.b = 0 - (self.ans1 + self.ans2)
        self.c = self.ans1 * self.ans2
    
    def calculate_D(self):
        self.D = self.b**2 - 4*self.a*self.c
        if self.D < 0:
            self.genans()
            self.viet()
            self.gena()
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
        }


def dl_1():
    se = SquareEq()

    se.genans()
    se.viet()

    return se.retdict(1)


def dl_2():
    se = SquareEq()

    se.genans()
    se.viet()

    se.gena()

    se.b = se.b * se.a
    se.c = se.c * se.a

    return se.retdict(2)


def dl_3():
    se = SquareEq()
    se.genans()
    se.gena()
    se.viet()
    se.integer_D()
    return se.retdict(3)


def dl_4():
    se = SquareEq()

    se.gf = se.pgs
    se.genans()
    se.viet()

    return se.retdict(4)


def dl_5():
    se = SquareEq()

    se.gf = se.pgs
    se.genans()

    se.sgf = se.psgs
    se.gena()
    se.viet()
    se.integer_D()
    return se.retdict(5)
    

def generate_eq():
    v = [1, 2, 4]
    vv = random.choice(v)
    if vv == 1:
        return dl_1()
    elif vv == 2:
        return dl_2()
    elif vv == 4:
        return dl_4()


if __name__ == "__main__":
    se = dl_1()
    print(f"{se['a'] if se['a'] != 1 else ''}x^2 {'+' if se['b'] > 0 else '-'} {abs(se['b']) if se['b'] != 0 else ''}x {'+' if se['c'] > 0 else '-'} {abs(se['c'])} =0")
    print(f"ans1: {se['ans1']}\nans2: {se['ans2']}")
