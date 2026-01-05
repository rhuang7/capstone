import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    N = int(data[0])
    permutation = list(map(int, data[1:]))

    # Find the longest increasing subsequence (LIS) that is already in order
    # The minimum number of moves is N - length of LIS
    # Because each element not in the LIS needs to be moved

    # Use a list to keep track of the smallest tail of all increasing subsequences
    # with length i+1
    tails = []

    for num in permutation:
        # Binary search for the first element in tails >= num
        # Using bisect_left
        idx = 0
        while idx < len(tails) and tails[idx] < num:
            idx += 1
        if idx == len(tails):
            tails.append(num)
        else:
            tails[idx] = num

    # The length of the LIS is the length of tails
    lis_length = len(tails)
    print(N - lis_length)

if __name__ == '__main__':
    solve()