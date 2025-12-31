import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    T = int(data[0])
    results = []
    
    for i in range(1, T + 1):
        S = data[i]
        n = len(S)
        operations = 0
        
        for j in range(n // 2):
            left = S[j]
            right = S[n - 1 - j]
            
            if left != right:
                # Find the minimum steps to make left and right equal
                # We need to reduce the higher character to the lower one
                if ord(left) > ord(right):
                    # Reduce left to right
                    operations += ord(left) - ord(right)
                else:
                    # Reduce right to left
                    operations += ord(right) - ord(left)
        
        results.append(str(operations))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()