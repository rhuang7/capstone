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
        # 1. The time for the first person to learn all m topics from the end (Malvika)
        # 2. The time for the last person to learn all m topics from the end (Malvika)
        # Since each topic takes 1 hour to propagate one step, the time for a person at distance d is d * m
        # The maximum distance is (n-1) steps from Malvika to the first person
        time1 = (n - 1) * m
        time2 = (n - 1) * m
        
        print(max(time1, time2))

if __name__ == '__main__':
    solve()