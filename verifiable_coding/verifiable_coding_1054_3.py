import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    T = int(data[0])
    cases = data[1:T+1]
    
    for s in cases:
        n = len(s)
        left = 0
        right = n - 1
        res = list(s)
        possible = True
        
        while left < right:
            if res[left] == res[right]:
                left += 1
                right -= 1
            elif res[left] == '.':
                res[left] = res[right]
                left += 1
                right -= 1
            elif res[right] == '.':
                res[right] = res[left]
                left += 1
                right -= 1
            else:
                possible = False
                break
        
        if not possible:
            print(-1)
        else:
            # Fill remaining '.' with 'a' for lex smallest
            for i in range(n):
                if res[i] == '.':
                    res[i] = 'a'
            print(''.join(res))
    
if __name__ == '__main__':
    solve()