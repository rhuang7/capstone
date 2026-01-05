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
        
        # The largest number <= c that leaves remainder b when divided by a
        # is c - ((c - b) % a)
        # If (c - b) % a == 0, then the number is c - (c - b) = b
        # Else, it's c - ((c - b) % a)
        result = c - ((c - b) % a)
        results.append(str(result))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()