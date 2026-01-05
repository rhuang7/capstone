import sys

def solve():
    import sys
    sys.setrecursionlimit(1000000)
    input = sys.stdin.buffer.read
    data = input().split()
    
    T = int(data[0])
    index = 1
    results = []
    
    def power(x, y):
        return x ** y
    
    def order(arr, i):
        if len(arr) <= 1:
            return arr
        l = []
        r = []
        n = len(arr) - 1
        two_i_plus_1 = power(2, i + 1)
        two_i = power(2, i)
        for j in range(len(arr)):
            if (arr[j] % two_i_plus_1) < two_i:
                l.append(arr[j])
            else:
                r.append(arr[j])
        l = order(l, i + 1)
        r = order(r, i + 1)
        return l + r
    
    for _ in range(T):
        p = int(data[index])
        idx = int(data[index + 1])
        index += 2
        size = power(2, p)
        a = list(range(size))
        result = order(a, 0)
        results.append(str(result[idx]))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()