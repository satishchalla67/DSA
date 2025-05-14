


def isValid(string):
    bracesMap = {"{": "}", "[":"]", "(":")"}
    openBraces = ("{", "[", "(")
    stack = []
    
    for s in string:
        if s in openBraces:
            stack.append(s)
        elif stack and s == bracesMap[stack[-1]]:
            stack.pop()
        else:
            return False
    return stack == []
            


string = "[{}][]}"
print(isValid(string))