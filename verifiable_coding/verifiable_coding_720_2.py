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
            cnt_0_local = 0
            cnt_1_local = 0
            for j in range(i, len(s)):
                if s[j] == '0':
                    cnt_0_local += 1
                else:
                    cnt_1_local += 1
                if cnt_0_local == cnt_1_local * cnt_1_local:
                    beauty += 1
        print(beauty)

if __name__ == '__main__':
    solve()