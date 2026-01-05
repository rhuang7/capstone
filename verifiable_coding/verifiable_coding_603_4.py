import sys

def solve():
    import sys
    input = sys.stdin.buffer.read().split()
    T = int(input[0])
    K_list = list(map(int, input[1:T+1]))
    
    for K in K_list:
        if K == 0:
            print('a')
            continue
        # Construct the string with exactly K "descents"
        # The minimal length is K + 1, and the lexicographically smallest is 'a' followed by 'b' ... 'a' (K times)
        # For example, K=1: 'ba', K=2: 'cba'
        result = 'a' * (K + 1)
        # Replace the last character with 'a' to create a descent
        result = result[:-1] + 'a'
        # Now replace the first 'a' with 'b' to create the first descent
        result = 'b' + 'a' * K
        print(result)

if __name__ == '__main__':
    solve()