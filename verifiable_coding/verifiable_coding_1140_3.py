import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    index = 1
    for _ in range(T):
        p = int(data[index])
        idx = int(data[index + 1])
        index += 2
        
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
        
        a = list(range(1 << p))
        result = order(a, 0)
        print(result[idx])

if __name__ == '__main__':
    solve()