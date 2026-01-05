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
        B = list(map(int, data[idx:idx+N]))
        idx += N
        
        a_pos = 0
        b_pos = 0
        weird_distance = 0
        
        for i in range(N):
            a_speed = A[i]
            b_speed = B[i]
            
            if a_speed == b_speed:
                weird_distance += a_speed
                a_pos += a_speed
                b_pos += b_speed
            else:
                a_pos += a_speed
                b_pos += b_speed
        
        results.append(str(weird_distance))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()