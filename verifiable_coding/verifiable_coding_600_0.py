import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    N_list = list(map(int, data[1:T+1]))
    
    def last_remaining_number(N):
        if N == 1:
            return 0
        if N % 2 == 1:
            return last_remaining_number((N + 1) // 2)
        else:
            return last_remaining_number(N // 2)
    
    for N in N_list:
        print(last_remaining_number(N))

if __name__ == '__main__':
    solve()