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
        
        # Construct the sequence
        result = []
        count = 0
        for i in range(1, N+1):
            if count < K:
                result.append(i)
                count += 1
            else:
                result.append(-i)
        
        print(' '.join(map(str, result)))
        
if __name__ == '__main__':
    solve()