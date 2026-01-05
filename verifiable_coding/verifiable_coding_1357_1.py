import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    T = int(data[idx])
    idx += 1
    for _ in range(T):
        N = int(data[idx])
        idx += 1
        a = list(map(int, data[idx:idx+N]))
        idx += N
        five = 0
        ten = 0
        fifteen = 0
        possible = True
        for coin in a:
            if coin == 5:
                five += 1
            elif coin == 10:
                if five > 0:
                    five -= 1
                    ten += 1
                else:
                    possible = False
                    break
            elif coin == 15:
                if five > 0 and ten > 0:
                    five -= 1
                    ten -= 1
                    fifteen += 1
                else:
                    possible = False
                    break
        if possible:
            print("YES")
        else:
            print("NO")

if __name__ == '__main__':
    solve()