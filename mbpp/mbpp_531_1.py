def check(candidate):
    assert candidate([9, 6, 5, 1] ,4,11)==2
    assert candidate([4,5,6,7,8,9],6,9)==1
    assert candidate([1, 2, 3],3,4)==2


def min_coins(value, coins):
    coins.sort(reverse=True)
    count = 0
    for coin in coins:
        if value >= coin:
            count += value // coin
            value %= coin
    return count if value == 0 else -1

check(min_coins)