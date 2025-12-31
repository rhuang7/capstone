import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    T = int(data[0])
    index = 1
    
    results = []
    
    for _ in range(T):
        B = int(data[index])
        G = int(data[index + 1])
        index += 2
        
        # Each boy gives a rose to a girl and vice versa
        # But if a person has already received a rose, they can't exchange again
        # So the total number of roses is 2 * min(B, G)
        results.append(str(2 * min(B, G)))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()