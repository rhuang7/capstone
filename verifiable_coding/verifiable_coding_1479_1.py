import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    idx = 0
    T = int(data[idx])
    idx += 1
    
    score = [0] * 12  # index 0 unused, 1-11 are problems
    
    for _ in range(T):
        N = int(data[idx])
        idx += 1
        for _ in range(N):
            p = int(data[idx])
            s = int(data[idx + 1])
            idx += 2
            if 1 <= p <= 8:
                if s > score[p]:
                    score[p] = s
        total = sum(score[1:9])
        print(total)
        
if __name__ == '__main__':
    solve()