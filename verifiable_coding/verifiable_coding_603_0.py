import sys

def solve():
    import sys
    input = sys.stdin.buffer.read().split()
    T = int(input[0])
    cases = list(map(int, input[1:T+1]))
    
    for k in cases:
        if k == 0:
            print('a')
            continue
        # Construct the string with exactly k "drops"
        # The minimal length is k + 1, and the lex smallest is 'a' followed by 'b'... 'a' (k times)
        # But to have exactly k drops, we need a sequence that decreases at k positions
        # The lex smallest such string is 'a' followed by 'b'... 'a' (k times)
        # For example, for k=1: 'ba' (1 drop)
        # For k=2: 'cba' (2 drops)
        # So the string is 'a' followed by 'b'... 'a' (k times)
        res = 'a' + 'b' * k
        print(res)

if __name__ == '__main__':
    solve()