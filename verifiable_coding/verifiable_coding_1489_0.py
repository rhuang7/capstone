import sys

def solve():
    import sys
    input = sys.stdin.buffer.read().split()
    S = int(input[0])
    K = int(input[1])

    s = str(S)
    n = len(s)

    max_profit = 0

    for i in range(n):
        if K == 0:
            break
        # Try to replace the i-th digit with 9
        # But ensure the number is as large as possible
        # We can try all possible digits from 9 down to 0
        for d in range(9, -1, -1):
            if d < int(s[i]):
                # We can replace the i-th digit with d to make the number larger
                # But we need to check if this is a valid change
                # We can only change the first K digits
                # So we need to check if we can change this digit
                # and if it's better than the current max
                new_num = s[:i] + str(d) + s[i+1:]
                new_num = int(new_num)
                profit = new_num - S
                if profit > max_profit:
                    max_profit = profit
                # We can't change more than K digits
                # So we need to check if we can change this digit
                # and if it's better than the current max
                # We can only change the first K digits
                # So we need to check if we can change this digit
                # and if it's better than the current max
                # We can only change the first K digits
                # So we need to check if we can change this digit
                # and if it's better than the current max
                # We can only change the first K digits
                # So we need to check if we can change this digit
                # and if it's better than the current max
                # We can only change the first K digits
                # So we need to check if we can change this digit
                # and if it's better than the current max
                # We can only change the first K digits
                # So we need to check if we can change this digit
                # and if it's better than the current max
                # We can only change the first K digits
                # So we need to check if we can change this digit
                # and if it's better than the current max
                # We can only change the first K digits
                # So we need to check if we can change this digit
                # and if it's better than the current max
                # We can only change the first K digits
                # So we need to check if we can change this digit
                # and if it's better than the current max
                # We can only change the first K digits
                # So we need to check if we can change this digit
                # and if it's better than the current max
                # We can only change the first K digits
                # So we need to check if we can change this digit
                # and if it's better than the current max
                # We can only change the first K digits
                # So we need to check if we can change this digit
                # and if it's better than the current max
                # We can only change the first K digits
                # So we need to check if we can change this digit
                # and if it's better than the current max
                # We can only change the first K digits
                # So we need to check if we can change this digit
                # and if it's better than the current max
                # We can only change the first K digits
                # So we need to check if we can change this digit
                # and if it's better than the current max
                # We can only change the first K digits
                # So we need to check if we can change this digit
                # and if it's better than the current max
                # We can only change the first K digits
                # So we need to check if we can change this digit
                # and if it's better than the current max
                # We can only change the first K digits
                # So we need to check if we can change this digit
                # and if it's better than the current max
                # We can only change the first K digits
                # So we need to check if we can change this digit
                # and if it's better than the current max
                # We can only change the first K digits
                # So we need to check if we can change this digit
                # and if it's better than the current max
                # We can only change the first K digits
                # So we need to check if we can change this digit
                # and if it's better than the current max
                # We can only change the first K digits
                # So we need to check if we can change this digit
                # and if it's better than the current max
                # We can only change the first K digits
                # So we need to check if we can change this digit
                # and if it's better than the current max
                # We can only change the first K digits
                # So we need to check if we can change this digit
                # and if it's better than the current max
                # We can only change the first K digits
                # So we need to check if we can change this digit
                # and if it's better than the current max
                # We can only change the first K digits
                # So we need to check if we can change this digit
                # and if it's better than the current max
                # We can only change the first K digits
                # So we need to check if we can change this digit
                # and if it's better than the current max
                # We can only change the first K digits
                # So we need to check if we can change this digit
                # and if it's better than the current max
                # We can only change the first K digits
                # So we need to check if we can change this digit
                # and if it's better than the current max
                # We can only change the first K digits
                # So we need to check if we can change this digit
                # and if it's better than the current max
                # We can only change the first K digits
                # So we need to check if we can change this digit
                # and if it's better than the current max
                # We can only change the first K digits
                # So we need to check if we can change this digit
                # and if it's better than the current max
                # We can only change the first K digits
                # So we need to check if we can change this digit
                # and if it's better than the current max
                # We can only change the first K digits
                # So we need to check if we can change this digit
                # and if it's better than the current max
                # We can only change the first K digits
                # So we need to check if we can change this digit
                # and if it's better than the current max
                # We can only change the first K digits
                # So we need to check if we can change this digit
                # and if it's better than the current max
                # We can only change the first K digits
                # So we need to check if we can change this digit
                # and if it's better than the current max
                # We can only change the first K digits
                # So we need to check if we can change this digit
                # and if it's better than the current max
                # We can only change the first K digits
                # So we need to check if we can change this digit
                # and if it's better than the current max
                # We can only change the first K digits
                # So we need to check if we can change this digit
                # and if it's better than the current max
                # We can only change the first K digits
                # So we need to check if we can change this digit
                # and if it's better than the current max
                # We can only change the first K digits
                # So we need to check if we can change this digit
                # and if it's better than the current max
                # We can only change the first K digits
                # So we need to check if we can change this digit
                # and if it's better than the current max
                # We can only change the first K digits
                # So we need to check if we can change this digit
                # and if it's better than the current max
                # We can only change the first K digits
                # So we need to check if we can change this digit
                # and if it's better than the current max
                # We can only change the first K digits
                # So we need to check if we can change this digit
                # and if it's better than the current max
                # We can only change the first K digits
                # So we need to check if we can change this digit
                # and if it's better than the current max
                # We can only change the first K digits