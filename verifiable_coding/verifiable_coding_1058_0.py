import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    t = int(data[0])
    results = []
    
    for i in range(1, t + 1):
        n = data[i]
        original = ""
        for ch in n:
            digit = int(ch) - 2
            original += str(digit)
        results.append(original)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()