def check(candidate):
    assert candidate([[], [], [], 'Red', 'Green', [1,2], 'Blue', [], []])==['Red', 'Green', [1, 2], 'Blue']
    assert candidate([[], [], [],[],[], 'Green', [1,2], 'Blue', [], []])==[ 'Green', [1, 2], 'Blue']
    assert candidate([[], [], [], 'Python',[],[], 'programming', 'language',[],[],[], [], []])==['Python', 'programming', 'language']


def remove_empty_lists(input_list):
    return [lst for lst in input_list if lst]

check(remove_empty_lists)