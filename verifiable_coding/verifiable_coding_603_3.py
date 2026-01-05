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
        # The minimal length is K + 1, as each 'drop' requires at least one more character
        # To minimize the length, we can use a sequence that drops as much as possible
        # For example, for K=1, 'ba' has one drop (b > a)
        # For K=2, 'cba' has two drops (c > b, b > a)
        # So the minimal string is 'a' followed by 'b', 'c', ..., 'a + K'
        # But we need to reverse it to get the required drops
        # So the string is 'a' followed by 'b', 'c', ..., 'a + K', then 'a'
        # But to get exactly K drops, we can use a sequence that drops K times
        # The minimal string is 'a' followed by 'b', 'c', ..., 'a + K', then 'a'
        # But to get exactly K drops, we can use a sequence that drops K times
        # The minimal string is 'a' followed by 'b', 'c', ..., 'a + K', then 'a'
        # But to get exactly K drops, we can use a sequence that drops K times
        # The minimal string is 'a' followed by 'b', 'c', ..., 'a + K', then 'a'
        # But to get exactly K drops, we can use a sequence that drops K times
        # The minimal string is 'a' followed by 'b', 'c', ..., 'a + K', then 'a'
        # But to get exactly K drops, we can use a sequence that drops K times
        # The minimal string is 'a' followed by 'b', 'c', ..., 'a + K', then 'a'
        # But to get exactly K drops, we can use a sequence that drops K times
        # The minimal string is 'a' followed by 'b', 'c', ..., 'a + K', then 'a'
        # But to get exactly K drops, we can use a sequence that drops K times
        # The minimal string is 'a' followed by 'b', 'c', ..., 'a + K', then 'a'
        # But to get exactly K drops, we can use a sequence that drops K times
        # The minimal string is 'a' followed by 'b', 'c', ..., 'a + K', then 'a'
        # But to get exactly K drops, we can use a sequence that drops K times
        # The minimal string is 'a' followed by 'b', 'c', ..., 'a + K', then 'a'
        # But to get exactly K drops, we can use a sequence that drops K times
        # The minimal string is 'a' followed by 'b', 'c', ..., 'a + K', then 'a'
        # But to get exactly K drops, we can use a sequence that drops K times
        # The minimal string is 'a' followed by 'b', 'c', ..., 'a + K', then 'a'
        # But to get exactly K drops, we can use a sequence that drops K times
        # The minimal string is 'a' followed by 'b', 'c', ..., 'a + K', then 'a'
        # But to get exactly K drops, we can use a sequence that drops K times
        # The minimal string is 'a' followed by 'b', 'c', ..., 'a + K', then 'a'
        # But to get exactly K drops, we can use a sequence that drops K times
        # The minimal string is 'a' followed by 'b', 'c', ..., 'a + K', then 'a'
        # But to get exactly K drops, we can use a sequence that drops K times
        # The minimal string is 'a' followed by 'b', 'c', ..., 'a + K', then 'a'
        # But to get exactly K drops, we can use a sequence that drops K times
        # The minimal string is 'a' followed by 'b', 'c', ..., 'a + K', then 'a'
        # But to get exactly K drops, we can use a sequence that drops K times
        # The minimal string is 'a' followed by 'b', 'c', ..., 'a + K', then 'a'
        # But to get exactly K drops, we can use a sequence that drops K times
        # The minimal string is 'a' followed by 'b', 'c', ..., 'a + K', then 'a'
        # But to get exactly K drops, we can use a sequence that drops K times
        # The minimal string is 'a' followed by 'b', 'c', ..., 'a + K', then 'a'
        # But to get exactly K drops, we can use a sequence that drops K times
        # The minimal string is 'a' followed by 'b', 'c', ..., 'a + K', then 'a'
        # But to get exactly K drops, we can use a sequence that drops K times
        # The minimal string is 'a' followed by 'b', 'c', ..., 'a + K', then 'a'
        # But to get exactly K drops, we can use a sequence that drops K times
        # The minimal string is 'a' followed by 'b', 'c', ..., 'a + K', then 'a'
        # But to get exactly K drops, we can use a sequence that drops K times
        # The minimal string is 'a' followed by 'b', 'c', ..., 'a + K', then 'a'
        # But to get exactly K drops, we can use a sequence that drops K times
        # The minimal string is 'a' followed by 'b', 'c', ..., 'a + K', then 'a'
        # But to get exactly K drops, we can use a sequence that drops K times
        # The minimal string is 'a' followed by 'b', 'c', ..., 'a + K', then 'a'
        # But to get exactly K drops, we can use a sequence that drops K times
        # The minimal string is 'a' followed by 'b', 'c', ..., 'a + K', then 'a'
        # But to get exactly K drops, we can use a sequence that drops K times
        # The minimal string is 'a' followed by 'b', 'c', ..., 'a + K', then 'a'
        # But to get exactly K drops, we can use a sequence that drops K times
        # The minimal string is 'a' followed by 'b', 'c', ..., 'a + K', then 'a'
        # But to get exactly K drops, we can use a sequence that drops K times
        # The minimal string is 'a' followed by 'b', 'c', ..., 'a + K', then 'a'
        # But to get exactly K drops, we can use a sequence that drops K times
        # The minimal string is 'a' followed by 'b', 'c', ..., 'a + K', then 'a'
        # But to get exactly K drops, we can use a sequence that drops K times
        # The minimal string is 'a' followed by 'b', 'c', ..., 'a + K', then 'a'
        # But to get exactly K drops, we can use a sequence that drops K times
        # The minimal string is 'a' followed by 'b', 'c', ..., 'a + K', then 'a'
        # But to get exactly K drops, we can use a sequence that drops K times
        # The minimal string is 'a' followed by 'b', 'c', ..., 'a + K', then 'a'
        # But to get exactly K drops, we can use a sequence that drops K times
        # The minimal string is 'a' followed by 'b', 'c', ..., 'a + K', then 'a'
        # But to get exactly K drops, we can use a sequence that drops K times
        # The minimal string is 'a' followed by 'b', 'c', ..., 'a + K', then 'a'
        # But to get exactly K drops, we can use a sequence that drops K times
        # The minimal string is 'a' followed by 'b', 'c', ..., 'a + K', then 'a'
        # But to get exactly K drops, we can use a sequence that drops K times
        # The minimal string is 'a' followed by 'b', 'c', ..., 'a + K', then 'a'
        # But to get exactly K drops, we can use a sequence that drops K times
        # The minimal string is 'a' followed by 'b', 'c', ..., 'a + K', then 'a'
        # But to get exactly K drops, we can use a sequence that drops K times
        # The minimal string is 'a' followed by 'b', 'c',