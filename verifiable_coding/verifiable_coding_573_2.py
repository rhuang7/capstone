import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    T = int(data[0])
    index = 1
    
    for _ in range(T):
        n = int(data[index])
        m = int(data[index+1])
        index += 2
        
        if n == 1:
            print(m)
            continue
        
        # The minimum time is determined by the maximum between:
        # 1. The time for the first person to learn all topics from the end (Malvika)
        # 2. The time for the last person to learn all topics from the start
        # Since each topic takes 1 hour to propagate in one direction
        # The maximum distance is (n-1) steps for each direction
        # But since each topic takes 1 hour, the total time is m * (n-1)
        # However, since the topics can be taught in parallel, the actual time is m * (n-1)
        # But we need to check the maximum between the two directions
        # The correct formula is m * (n - 1)
        print(m * (n - 1))

if __name__ == '__main__':
    solve()