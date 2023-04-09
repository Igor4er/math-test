import random

def genwa(ans1, ans2):
    pass


# requires validation of 2 same inverted numbers
def wa_2(ans1, ans2):
    wa1 = 0 - ans1
    wa2 = 0 - ans2
    return wa1, wa2


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
