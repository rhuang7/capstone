import sys

def solve():
    import math
    input = sys.stdin.buffer.read
    data = input().split()
    
    T = int(data[0])
    index = 1
    
    results = []
    
    for _ in range(T):
        X = int(data[index])
        N = int(data[index + 1])
        index += 2
        
        # Find the number of working days
        count = N // X
        
        # Sum of arithmetic series: X + 2X + 3X + ... + count*X = X * (count * (count + 1)) // 2
        salary = X * (count * (count + 1)) // 2
        results.append(str(salary))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()