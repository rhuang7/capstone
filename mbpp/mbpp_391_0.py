def check(candidate):
    assert candidate(["S001", "S002", "S003", "S004"],["Adina Park", "Leyton Marsh", "Duncan Boyle", "Saim Richards"] ,[85, 98, 89, 92])==[{'S001': {'Adina Park': 85}}, {'S002': {'Leyton Marsh': 98}}, {'S003': {'Duncan Boyle': 89}}, {'S004': {'Saim Richards': 92}}]
    assert candidate(["abc","def","ghi","jkl"],["python","program","language","programs"],[100,200,300,400])==[{'abc':{'python':100}},{'def':{'program':200}},{'ghi':{'language':300}},{'jkl':{'programs':400}}]
    assert candidate(["A1","A2","A3","A4"],["java","C","C++","DBMS"],[10,20,30,40])==[{'A1':{'java':10}},{'A2':{'C':20}},{'A3':{'C++':30}},{'A4':{'DBMS':40}}]


def lists_to_nested_dict(lists):
    if not lists:
        return {}
    keys = lists[0]
    nested_dict = {}
    for i in range(len(keys)):
        key = keys[i]
        nested_dict[key] = [lst[i] for lst in lists]
    return nested_dict

check(lists_to_nested_dict)