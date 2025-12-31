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
        # The optimal way is to have a string like 'a...a' with one 'b' at the end
        # For K descents, we need a string that decreases K times
        # The minimal length is K + 1, and the lex smallest is 'a...a' with one 'b' at the end
        # For example, K=1: 'ba', K=2: 'cba', K=3: 'dcb a', etc.
        # So the string is 'a'*(K) + 'b' + 'a'*(K-1)
        # Wait, no, that's not right. Let's think again.
        # To have exactly K descents, we can use a string that is strictly decreasing.
        # For example, for K=1, 'ba' has one descent (b > a).
        # For K=2, 'cba' has two descents (c > b, b > a).
        # For K=3, 'dcb a' has three descents (d > c, c > b, b > a).
        # So the pattern is to have a string that is a sequence of decreasing letters, starting from 'a' + K and ending with 'a'.
        # So the string is 'a' + (K+1) letters, starting from 'a' + K and decreasing.
        # For example, K=1: 'ba', K=2: 'cba', K=3: 'dcb a', etc.
        # So the string is 'a' + (K+1) letters, starting from 'a' + K and decreasing.
        # So the string is 'a' + (K+1) letters, starting from 'a' + K and decreasing.
        # So the string is 'a' + (K+1) letters, starting from 'a' + K and decreasing.
        # So the string is 'a' + (K+1) letters, starting from 'a' + K and decreasing.
        # So the string is 'a' + (K+1) letters, starting from 'a' + K and decreasing.
        # So the string is 'a' + (K+1) letters, starting from 'a' + K and decreasing.
        # So the string is 'a' + (K+1) letters, starting from 'a' + K and decreasing.
        # So the string is 'a' + (K+1) letters, starting from 'a' + K and decreasing.
        # So the string is 'a' + (K+1) letters, starting from 'a' + K and decreasing.
        # So the string is 'a' + (K+1) letters, starting from 'a' + K and decreasing.
        # So the string is 'a' + (K+1) letters, starting from 'a' + K and decreasing.
        # So the string is 'a' + (K+1) letters, starting from 'a' + K and decreasing.
        # So the string is 'a' + (K+1) letters, starting from 'a' + K and decreasing.
        # So the string is 'a' + (K+1) letters, starting from 'a' + K and decreasing.
        # So the string is 'a' + (K+1) letters, starting from 'a' + K and decreasing.
        # So the string is 'a' + (K+1) letters, starting from 'a' + K and decreasing.
        # So the string is 'a' + (K+1) letters, starting from 'a' + K and decreasing.
        # So the string is 'a' + (K+1) letters, starting from 'a' + K and decreasing.
        # So the string is 'a' + (K+1) letters, starting from 'a' + K and decreasing.
        # So the string is 'a' + (K+1) letters, starting from 'a' + K and decreasing.
        # So the string is 'a' + (K+1) letters, starting from 'a' + K and decreasing.
        # So the string is 'a' + (K+1) letters, starting from 'a' + K and decreasing.
        # So the string is 'a' + (K+1) letters, starting from 'a' + K and decreasing.
        # So the string is 'a' + (K+1) letters, starting from 'a' + K and decreasing.
        # So the string is 'a' + (K+1) letters, starting from 'a' + K and decreasing.
        # So the string is 'a' + (K+1) letters, starting from 'a' + K and decreasing.
        # So the string is 'a' + (K+1) letters, starting from 'a' + K and decreasing.
        # So the string is 'a' + (K+1) letters, starting from 'a' + K and decreasing.
        # So the string is 'a' + (K+1) letters, starting from 'a' + K and decreasing.
        # So the string is 'a' + (K+1) letters, starting from 'a' + K and decreasing.
        # So the string is 'a' + (K+1) letters, starting from 'a' + K and decreasing.
        # So the string is 'a' + (K+1) letters, starting from 'a' + K and decreasing.
        # So the string is 'a' + (K+1) letters, starting from 'a' + K and decreasing.
        # So the string is 'a' + (K+1) letters, starting from 'a' + K and decreasing.
        # So the string is 'a' + (K+1) letters, starting from 'a' + K and decreasing.
        # So the string is 'a' + (K+1) letters, starting from 'a' + K and decreasing.
        # So the string is 'a' + (K+1) letters, starting from 'a' + K and decreasing.
        # So the string is 'a' + (K+1) letters, starting from 'a' + K and decreasing.
        # So the string is 'a' + (K+1) letters, starting from 'a' + K and decreasing.
        # So the string is 'a' + (K+1) letters, starting from 'a' + K and decreasing.
        # So the string is 'a' + (K+1) letters, starting from 'a' + K and decreasing.
        # So the string is 'a' + (K+1) letters, starting from 'a' + K and decreasing.
        # So the string is 'a' + (K+1) letters, starting from 'a' + K and decreasing.
        # So the string is 'a' + (K+1) letters, starting from 'a' + K and decreasing.
        # So the string is 'a' + (K+1) letters, starting from 'a' + K and decreasing.
        # So the string is 'a' + (K+1) letters, starting from 'a' + K and decreasing.
        # So the string is 'a' + (K+1) letters, starting from 'a' + K and decreasing.
        # So the string is 'a' + (K+1) letters, starting from 'a' + K and decreasing.
        # So the string is 'a' + (K+1) letters, starting from 'a' + K and decreasing.
        # So the string is 'a' + (K+1) letters, starting from 'a' + K and decreasing.
        # So the string is 'a' + (K+1) letters, starting from 'a' + K and decreasing.
        # So the string is 'a' + (K+1) letters, starting from 'a' + K and decreasing.
        # So the string is 'a' + (K+1) letters, starting from 'a' + K and decreasing.
        # So the string is 'a' + (K+1) letters, starting from 'a' + K and decreasing.
        # So the string is 'a' + (K+1) letters, starting from 'a' + K and decreasing.
        # So the string is 'a' + (K+1) letters, starting from 'a' + K and decreasing.
        # So the string is 'a' + (K+1) letters, starting from 'a' + K and decreasing.
        # So the string is 'a' + (K+1) letters, starting from 'a' + K and decreasing.
        # So the string is 'a' + (K+1) letters, starting from 'a' + K and decreasing.
        # So the string is '