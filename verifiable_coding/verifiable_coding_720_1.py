import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    strings = data[1:T+1]
    
    for s in strings:
        cnt_0 = s.count('0')
        cnt_1 = s.count('1')
        beauty = 0
        for i in range(len(s)):
            zero = 0
            one = 0
            for j in range(i, len(s)):
                if s[j] == '0':
                    zero += 1
                else:
                    one += 1
                if zero == one * one:
                    beauty += 1
        print(beauty)

if __name__ == '__main__':
    solve()