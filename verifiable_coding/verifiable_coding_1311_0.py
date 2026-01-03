import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    T = int(data[0])
    index = 1
    
    for _ in range(T):
        N = int(data[index])
        K = int(data[index+1])
        index += 2
        
        # We need exactly K positions where the prefix sum is positive
        # One way is to make the first K elements positive and the rest negative
        # This ensures that the prefix sum is positive for the first K elements
        result = []
        for i in range(1, N+1):
            if i <= K:
                result.append(i)
            else:
                result.append(-i)
        
        print(' '.join(map(str, result)))
        
if __name__ == '__main__':
    solve()