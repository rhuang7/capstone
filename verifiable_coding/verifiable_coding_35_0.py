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
        e = list(map(int, data[idx:idx+N]))
        idx += N
        
        e.sort()
        groups = 0
        current_group_size = 0
        
        for e_i in e:
            if current_group_size < e_i:
                current_group_size = e_i
                groups += 1
            else:
                current_group_size += 1
        
        results.append(str(groups))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()