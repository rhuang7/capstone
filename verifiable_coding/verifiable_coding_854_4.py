import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    idx = 0
    T = int(data[idx])
    idx += 1
    results = []
    
    for _ in range(T):
        N = int(data[idx])
        idx += 1
        A = list(map(int, data[idx:idx+N]))
        idx += N
        
        seen = set()
        is_beautiful = True
        for num in A:
            if num in seen:
                is_beautiful = False
                break
            seen.add(num)
        
        if is_beautiful:
            results.append("prekrasnyy")
        else:
            results.append("ne krasivo")
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()