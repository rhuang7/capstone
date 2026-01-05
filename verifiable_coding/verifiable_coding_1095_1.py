import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    N = int(data[0])
    perm = list(map(int, data[1:]))
    
    # Find the longest increasing subsequence (LIS) that is already in order
    # The minimum number of moves is N - length of LIS
    # Because each element not in the LIS needs to be moved
    
    # Use a list to track the smallest possible tail of all increasing subsequences
    # with length i+1
    lis = []
    
    for num in perm:
        # Binary search for the first element in lis >= num
        # Using bisect_left
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