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
        
        # Each boy gives a rose to a girl and each girl gives a rose to a boy
        # But the exchange is only possible if at least one hasn't received a rose
        # So the total number of roses is B + G
        results.append(str(B + G))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()