import random


def genwa(ans1, ans2):
    pass


def wr_1(ans1, ans2):
    i = random.randrange(1, 2)
    if i == 1:
        ans1 = -ans1
    elif i == 2:
        ans2 = -ans2
    return ans1, ans2


# requires validation of 2 same inverted numbers
def wa_2(ans1, ans2):
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


def wa_4(ans1, ans2):
    b = 0 - (ans1 + ans2)
    v = [True, False]
    cv = random.choice(v)
    if cv:
        return ans1, b/ans1
    else:
        return ans2, b/ans2


if __name__ == "__main__":
    print(wa_2(4, 5))
    print(wa_4(4, 5))
