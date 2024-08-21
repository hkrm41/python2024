import random
def rolling_dice(pip,repeat):
    for r in range(repeat):
        n = random.randint(1,pip)
        print(r, n)

rolling_dice(6,5)

