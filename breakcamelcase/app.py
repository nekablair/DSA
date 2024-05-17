# taken from codewars 5-17-24
# PREP
# Parameter: string in camel case
# Return: string with space between camel case words
# Example: "camelCasing"  =>  "camel Casing" | ""   =>  ""
# Pseudocode:
# -iterate over string looking for first uppercase letter
# - once found, include space and then return first lowercase word, space, titlecase second word
# -may want to use a temporary list to push lowercase letters into
# -edge case if empty string, then return empty string

def solution(s):
    result = []
    for letter in s:
        if s == "":
            return s
        elif letter == letter.lower():
            result.append(letter)
        elif letter == letter.upper():
            result.append(" ")
            result.append(letter)
    result_str = "".join(result)
    return result_str

print(solution("helloWorld"))
print(solution(""))