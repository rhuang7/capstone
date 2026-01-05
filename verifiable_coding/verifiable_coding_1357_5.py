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
                if five == 0:
                    possible = False
                    break
                five -= 1
                ten += 1
            elif coin == 15:
                if five >= 1 and ten >= 1:
                    five -= 1
                    ten -= 1
                    fifteen += 1
                else:
                    possible = False
                    break
        
        print("YES" if possible else "NO")

if __name__ == '__main__':
    solve()