import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    N = int(data[0])
    shelf = list(map(int, data[1:]))

    # Find the longest increasing subsequence (LIS) that is already in order
    # The minimum number of moves is N - length of LIS
    # Because each element not in the LIS needs to be moved

    # Use a patience sorting-like algorithm to find the length of LIS
    lis = []
    for num in shelf:
        # Binary search for the first element >= num
        idx = 0
        while idx < len(lis) and lis[idx] < num:
            idx += 1
        if idx == len(lis):
            lis.append(num)
        else:
            lis[idx] = num
    print(N - len(lis))

if __name__ == '__main__':
    solve()