# シンプソンの公式.

def simpson_rule(LIMIT: int, MAX: int, DIVIDE: int) -> float:
    ans = 0
    h = float((MAX - LIMIT) / DIVIDE)
    H = float(((MAX - LIMIT) / DIVIDE) / 2)

    for i in range(DIVIDE):
        top = i * h
        mid = ((i + 1) * h + i * h) / 2
        bot = (i + 1) * h

        s = func(top) + 4 * func(mid) + func(bot)
        ans += s
    return ans * H/3


def func(x: float) -> float:
    fx = x**3
    return fx
