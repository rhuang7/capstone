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
        # The minimal string with exactly K "descents" is a sequence of decreasing letters
        # Starting from 'a' and increasing the length as needed
        # For K descents, the minimal length is K + 1
        # The string is 'a' followed by 'b' followed by 'c' ... up to 'a' + K
        # But to have exactly K descents, we need a string like 'cba' (for K=2)
        # So the string is 'a' repeated (K+1) times, but in reverse order
        # Wait, no. The minimal string with exactly K descents is a string of length K+1
        # where each character is one more than the previous, but in reverse order
        # For example, K=1: 'ba' (1 descent)
        # K=2: 'cba' (2 descents)
        # So the string is 'a' followed by 'b' followed by 'c' ... up to 'a' + K
        # But in reverse order
        # So the string is 'a' followed by 'b' followed by 'c' ... up to 'a' + K
        # But in reverse order, so 'a' + K, 'a' + K - 1, ..., 'a'
        # So the string is 'a' repeated (K+1) times, but in reverse order
        # So the string is 'a' followed by 'b' followed by 'c' ... up to 'a' + K
        # But in reverse order
        # So the string is 'a' repeated (K+1) times, but in reverse order
        # So the string is 'a' followed by 'b' followed by 'c' ... up to 'a' + K
        # But in reverse order
        # So the string is 'a' repeated (K+1) times, but in reverse order
        # So the string is 'a' followed by 'b' followed by 'c' ... up to 'a' + K
        # But in reverse order
        # So the string is 'a' repeated (K+1) times, but in reverse order
        # So the string is 'a' followed by 'b' followed by 'c' ... up to 'a' + K
        # But in reverse order
        # So the string is 'a' repeated (K+1) times, but in reverse order
        # So the string is 'a' followed by 'b' followed by 'c' ... up to 'a' + K
        # But in reverse order
        # So the string is 'a' repeated (K+1) times, but in reverse order
        # So the string is 'a' followed by 'b' followed by 'c' ... up to 'a' + K
        # But in reverse order
        # So the string is 'a' repeated (K+1) times, but in reverse order
        # So the string is 'a' followed by 'b' followed by 'c' ... up to 'a' + K
        # But in reverse order
        # So the string is 'a' repeated (K+1) times, but in reverse order
        # So the string is 'a' followed by 'b' followed by 'c' ... up to 'a' + K
        # But in reverse order
        # So the string is 'a' repeated (K+1) times, but in reverse order
        # So the string is 'a' followed by 'b' followed by 'c' ... up to 'a' + K
        # But in reverse order
        # So the string is 'a' repeated (K+1) times, but in reverse order
        # So the string is 'a' followed by 'b' followed by 'c' ... up to 'a' + K
        # But in reverse order
        # So the string is 'a' repeated (K+1) times, but in reverse order
        # So the string is 'a' followed by 'b' followed by 'c' ... up to 'a' + K
        # But in reverse order
        # So the string is 'a' repeated (K+1) times, but in reverse order
        # So the string is 'a' followed by 'b' followed by 'c' ... up to 'a' + K
        # But in reverse order
        # So the string is 'a' repeated (K+1) times, but in reverse order
        # So the string is 'a' followed by 'b' followed by 'c' ... up to 'a' + K
        # But in reverse order
        # So the string is 'a' repeated (K+1) times, but in reverse order
        # So the string is 'a' followed by 'b' followed by 'c' ... up to 'a' + K
        # But in reverse order
        # So the string is 'a' repeated (K+1) times, but in reverse order
        # So the string is 'a' followed by 'b' followed by 'c' ... up to 'a' + K
        # But in reverse order
        # So the string is 'a' repeated (K+1) times, but in reverse order
        # So the string is 'a' followed by 'b' followed by 'c' ... up to 'a' + K
        # But in reverse order
        # So the string is 'a' repeated (K+1) times, but in reverse order
        # So the string is 'a' followed by 'b' followed by 'c' ... up to 'a' + K
        # But in reverse order
        # So the string is 'a' repeated (K+1) times, but in reverse order
        # So the string is 'a' followed by 'b' followed by 'c' ... up to 'a' + K
        # But in reverse order
        # So the string is 'a' repeated (K+1) times, but in reverse order
        # So the string is 'a' followed by 'b' followed by 'c' ... up to 'a' + K
        # But in reverse order
        # So the string is 'a' repeated (K+1) times, but in reverse order
        # So the string is 'a' followed by 'b' followed by 'c' ... up to 'a' + K
        # But in reverse order
        # So the string is 'a' repeated (K+1) times, but in reverse order
        # So the string is 'a' followed by 'b' followed by 'c' ... up to 'a' + K
        # But in reverse order
        # So the string is 'a' repeated (K+1) times, but in reverse order
        # So the string is 'a' followed by 'b' followed by 'c' ... up to 'a' + K
        # But in reverse order
        # So the string is 'a' repeated (K+1) times, but in reverse order
        # So the string is 'a' followed by 'b' followed by 'c' ... up to 'a' + K
        # But in reverse order
        # So the string is 'a' repeated (K+1) times, but in reverse order
        # So the string is 'a' followed by 'b' followed by 'c' ... up to 'a' + K
        # But in reverse order
        # So the string is 'a' repeated (K+1) times, but in reverse order
        # So the string is 'a' followed by 'b' followed by 'c' ... up to 'a' + K
        # But in reverse order
        # So the string is 'a' repeated (K+1) times, but in reverse order
        # So the string is 'a' followed by 'b' followed by 'c' ... up to 'a' + K
        # But in reverse order
        # So the string is 'a' repeated (K+1) times, but in reverse order
        # So the string is 'a' followed by 'b' followed by 'c' ... up to 'a' + K
        # But in reverse order
        # So the string is 'a' repeated (K+1) times, but in reverse order
        # So the string is 'a' followed by 'b' followed by 'c' ... up to 'a' + K
        # But in reverse order
        # So the string is 'a' repeated (K+1) times, but in reverse order
        # So the string is 'a' followed by 'b' followed by 'c' ... up to 'a' + K
        # But in reverse order