import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    idx = 1
    results = []
    for _ in range(T):
        M = int(data[idx])
        N = int(data[idx+1])
        idx += 2
        
        count_pairs = 0
        count_x = 0
        seen_x = set()
        
        for x in range(1, M+1):
            for y in range(1, N+1):
                lhs = x * y + x + y
                s = str(x) + str(y)
                if str(lhs) == s:
                    count_pairs += 1
                    seen_x.add(x)
        count_x = len(seen_x)
        results.append(f"{count_pairs} {count_x}")
    
    print("\n".join(results))

if __name__ == '__main__':
    solve()