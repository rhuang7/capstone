def check(candidate):
    assert candidate('Python language, Programming language.',2)==('Python:language: Programming language.')
    assert candidate('a b c,d e f',3)==('a:b:c:d e f')
    assert candidate('ram reshma,ram rahim',1)==('ram:reshma,ram rahim')


def replace_max_occurrences(text, n):
    import re
    pattern = r'[\s,.]'
    replacements = re.findall(pattern, text)
    if len(replacements) <= n:
        return re.sub(pattern, ':', text)
    else:
        replacement_count = 0
        result = []
        for char in text:
            if char in ' ,.' and replacement_count < n:
                result.append(':')
                replacement_count += 1
            else:
                result.append(char)
        return ''.join(result)

check(replace_max_occurrences)