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
            
            # Find the minimum operations to make left and right equal
            # We can only reduce characters, so we need to find the common character
            # that is less than or equal to both left and right
            # The best common character is the minimum of left and right
            # So we reduce the higher character to match the lower one
            if left < right:
                operations += (right - left)
            else:
                operations += (left - right)
        
        results.append(str(operations))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()