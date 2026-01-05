import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    Ks = list(map(int, data[1:]))
    
    def is_beautiful(n):
        while n > 0:
            if n & 1:
                n >>= 1
                if n & 1:
                    return False
            else:
                n >>= 1
        return True
    
    def find_previous_beautiful(n):
        while True:
            if is_beautiful(n):
                return n
            n -= 1
    
    for K in Ks:
        if is_beautiful(K):
            print(K)
        else:
            print(find_previous_beautiful(K))
    
if __name__ == '__main__':
    solve()