import random

def rand_nonneg_ints_sum(total=25, n=12):
    m = total + n - 1
    bars = sorted(random.sample(range(m), n - 1))
    nums = []
    prev = -1
    for b in bars + [m]:
        nums.append(b - prev - 1)
        prev = b
    return nums

nums = rand_nonneg_ints_sum(5, 12)
print(nums)
print("sum =", sum(nums), "min =", min(nums))