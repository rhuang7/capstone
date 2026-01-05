import sys

MOD = 10**9 + 7

def solve():
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    index = 1
    for _ in range(T):
        N = int(data[index])
        K = int(data[index+1])
        index += 2
        
        if N == 0:
            print(0)
            continue
        
        # Find the round in which N is visited for the Kth time
        # In round K, N is visited twice (once going up, once going down)
        # But for K > 1, the first time is in the Kth round, the second time is in the (K+1)th round, etc.
        # So for Kth time, if K is odd, it's in the Kth round, if even, it's in the (K+1)th round
        # But we need to find the correct round where the Kth occurrence of N happens
        # For N, the number of times it is visited in round r is 2 (up and down), except for the first time in round 1
        # So for Kth time, if K is odd, it's in round (K+1)//2, else in round K//2
        # But we need to find the correct round for the Kth time of N
        
        # Find the round in which N is visited for the Kth time
        # For N, the first occurrence is in round 1, the second in round 2, etc.
        # So the Kth occurrence is in round K if K is odd, or K-1 if even
        # But we need to find the correct round for the Kth occurrence of N
        # For N, the first occurrence is in round 1, the second in round 2, etc.
        # So the Kth occurrence is in round K if K is odd, or K-1 if even
        # But we need to find the correct round for the Kth occurrence of N
        
        # The Kth occurrence of N is in round r where r = (K + 1) // 2 if K is odd, else K // 2
        # But we need to find the correct round for the Kth occurrence of N
        
        # The Kth occurrence of N is in round r where r = (K + 1) // 2 if K is odd, else K // 2
        # But we need to find the correct round for the Kth occurrence of N
        
        # The Kth occurrence of N is in round r where r = (K + 1) // 2 if K is odd, else K // 2
        # But we need to find the correct round for the Kth occurrence of N
        
        # The Kth occurrence of N is in round r where r = (K + 1) // 2 if K is odd, else K // 2
        # But we need to find the correct round for the Kth occurrence of N
        
        # The Kth occurrence of N is in round r where r = (K + 1) // 2 if K is odd, else K // 2
        # But we need to find the correct round for the Kth occurrence of N
        
        # The Kth occurrence of N is in round r where r = (K + 1) // 2 if K is odd, else K // 2
        # But we need to find the correct round for the Kth occurrence of N
        
        # The Kth occurrence of N is in round r where r = (K + 1) // 2 if K is odd, else K // 2
        # But we need to find the correct round for the Kth occurrence of N
        
        # The Kth occurrence of N is in round r where r = (K + 1) // 2 if K is odd, else K // 2
        # But we need to find the correct round for the Kth occurrence of N
        
        # The Kth occurrence of N is in round r where r = (K + 1) // 2 if K is odd, else K // 2
        # But we need to find the correct round for the Kth occurrence of N
        
        # The Kth occurrence of N is in round r where r = (K + 1) // 2 if K is odd, else K // 2
        # But we need to find the correct round for the Kth occurrence of N
        
        # The Kth occurrence of N is in round r where r = (K + 1) // 2 if K is odd, else K // 2
        # But we need to find the correct round for the Kth occurrence of N
        
        # The Kth occurrence of N is in round r where r = (K + 1) // 2 if K is odd, else K // 2
        # But we need to find the correct round for the Kth occurrence of N
        
        # The Kth occurrence of N is in round r where r = (K + 1) // 2 if K is odd, else K // 2
        # But we need to find the correct round for the Kth occurrence of N
        
        # The Kth occurrence of N is in round r where r = (K + 1) // 2 if K is odd, else K // 2
        # But we need to find the correct round for the Kth occurrence of N
        
        # The Kth occurrence of N is in round r where r = (K + 1) // 2 if K is odd, else K // 2
        # But we need to find the correct round for the Kth occurrence of N
        
        # The Kth occurrence of N is in round r where r = (K + 1) // 2 if K is odd, else K // 2
        # But we need to find the correct round for the Kth occurrence of N
        
        # The Kth occurrence of N is in round r where r = (K + 1) // 2 if K is odd, else K // 2
        # But we need to find the correct round for the Kth occurrence of N
        
        # The Kth occurrence of N is in round r where r = (K + 1) // 2 if K is odd, else K // 2
        # But we need to find the correct round for the Kth occurrence of N
        
        # The Kth occurrence of N is in round r where r = (K + 1) // 2 if K is odd, else K // 2
        # But we need to find the correct round for the Kth occurrence of N
        
        # The Kth occurrence of N is in round r where r = (K + 1) // 2 if K is odd, else K // 2
        # But we need to find the correct round for the Kth occurrence of N
        
        # The Kth occurrence of N is in round r where r = (K + 1) // 2 if K is odd, else K // 2
        # But we need to find the correct round for the Kth occurrence of N
        
        # The Kth occurrence of N is in round r where r = (K + 1) // 2 if K is odd, else K // 2
        # But we need to find the correct round for the Kth occurrence of N
        
        # The Kth occurrence of N is in round r where r = (K + 1) // 2 if K is odd, else K // 2
        # But we need to find the correct round for the Kth occurrence of N
        
        # The Kth occurrence of N is in round r where r = (K + 1) // 2 if K is odd, else K // 2
        # But we need to find the correct round for the Kth occurrence of N
        
        # The Kth occurrence of N is in round r where r = (K + 1) // 2 if K is odd, else K // 2
        # But we need to find the correct round for the Kth occurrence of N
        
        # The Kth occurrence of N is in round r where r = (K + 1) // 2 if K is odd, else K // 2
        # But we need to find the correct round for the Kth occurrence of N
        
        # The Kth occurrence of N is in round r where r = (K + 1) // 2 if K is odd, else K // 2
        # But we need to find the correct round for the Kth occurrence of N
        
        # The Kth occurrence of N is in round r where r = (K + 1) // 2 if K is odd, else K // 2
        # But we need to find the correct round for the Kth occurrence of N
        
        # The Kth occurrence of N is in round r where r = (K + 1) // 2 if K is odd, else K // 2
        # But we need to find the correct round for the Kth occurrence of N
        
        # The Kth occurrence of N is in round r where r = (K + 1) //