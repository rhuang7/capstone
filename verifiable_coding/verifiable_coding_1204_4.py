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
        
        # We need to find the minimum cost to turn S into R
        # The cost is k * l, where k is the number of operations and l is the total number of replaced characters
        # To minimize the cost, we need to minimize k * l
        # We can do this by making as few operations as possible, but each operation should cover as many characters as possible
        
        # We'll track the number of operations and the total number of replaced characters
        k = 0
        l = 0
        i = 0
        while i < N:
            if S[i] != R[i]:
                # Start a new operation
                k += 1
                # Find the end of this operation
                j = i
                while j < N and S[j] != R[j]:
                    j += 1
                # Replace from i to j-1
                l += (j - i)
                i = j
            else:
                i += 1
        
        print(k * l)

if __name__ == '__main__':
    solve()