import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    T = int(data[0])
    index = 1
    
    for _ in range(T):
        n = int(data[index])
        m = int(data[index + 1])
        index += 2
        
        # Malvika is at position n, and needs to teach m topics to the first n-1 people
        # Each topic takes 2 hours to propagate: one hour for teaching, one for learning
        # But since Malvika can teach multiple topics in parallel, the total time is 2 * m
        # However, if n == 1, then no one needs to learn, so time is 0
        if n == 1:
            print(0)
        else:
            print(2 * m)
            
if __name__ == '__main__':
    solve()