# 괄호 회전하기 ★

# 다음 규칙을 지키는 문자열을 올바른 괄호 문자열이라고 정의한다
# - "()", "[]", "{}"는 모두 올바를 괄호 문자열이다.
# - 만약 A가 올바른 괄호 문자열이라면, "(A)", "[A]", "{A}"도 올바른 괄호 문자열이다
#     "[]"가 올바른 괄호 문자열이므로, "([])"도 올바른 괄호 문자열이다
# - 만약 A, B가 올바른 문자열이면, AB도 올바른 문자열이다
#     "{}"와 "([])"가 올바른 괄호 문자열이므로, "{}([])"도 올바른 괄호 문자열이다

# 대괄호, 중괄호, 소괄호로 이루어진 문자열 s
# 이 s를 왼쪽으로 x( 0 <= x <= s의 길이) 칸만큼 회전시켰을 때 s가 올바른 괄호 문자열이 되게 하는 x의 개수를 반환하는 solution() 구현

# s = "[](){}" → 3
# s = "}]()[{" → 2
# s = "[)(]" → 0
# s = "}}}" → 0

# 왼쪽으로 한칸씩 이동 - "[](){}" > "](){}[" > "(){}[]" > "){}[](" > "{}[]()" > "}[](){"
#                           o           x       o           x           o           x

def solution(s):
    count = 0
    for i in range(len(s)):
        rotated_s = s[i:] + s[:i]
        if bracket(rotated_s):
            count += 1
    return count

def bracket(s):
    stack = []
    for c in s:
        if c == "(" or c == "[" or c == "{":
            stack.append(c)
        else:
            if not stack:
                return False
            if c == ")" and stack[-1] == "(":
                stack.pop()
            elif c == "]" and stack[-1] == "[":
                stack.pop()
            elif c == "}" and stack[-1] == "{":
                stack.pop()
    return len(stack) == 0

print(solution("[](){}"))
print(solution("}]()[{"))
print(solution("[)(]"))
print(solution("}}}"))


# print(bracket("[](){}"))
# print(bracket("](){}["))
# print(bracket("(){}[]"))
# print(bracket("){}[]("))
# print(bracket("{}[]()"))
# print(bracket("}[](){"))