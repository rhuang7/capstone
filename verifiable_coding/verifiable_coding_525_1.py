import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    T = int(data[0])
    index = 1
    
    results = []
    
    for _ in range(T):
        a = int(data[index])
        b = int(data[index+1])
        c = int(data[index+2])
        index += 3
        
        # The largest number <= c that leaves remainder b when divided by a is:
        # If b <= c, then it's c - ((c - b) % a)
        # Otherwise, it's c - ((c - b) % a) if (c - b) % a is not zero, else c - a
        # But since b < a and a < c, we can directly compute:
        remainder = (c - b) % a
        result = c - remainder
        results.append(str(result))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()