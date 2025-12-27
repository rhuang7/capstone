def check(candidate):
    assert candidate(("Manjeet", "Nikhil", "Akshat"), (" Singh", " Meherwal", " Garg")) == ('Manjeet Singh', 'Nikhil Meherwal', 'Akshat Garg')
    assert candidate(("Shaik", "Ayesha", "Sanya"), (" Dawood", " Begum", " Singh")) == ('Shaik Dawood', 'Ayesha Begum', 'Sanya Singh')
    assert candidate(("Harpreet", "Priyanka", "Muskan"), ("Kour", " Agarwal", "Sethi")) == ('HarpreetKour', 'Priyanka Agarwal', 'MuskanSethi')


def concatenate_string_tuples(t1, t2):
    return tuple(s for s in t1 + t2)

check(concatenate_string_tuples)