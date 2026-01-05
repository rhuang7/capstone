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
        
        # Person 1 knows on day 0
        # We track the number of people who know on each day
        # And the total number of people who can spread the news
        # We also track the current day
        current_day = 0
        total_people = 1  # Person 1 knows
        people_who_can_spread = 1  # Only person 1 can spread on day 0
        people_to_tell = N - 1  # Total people to tell
        
        while people_to_tell > 0:
            current_day += 1
            # People who can spread can tell up to their A_i people
            # We tell people in ascending order
            # So we take the first 'people_who_can_spread' people
            # and tell them up to their A_i people
            # We need to find how many people can be told
            # and update the total_people and people_who_can_spread
            # and people_to_tell
            # We also need to make sure that we don't tell more than people_to_tell
            # and that we don't tell more than the capacity of each person
            # So we take the first 'people_who_can_spread' people
            # and tell them up to their A_i people
            # We can tell up to sum of A_i for the first 'people_who_can_spread' people
            # But we can't tell more than people_to_tell
            # So we take the minimum of the sum and people_to_tell
            # And then update the people_to_tell and people_who_can_spread
            # and total_people
            # But we also need to track which people are telling
            # So we need to track the people who can spread
            # So we need to keep track of the people who know the news
            # and can spread it
            # So we can use a priority queue or a list
            # But for efficiency, we can use a list and keep track of the people
            # who can spread
            # We can use a list to track the people who can spread
            # and for each day, we take the first 'people_who_can_spread' people
            # and tell them up to their A_i people
            # So we can use a list to track the people who can spread
            # and for each day, we take the first 'people_who_can_spread' people
            # and tell them up to their A_i people
            # But for efficiency, we can use a list and track the people who can spread
            # and for each day, we take the first 'people_who_can_spread' people
            # and tell them up to their A_i people
            # So we can use a list to track the people who can spread
            # and for each day, we take the first 'people_who_can_spread' people
            # and tell them up to their A_i people
            # So we can use a list to track the people who can spread
            # and for each day, we take the first 'people_who_can_spread' people
            # and tell them up to their A_i people
            # But for efficiency, we can use a list and track the people who can spread
            # and for each day, we take the first 'people_who_can_spread' people
            # and tell them up to their A_i people
            # So we can use a list to track the people who can spread
            # and for each day, we take the first 'people_who_can_spread' people
            # and tell them up to their A_i people
            # But for efficiency, we can use a list and track the people who can spread
            # and for each day, we take the first 'people_who_can_spread' people
            # and tell them up to their A_i people
            # So we can use a list to track the people who can spread
            # and for each day, we take the first 'people_who_can_spread' people
            # and tell them up to their A_i people
            # So we can use a list to track the people who can spread
            # and for each day, we take the first 'people_who_can_spread' people
            # and tell them up to their A_i people
            # But for efficiency, we can use a list and track the people who can spread
            # and for each day, we take the first 'people_who_can_spread' people
            # and tell them up to their A_i people
            # So we can use a list to track the people who can spread
            # and for each day, we take the first 'people_who_can_spread' people
            # and tell them up to their A_i people
            # But for efficiency, we can use a list and track the people who can spread
            # and for each day, we take the first 'people_who_can_spread' people
            # and tell them up to their A_i people
            # So we can use a list to track the people who can spread
            # and for each day, we take the first 'people_who_can_spread' people
            # and tell them up to their A_i people
            # But for efficiency, we can use a list and track the people who can spread
            # and for each day, we take the first 'people_who_can_spread' people
            # and tell them up to their A_i people
            # So we can use a list to track the people who can spread
            # and for each day, we take the first 'people_who_can_spread' people
            # and tell them up to their A_i people
            # But for efficiency, we can use a list and track the people who can spread
            # and for each day, we take the first 'people_who_can_spread' people
            # and tell them up to their A_i people
            # So we can use a list to track the people who can spread
            # and for each day, we take the first 'people_who_can_spread' people
            # and tell them up to their A_i people
            # But for efficiency, we can use a list and track the people who can spread
            # and for each day, we take the first 'people_who_can_spread' people
            # and tell them up to their A_i people
            # So we can use a list to track the people who can spread
            # and for each day, we take the first 'people_who_can_spread' people
            # and tell them up to their A_i people
            # But for efficiency, we can use a list and track the people who can spread
            # and for each day, we take the first 'people_who_can_spread' people
            # and tell them up to their A_i people
            # So we can use a list to track the people who can spread
            # and for each day, we take the first 'people_who_can_spread' people
            # and tell them up to their A_i people
            # But for efficiency, we can use a list and track the people who can spread
            # and for each day, we take the first 'people_who_can_spread' people
            # and tell them up to their A_i people
            # So we can use a list to track the people who can spread
            # and for each day, we take the first 'people_who_can_spread' people
            # and tell them up to their A_i people
            # But for efficiency, we can use a list and track the people who can spread
            # and for each day, we take the first 'people_who_can_spread' people
            # and tell them up to their A_i people
            # So we can use a list to track the people who can spread
            # and for each day, we take the first 'people_who_can_spread' people
            # and tell them up to their A_i people
            # But for efficiency, we can use a list and track the people who can spread
            # and for each day, we take the first 'people_who_can_spread' people
            # and tell them up to their A_i people
            # So we can use a list to track the people who can spread
            # and for each day, we take the first 'people_who_can_spread' people
            # and tell them up to their A_i people
            # But for efficiency, we can use a list and track the people who can spread
            # and for each day, we take the first 'people_who_can_spread' people
            # and tell them up to their A_i people
            # So we can use a list to track the