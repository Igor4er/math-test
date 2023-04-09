import random
from decimal import Decimal


def genwa(ans1, ans2):
    v = [1, 2, 3, 4]
    was = []
    while len(was) < 3:
        cv = random.choice(v)
        
        if cv == 1:
            was.append(wr_1(ans1, ans2))
        elif cv == 2:
            if ans1 != -ans2:
                was.append(wr_2(ans1, ans2))
        elif cv == 3:
            was.append(wr_3(ans1, ans2))
        else:
            was.append(wr_4(ans1, ans2))
    return was


def wr_1(ans1, ans2):
    i = random.randrange(1, 2)
    if i == 1:
        ans1 = -ans1
    elif i == 2:
        ans2 = -ans2
    return ans1, ans2


# requires validation of 2 same inverted numbers
def wr_2(ans1, ans2):
    wa1 = 0 - ans1
    wa2 = 0 - ans2
    return wa1, wa2


def wr_3(ans1, ans2):
    i = random.randrange(1, 2)
    diff = random.randrange(-5, 5)
    if i == 1:
        ans1 = ans1 + diff
        ans2 = ans2 - diff
    elif i == 2:
        ans1 = ans1 - diff
        ans2 = ans2 + diff
    return ans1, ans2


def wr_4(ans1, ans2):
    b = 0 - (ans1 + ans2)
    v = [True, False]
    cv = random.choice(v)
    if cv:
        return ans1, Decimal(b)/Decimal(ans1)
    else:
        return ans2, Decimal(b)/Decimal(ans2)


if __name__ == "__main__":
    print(wa_2(4, 5))
    print(wa_4(4, 5))
