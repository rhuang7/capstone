import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    T = int(data[0])
    index = 1
    
    for _ in range(T):
        S = data[index]
        R = data[index+1]
        index += 2
        
        N = len(S)
        if S == R:
            print(0)
            continue
        
        # Find the positions where S and R differ
        diff = []
        for i in range(N):
            if S[i] != R[i]:
                diff.append(i)
        
        # If there are no differences, output 0
        if not diff:
            print(0)
            continue
        
        # The minimum cost is achieved by making as few operations as possible
        # Each operation can cover a contiguous block of differing positions
        # So we need to find the number of operations required to cover all differing positions
        # This is equivalent to the number of "blocks" of differing positions
        
        # Initialize the number of operations
        k = 1
        # Start from the first differing position
        start = diff[0]
        # Iterate through the differing positions
        for i in range(1, len(diff)):
            if diff[i] != diff[i-1] + 1:
                k += 1
        
        # The length of the operation is the number of differing positions
        l = len(diff)
        # The cost is k * l
        print(k * l)

if __name__ == '__main__':
    solve()