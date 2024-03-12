# 괄호 짝 맞추기★★

# 소괄호는 짝을 맞춘 열린 괄화 '(' 와 닫힌 괄호 ')'로 구성
# 열린 괄호와 닫힌 괄호가 무작위로 섞인 문자열이 주어졌을 때,
# 소괄호가 정상적으로 열고 닫혔는지 판별하는 solution() 함수를 구현

# 입출력 예
# s = "(())()" → True
# s = "((())()" → False

def solution(s):
    stack = []
    for i in s:
        if i == '(':
            stack.append(i)
        elif i == ')':
            if stack:
                stack.pop()
            else:
                return False
    return len(stack) == 0

print(solution("(())()"))
print(solution("((())()"))
print(solution("(())())"))