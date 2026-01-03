import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    index = 1
    for _ in range(T):
        p = int(data[index])
        idx = int(data[index+1])
        index += 2
        
        size = 1 << p  # 2^p
        result = [0] * size
        
        def order(arr, i):
            if len(arr) <= 1:
                return arr
            l = []
            r = []
            n = len(arr) - 1
            power = 1 << i
            for j in range(len(arr)):
                if (arr[j] % (power << 1)) < power:
                    l.append(arr[j])
                else:
                    r.append(arr[j])
            l = order(l, i + 1)
            r = order(r, i + 1)
            return l + r
        
        a = list(range(size))
        final = order(a, 0)
        print(final[idx])

if __name__ == '__main__':
    solve()