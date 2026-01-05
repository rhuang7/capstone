import sys

def solve():
    import sys
    input = sys.stdin.buffer.read().split(b'\n')
    idx = 0
    T = int(input[idx])
    idx += 1
    for _ in range(T):
        N = int(input[idx])
        idx += 1
        votes = []
        for _ in range(N):
            parts = input[idx].split()
            idx += 1
            votes.append(parts)
        score = 0
        user_votes = {}
        for user, vote in votes:
            if user in user_votes:
                # Nullify previous vote
                prev_vote = user_votes[user]
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
            user_votes[user] = vote
        print(score)

if __name__ == '__main__':
    solve()