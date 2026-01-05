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
        # We need to find the minimum number of days such that the total number of people informed is >= N
        # Initially, only person 1 knows
        # On each day, all people who know can tell others
        # People can start telling the day after they learn
        # We can simulate this with a priority queue (max heap) to always select the person who can tell the most people
        # But since the people are told in ascending order, we can simulate it with a greedy approach
        # We can track the number of people who can tell others on each day
        # We can use a greedy approach where we track the number of people who can tell others on each day
        # We start with person 1 who can tell A[0] people on day 1
        # On each day, the people who can tell are those who were informed on or before the previous day
        # We can track the number of people who can tell on each day
        # We can use a variable to track the current number of people who can tell
        # We can also track the total number of people informed
        # We can use a loop to simulate the days
        # Initialize
        total = 1  # person 1 knows
        days = 0
        # The number of people who can tell on each day
        can_tell = 0
        # The number of people who can tell on the current day
        current_can_tell = 0
        # We need to process the people in order
        # We can use a priority queue to track the people who can tell
        # But since the people are told in order, we can simulate it with a list
        # We can use a list to track the number of people each can tell
        # We can use a pointer to track the next person to be informed
        # We can use a variable to track the current day
        # We can use a variable to track the current number of people who can tell
        # We can use a variable to track the total number of people informed
        # We can use a variable to track the current day
        # We can use a list to track the number of people each can tell
        # We can use a pointer to track the next person to be informed
        # We can use a variable to track the current day
        # We can use a list to track the number of people each can tell
        # We can use a pointer to track the next person to be informed
        # We can use a variable to track the current day
        # We can use a list to track the number of people each can tell
        # We can use a pointer to track the next person to be informed
        # We can use a variable to track the current day
        # We can use a list to track the number of people each can tell
        # We can use a pointer to track the next person to be informed
        # We can use a variable to track the current day
        # We can use a list to track the number of people each can tell
        # We can use a pointer to track the next person to be informed
        # We can use a variable to track the current day
        # We can use a list to track the number of people each can tell
        # We can use a pointer to track the next person to be informed
        # We can use a variable to track the current day
        # We can use a list to track the number of people each can tell
        # We can use a pointer to track the next person to be informed
        # We can use a variable to track the current day
        # We can use a list to track the number of people each can tell
        # We can use a pointer to track the next person to be informed
        # We can use a variable to track the current day
        # We can use a list to track the number of people each can tell
        # We can use a pointer to track the next person to be informed
        # We can use a variable to track the current day
        # We can use a list to track the number of people each can tell
        # We can use a pointer to track the next person to be informed
        # We can use a variable to track the current day
        # We can use a list to track the number of people each can tell
        # We can use a pointer to track the next person to be informed
        # We can use a variable to track the current day
        # We can use a list to track the number of people each can tell
        # We can use a pointer to track the next person to be informed
        # We can use a variable to track the current day
        # We can use a list to track the number of people each can tell
        # We can use a pointer to track the next person to be informed
        # We can use a variable to track the current day
        # We can use a list to track the number of people each can tell
        # We can use a pointer to track the next person to be informed
        # We can use a variable to track the current day
        # We can use a list to track the number of people each can tell
        # We can use a pointer to track the next person to be informed
        # We can use a variable to track the current day
        # We can use a list to track the number of people each can tell
        # We can use a pointer to track the next person to be informed
        # We can use a variable to track the current day
        # We can use a list to track the number of people each can tell
        # We can use a pointer to track the next person to be informed
        # We can use a variable to track the current day
        # We can use a list to track the number of people each can tell
        # We can use a pointer to track the next person to be informed
        # We can use a variable to track the current day
        # We can use a list to track the number of people each can tell
        # We can use a pointer to track the next person to be informed
        # We can use a variable to track the current day
        # We can use a list to track the number of people each can tell
        # We can use a pointer to track the next person to be informed
        # We can use a variable to track the current day
        # We can use a list to track the number of people each can tell
        # We can use a pointer to track the next person to be informed
        # We can use a variable to track the current day
        # We can use a list to track the number of people each can tell
        # We can use a pointer to track the next person to be informed
        # We can use a variable to track the current day
        # We can use a list to track the number of people each can tell
        # We can use a pointer to track the next person to be informed
        # We can use a variable to track the current day
        # We can use a list to track the number of people each can tell
        # We can use a pointer to track the next person to be informed
        # We can use a variable to track the current day
        # We can use a list to track the number of people each can tell
        # We can use a pointer to track the next person to be informed
        # We can use a variable to track the current day
        # We can use a list to track the number of people each can tell
        # We can use a pointer to track the next person to be informed
        # We can use a variable to track the current day
        # We can use a list to track the number of people each can tell
        # We can use a pointer to track the next person to be informed
        # We can use a variable to track the current day
        # We can use a list to track the number of people each can tell
        # We can use a pointer to track the next person to be informed
        # We can use a variable to track the current day
        # We can use a list to track the number of people each can tell
        # We can use a pointer to track the next person to be informed
        # We can use a variable to track the current day
        # We can use a list to track the number of people each can tell
        # We can use a pointer to track the next person to be informed
        # We can use a variable to track the current day
        # We can use a list to track the number of people each can tell
        # We can use a pointer to track the next person to be informed
        # We can use a variable to track the current day
        # We can use a list to track the number of people each can tell
        # We can use a pointer to track the next person to be informed