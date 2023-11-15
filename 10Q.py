"Valid Parentheses"

def isValidParentheses(s):
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in mapping:
            top_ele = stack.pop() if stack else '#'
            if mapping[char] != top_ele:
                return False
        else:
            stack.append(char)

    return not stack


expression = "{[(})]}"
result = isValidParentheses(expression)
print(result)  