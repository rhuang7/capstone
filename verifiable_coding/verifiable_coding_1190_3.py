import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    T = int(data[0])
    p_list = list(map(int, data[1:T+1]))
    
    for p in p_list:
        count = 0
        while p > 0:
            # Find the highest power of 2 less than or equal to p
            highest = 1
            while highest * 2 <= p:
                highest *= 2
            count += 1
            p -= highest
        print(count)

if __name__ == '__main__':
    solve()