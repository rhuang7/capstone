import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    T = int(data[0])
    results = []
    
    for i in range(1, T + 1):
        s = data[i]
        unique_chars = set(s)
        results.append(str(len(unique_chars)))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()