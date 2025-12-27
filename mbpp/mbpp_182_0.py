def check(candidate):
    assert candidate("ThisIsGeeksforGeeks") == (['T', 'I', 'G', 'G'], ['h', 'i', 's', 's', 'e', 'e', 'k', 's', 'f', 'o', 'r', 'e', 'e', 'k', 's'], [], [])
    assert candidate("Hithere2") == (['H'], ['i', 't', 'h', 'e', 'r', 'e'], ['2'], [])
    assert candidate("HeyFolks32") == (['H', 'F'], ['e', 'y', 'o', 'l', 'k', 's'], ['3', '2'], [])


import re

def analyze_characters(s):
    uppercase = re.findall(r'[A-Z]', s)
    lowercase = re.findall(r'[a-z]', s)
    special = re.findall(r'[^A-Za-z0-9]', s)
    numeric = re.findall(r'[0-9]', s)
    return {
        'uppercase': uppercase,
        'lowercase': lowercase,
        'special': special,
        'numeric': numeric
    }

check(analyze_characters)