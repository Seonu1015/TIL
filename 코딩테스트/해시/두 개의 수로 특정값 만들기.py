# 두 개의 수로 특정값 만들기 ★

# n개의 양의 정수로 이루어진 리스트 arr와 정수 target이 주어졌을 때
# 이 중에서 합이 target인 두 수가 arr에 있는지 찾고,
# 있으면 True, 없으면 False를 반환

# arr = [1, 2, 3, 4, 8] target = 6 → True
# arr = [2, 3, 5, 9] target = 10 → False

def solution(arr, target):
    hashtable = {}

    for num in arr:
        if num <= target:
            hashtable[num] = True

    for num in arr:
        complement = target - num
        if complement in hashtable and (complement != num):
            return True
        
    return False

print(solution([1, 2, 3, 4, 8], 6))
print(solution([2, 3, 5, 9], 10))

print("=======================================")

# 불필요한 반복을 줄여서 다시 수정

# complement를 계산하고 나서 해당 complement가 해시테이블에 있는지 확인합니다.
# 만약 있다면, 두 수의 합이 target이 되는 것이므로 True를 반환합니다.
# 그렇지 않은 경우에는 현재의 num을 해시테이블에 추가해야 합니다.

# 그렇지 않으면 이후의 반복에서 이 num을 만나게 될 때, target - num이 항상 해시테이블에 있게 되어 두 번째로 같은 수를 선택하게 됩니다.
# 따라서, 현재의 num을 해시테이블에 추가하는 코드는 complement의 존재 여부를 확인하는 코드 이후에 위치해야 합니다.

def solution(arr, target):
    hashtable = {}

    for num in arr:
        complement = target - num
        if complement in hashtable and complement != num:
            return True
        hashtable[num] = True

    return False

print(solution([1, 2, 3, 4, 8], 6))
print(solution([2, 3, 5, 9], 10))