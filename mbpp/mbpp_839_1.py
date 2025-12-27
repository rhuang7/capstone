def check(candidate):
    assert candidate([("Amana", 28), ("Zenat", 30), ("Abhishek", 29),("Nikhil", 21), ("B", "C")]) == [('Abhishek', 29), ('Amana', 28), ('B', 'C'), ('Nikhil', 21), ('Zenat', 30)]
    assert candidate([("aaaa", 28), ("aa", 30), ("bab", 29), ("bb", 21), ("csa", "C")]) == [('aa', 30), ('aaaa', 28), ('bab', 29), ('bb', 21), ('csa', 'C')]
    assert candidate([("Sarala", 28), ("Ayesha", 30), ("Suman", 29),("Sai", 21), ("G", "H")]) == [('Ayesha', 30), ('G', 'H'), ('Sai', 21), ('Sarala', 28), ('Suman', 29)]


def sort_tuples_by_first_item(tuples_list):
    return sorted(tuples_list, key=lambda x: x[0])

check(sort_tuples_by_first_item)