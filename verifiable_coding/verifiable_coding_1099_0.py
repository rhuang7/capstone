import sys

def solve():
    import sys
    input = sys.stdin.buffer.read().splitlines()
    idx = 0
    T = int(input[idx])
    idx += 1
    for _ in range(T):
        N = int(input[idx])
        idx += 1
        votes = {}
        score = 0
        for _ in range(N):
            parts = input[idx].split()
            idx += 1
            user = parts[0]
            vote = parts[1]
            if user in votes:
                # Nullify previous vote
                prev_vote = votes[user]
                if prev_vote == '+':
                    score -= 1
                else:
                    score += 1
                # Update with current vote
                if vote == '+':
                    score += 1
                else:
                    score -= 1
            else:
                # Add current vote
                if vote == '+':
                    score += 1
                else:
                    score -= 1
            votes[user] = vote
        print(score)

if __name__ == '__main__':
    solve()