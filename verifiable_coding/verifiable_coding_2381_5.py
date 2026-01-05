import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    t = int(data[0])
    results = []
    
    index = 1
    for _ in range(t):
        s = data[index]
        index += 1
        n = len(s)
        max_d = 0
        current_pos = 0
        
        for i in range(n):
            if s[i] == 'R':
                if current_pos == 0:
                    max_d = max(max_d, i + 1)
                else:
                    max_d = max(max_d, i - current_pos + 1)
                current_pos = i
            else:
                if current_pos == 0:
                    max_d = max(max_d, i + 1)
                else:
                    max_d = max(max_d, current_pos - i + 1)
                current_pos = i
        
        if current_pos == 0:
            max_d = max(max_d, n + 1)
        else:
            max_d = max(max_d, n + 1 - current_pos)
        
        results.append(str(max_d))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()