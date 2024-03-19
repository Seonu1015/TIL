# 할인 행사 ★

# XYZ 마트는 일정 금액을 지불하면 10일 동안 회원 자격을 부여한다.
# 마트는 회원을 대상으로 매일 1가지 제품을 할인하는 행사를 하고 있다.
# 할인 제품은 하루에 하나만 구매 가능
# 알뜰한 정현이는 자신이 원하는 제품과 수량이 할인하는 날짜와 10일 연속으로 일치할 때 맞춰서 회원가입을 하려고 한다

# 정현이가 원하는 제품을 나타내는 want 배열과
# 정현이가 원하는 제품의 수량을 나타내는 number 배열,
# 마트의 할인 제품을 나타내는 discount 배열이 있을 때
# 회원가입 시 정현이가 원하는 제품을 모두 할인 받을 수 있는 회원 등록 날짜의 총 일수를 반환하는 solution() 함수를 구현
# 가능한 날이 없다면 0을 return

def solution(want, number, discount):
    dic = {want[i]: number[i] for i in range(len(want))}

    answer = 0

    for i in range(len(discount) - 9):
        discount_10d = {}
        for j in range(i, i + 10):
            if discount[j] in dic:
                discount_10d[discount[j]] = discount_10d.get(discount[j], 0) + 1
        if discount_10d == dic:
            answer += 1
    return answer

want = ["banana", "apple", "rice", "pork", "pot"]
number = [3, 2, 2, 2, 1]
discount = ["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"]

print(solution(want, number, discount)) # 3

want = ["apple"]
number = [10]
discount = ["banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana"]

print(solution(want, number, discount)) # 0