import sys
MOD = 10**9 + 7

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    T = int(data[0])
    index = 1
    
    for _ in range(T):
        N = int(data[index])
        S = data[index + 1]
        index += 2
        
        len_S = len(S)
        
        if len_S == 0:
            print(0)
            continue
        
        if N < len_S:
            print(0)
            continue
        
        # Number of ways to choose a substring to delete
        # Total ways = (N + 1) * (N) / 2 - (len_S + 1) * len_S / 2
        # But we need to subtract the cases where the remaining string is S
        # So total valid ways = total ways - (number of ways to delete a substring such that remaining is S)
        
        # Total ways to delete a substring of non-zero length
        total_ways = (N * (N + 1)) // 2
        
        # Number of ways to delete a substring such that remaining is S
        # This is equal to the number of ways to choose a substring to delete from M such that the remaining is S
        # Which is equal to the number of ways to choose a substring to delete from M such that the remaining is S
        # Which is equal to the number of possible positions to delete a substring that leaves S
        
        # The length of M is N, and the length of S is len_S
        # So the length of the substring to delete is N - len_S
        # So the number of ways is (N - len_S + 1) * (N - len_S + 2) // 2
        
        # But we need to subtract the cases where the substring to delete is such that the remaining is S
        # Which is equal to the number of ways to choose a substring to delete from M such that the remaining is S
        # Which is equal to the number of ways to choose a substring to delete from M such that the remaining is S
        # Which is equal to the number of ways to choose a substring to delete from M such that the remaining is S
        
        # The number of such ways is (N - len_S + 1) * (N - len_S + 2) // 2
        
        # But we need to subtract the cases where the substring to delete is such that the remaining is S
        # Which is equal to the number of ways to choose a substring to delete from M such that the remaining is S
        # Which is equal to the number of ways to choose a substring to delete from M such that the remaining is S
        
        # So the answer is total_ways - (N - len_S + 1) * (N - len_S + 2) // 2
        
        # But this is only valid if N - len_S >= 0
        if N - len_S < 0:
            print(0)
            continue
        
        ways_to_delete = (N - len_S + 1) * (N - len_S + 2) // 2
        
        answer = (total_ways - ways_to_delete) % MOD
        print(answer)
        
if __name__ == '__main__':
    solve()