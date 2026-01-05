import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    T = int(data[0])
    cases = data[1:T+1]
    
    for s in cases:
        n = len(s)
        if n % 2 != 0:
            print(-1)
            continue
        
        zero_count = s.count('0')
        one_count = n - zero_count
        
        if zero_count % 2 != 0 or one_count % 2 != 0:
            print(-1)
            continue
        
        # We need to make sure that the string can be paired into (0,1) or (1,0)
        # So we need to have equal number of 0s and 1s
        # If they are not equal, we need to perform operations to make them equal
        # The minimal number of operations is the absolute difference between zero_count and one_count divided by 2
        # Because each operation can change one 0 to 1 or one 1 to 0
        diff = abs(zero_count - one_count)
        if diff % 2 != 0:
            print(-1)
            continue
        
        print(diff // 2)
        
if __name__ == '__main__':
    solve()