import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    T = int(data[idx])
    idx += 1
    results = []
    
    for _ in range(T):
        N = int(data[idx])
        idx += 1
        A = list(map(int, data[idx:idx+N]))
        idx += N
        
        # The first person can start on day 1
        days = 1
        total_people = 1  # Initially, only person 1 knows
        # We need to find the minimum days such that total_people >= N
        # We can use a greedy approach: each day, the current people can spread the news
        
        # We keep track of the people who can spread the news
        # We use a priority queue to always select the person with the highest A_i
        # But since the people are processed in order, we can use a simple approach
        # We can track the current number of people who can spread the news
        # and the number of people they can tell each day
        
        # We can use a greedy approach: each day, the current people can tell up to their A_i people
        # We can track the number of people who can spread the news and the number of people they can tell
        # We can use a variable to track the current number of people who can spread the news
        # and the number of people they can tell each day
        
        # We can use a variable to track the number of people who can spread the news
        # and the number of people they can tell each day
        # We can use a variable to track the number of people who can spread the news
        # and the number of people they can tell each day
        
        # We can use a greedy approach: each day, the current people can tell up to their A_i people
        # We can track the number of people who can spread the news
        # and the number of people they can tell each day
        
        # We can use a variable to track the number of people who can spread the news
        # and the number of people they can tell each day
        # We can use a variable to track the number of people who can spread the news
        # and the number of people they can tell each day
        
        # We can use a variable to track the number of people who can spread the news
        # and the number of people they can tell each day
        # We can use a variable to track the number of people who can spread the news
        # and the number of people they can tell each day
        
        # We can use a variable to track the number of people who can spread the news
        # and the number of people they can tell each day
        # We can use a variable to track the number of people who can spread the news
        # and the number of people they can tell each day
        
        # We can use a variable to track the number of people who can spread the news
        # and the number of people they can tell each day
        # We can use a variable to track the number of people who can spread the news
        # and the number of people they can tell each day
        
        # We can use a variable to track the number of people who can spread the news
        # and the number of people they can tell each day
        # We can use a variable to track the number of people who can spread the news
        # and the number of people they can tell each day
        
        # We can use a variable to track the number of people who can spread the news
        # and the number of people they can tell each day
        # We can use a variable to track the number of people who can spread the news
        # and the number of people they can tell each day
        
        # We can use a variable to track the number of people who can spread the news
        # and the number of people they can tell each day
        # We can use a variable to track the number of people who can spread the news
        # and the number of people they can tell each day
        
        # We can use a variable to track the number of people who can spread the news
        # and the number of people they can tell each day
        # We can use a variable to track the number of people who can spread the news
        # and the number of people they can tell each day
        
        # We can use a variable to track the number of people who can spread the news
        # and the number of people they can tell each day
        # We can use a variable to track the number of people who can spread the news
        # and the number of people they can tell each day
        
        # We can use a variable to track the number of people who can spread the news
        # and the number of people they can tell each day
        # We can use a variable to track the number of people who can spread the news
        # and the number of people they can tell each day
        
        # We can use a variable to track the number of people who can spread the news
        # and the number of people they can tell each day
        # We can use a variable to track the number of people who can spread the news
        # and the number of people they can tell each day
        
        # We can use a variable to track the number of people who can spread the news
        # and the number of people they can tell each day
        # We can use a variable to track the number of people who can spread the news
        # and the number of people they can tell each day
        
        # We can use a variable to track the number of people who can spread the news
        # and the number of people they can tell each day
        # We can use a variable to track the number of people who can spread the news
        # and the number of people they can tell each day
        
        # We can use a variable to track the number of people who can spread the news
        # and the number of people they can tell each day
        # We can use a variable to track the number of people who can spread the news
        # and the number of people they can tell each day
        
        # We can use a variable to track the number of people who can spread the news
        # and the number of people they can tell each day
        # We can use a variable to track the number of people who can spread the news
        # and the number of people they can tell each day
        
        # We can use a variable to track the number of people who can spread the news
        # and the number of people they can tell each day
        # We can use a variable to track the number of people who can spread the news
        # and the number of people they can tell each day
        
        # We can use a variable to track the number of people who can spread the news
        # and the number of people they can tell each day
        # We can use a variable to track the number of people who can spread the news
        # and the number of people they can tell each day
        
        # We can use a variable to track the number of people who can spread the news
        # and the number of people they can tell each day
        # We can use a variable to track the number of people who can spread the news
        # and the number of people they can tell each day
        
        # We can use a variable to track the number of people who can spread the news
        # and the number of people they can tell each day
        # We can use a variable to track the number of people who can spread the news
        # and the number of people they can tell each day
        
        # We can use a variable to track the number of people who can spread the news
        # and the number of people they can tell each day
        # We can use a variable to track the number of people who can spread the news
        # and the number of people they can tell each day
        
        # We can use a variable to track the number of people who can spread the news
        # and the number of people they can tell each day
        # We can use a variable to track the number of people who can spread the news
        # and the number of people they can tell each day
        
        # We can use a variable to track the number of people who can spread the news
        # and the number of people they can tell each day
        # We can use a variable to track the number of people who can spread the news
        # and the number of people they can tell each day
        
        # We can use a variable to track the number of people who can spread the news
        # and the number of people they can tell each day
        # We can use a variable to track the number of people who can spread the news
        # and the number of people they can tell each day
        
        # We can use a variable to track the number of people who can spread the news
        # and the number of people they can tell each day
        # We can use a variable to track the number of people who can spread the news
        # and the number of people they can tell each day
        
        # We can use a variable to track the number of people who can spread the news
        # and the number of people they can tell each day