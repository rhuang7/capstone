import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    cases = data[1:T+1]
    
    for S in cases:
        n = len(S)
        max_len = 1
        for i in range(n):
            freq = {}
            left = i
            right = i
            while right < n:
                freq[S[right]] = freq.get(S[right], 0) + 1
                if len(freq) <= 2:
                    if (right - left + 1) > max_len:
                        max_len = right - left + 1
                else:
                    break
                right += 1
        print(max_len)

if __name__ == '__main__':
    solve()