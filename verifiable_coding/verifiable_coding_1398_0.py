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
        results.append(len(unique_chars))
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()