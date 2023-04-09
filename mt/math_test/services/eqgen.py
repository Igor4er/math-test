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
        self.gf = self.gs()
        self.sgf = self.sgs()

    def gs(self):
        return random.choice(list(range(-7, -1)) + list(range(1, 7)))

    def sgs(self):
        return random.choice(list(range(-5, -1)) + list(range(1, 5)))
    
    def pgs(self):
        return float(self.gs() + self.rsp())
    
    def psgs(self):
        return float(self.sgs() + self.rsp())
    
    def rsp(self):
        return random.choice([0.5, 0.75, 0.25, 0.05, 0.15])
    
    def gena(self):
        self.a = self.sgf()
    
    def genans(self):
        self.ans1 = gf()
        self.ans2 = gf()
    
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
    return se.retdict(type=3)


def dl_5():
    se = SquareEq()
    se.genans(gf=se.pgs)
    se.gena(gf=se.psgs)
    se.viet()
    se.integer_D()
    return se.retdict(5)
    

if __name__ == "__main__":
    se = dl_5()
    print(f"{se['a'] if se['a'] != 1 else ''}x^2 {'+' if se['b'] > 0 else '-'} {abs(se['b']) if se['b'] != 0 else ''}x {'+' if se['c'] > 0 else '-'} {abs(se['c'])} =0")
    print(f"ans1: {se['ans1']}\nans2: {se['ans2']}")
