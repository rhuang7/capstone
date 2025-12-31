import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    T = int(data[0])
    index = 1
    
    for _ in range(T):
        S = data[index]
        R = data[index + 1]
        index += 2
        
        N = len(S)
        if S == R:
            print(0)
            continue
        
        # Find the positions where S[i] != R[i]
        diff = [i for i in range(N) if S[i] != R[i]]
        if not diff:
            print(0)
            continue
        
        # The minimum cost is achieved by making as few operations as possible
        # Each operation can cover a contiguous block of differing positions
        # So we need to find the minimum number of operations needed to cover all differing positions
        # and then compute the cost as (number of operations) * (total number of characters replaced)
        
        # We can use a greedy approach: cover as many differing positions as possible in each operation
        # Start from the first differing position and cover as far as possible
        cost = 0
        i = 0
        while i < len(diff):
            # Start of the current operation
            start = diff[i]
            # End of the current operation
            end = diff[i]
            while end + 1 < len(diff) and diff[end + 1] == diff[end] + 1:
                end += 1
            # Number of operations is (end - start + 1)
            # Total characters replaced is (end - start + 1)
            # Cost is (number of operations) * (total characters replaced)
            cost += (end - start + 1) * (end - start + 1)
            i = end + 1
        
        print(cost)

if __name__ == '__main__':
    solve()