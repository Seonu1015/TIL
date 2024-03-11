# 배열 정렬하기 ★

# 정수 배열을 정렬해서 반환하는 solution() 함수를 완성하세요.

# 제약조건
# - 정수 배열의 길이는 2 이상 100,000 이하 입니다.
# - 정수 배열의 각 데이터 값은 -100,000 이상 100,000 이하 입니다.

# [1, -5, 2, 4, 3] → [-5, 1, 2, 3, 4]
# [2, 1, 1, 3, 2, 5, 4] → [1, 1, 2, 2, 3, 4, 5]
# [6, 1, 7] → [1, 6, 7]

def solution(arr):
    arr.sort()
    return arr

numbers = [1, -5, 2, 4, 3]

print(solution(numbers))


# sort() 메서드를 사용하지 않고 O(N²) 정렬 알고리즘을 사용한다면?

import time

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def do_sort(arr):
    arr.sort()
    return arr

def measure_time(func, arr):
    start_time = time.time()
    result = func(arr)
    end_time = time.time()
    return end_time - start_time, result

arr = list(range(10000))
bubble_time, bubble_sort = measure_time(bubble_sort, arr)
print("bubble_sort 실행 시간 : ", format(bubble_time, ".10f"))

arr = list(range(10000))
do_time, do_sort = measure_time(do_sort, arr)
print("do_sort 실행 시간 : ", format(do_time, ".10f"))

# 첫 번째 방법은 O(N²) 정렬 알고리즘인 버블 정렬을 사용
# 두 번째 방법은 O(NlogN) 시간 복잡도의 sort() 함수를 사용

# 실행환경마다 차이는 있지만 버블 정렬은 2초가 걸렸고, sort()는 1초도 걸리지 않았다.
# sort() 함수가 성능이 더 좋다.