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
        segments = []
        for _ in range(N):
            L = int(data[idx])
            R = int(data[idx+1])
            segments.append((L, R))
            idx += 2
        
        if N == 1:
            results.append("0")
            results.append("")
            continue
        
        current_L, current_R = segments[0]
        total_ops = 0
        operations = []
        
        for i in range(1, N):
            next_L, next_R = segments[i]
            
            # Move L to next_L
            diff_L = next_L - current_L
            for _ in range(abs(diff_L)):
                if diff_L > 0:
                    operations.append("L+")
                    current_L += 1
                else:
                    operations.append("L-")
                    current_L -= 1
            total_ops += abs(diff_L)
            
            # Move R to next_R
            diff_R = next_R - current_R
            for _ in range(abs(diff_R)):
                if diff_R > 0:
                    operations.append("R+")
                    current_R += 1
                else:
                    operations.append("R-")
                    current_R -= 1
            total_ops += abs(diff_R)
        
        results.append(str(total_ops))
        results.append("".join(operations))
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()