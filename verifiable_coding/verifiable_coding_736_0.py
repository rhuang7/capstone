import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    T = int(data[0])
    results = []
    
    for i in range(1, T + 1):
        S = data[i].decode()
        min_abs = float('inf')
        
        # Find the minimum ASCII value in the string
        min_char = min(S)
        min_val = ord(min_char)
        
        # Find the maximum ASCII value in the string
        max_char = max(S)
        max_val = ord(max_char)
        
        # Calculate the minimum absolute value of points
        min_abs = min(max_val - min_val, min_val - max_val)
        
        results.append(str(min_abs))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()