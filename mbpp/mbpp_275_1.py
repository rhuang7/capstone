def check(candidate):
    assert candidate([2,5,4],3,2) == 2
    assert candidate([4,3],2,2) == 2
    assert candidate([1,2,3,4],4,1) == 4


def find_last_removed_position(arr):
    removed_positions = []
    for i in range(len(arr)):
        if i in removed_positions:
            continue
        # Simulate removal (for example, remove every second element)
        if i % 2 == 1:
            removed_positions.append(i)
    return removed_positions[-1] if removed_positions else -1

check(find_last_removed_position)