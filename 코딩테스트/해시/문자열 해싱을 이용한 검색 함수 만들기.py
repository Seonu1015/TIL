# 문자열 해싱을 이용한 검색 함 수 만들기 ★★

# 문자열 리스트 string_list와 쿼리 리스트 query_list가 있을 때,
# 각 쿼리 리스트에 있는 문자열이 string_list의 문자열 리스트에 있는지 여부를 확인해야 한다
# 문자열이 있으면 True, 없으면 False를 반환

# string_list = ["apple", "banana", "cherry"]
# query_list = ["banana", "kiwi", "melon", "apple"]
# return → [True, False, False, True]

def solution(string_list, query_list):
    hash_list = {}

    for str in string_list:
        hash_value = hash(str)
        hash_list[hash_value] = True

    # hash_list = {hash(str): True for str in string_list} 딕셔너리 컴프리헨션을 사용해서 간단히 표현할 수 있음

    res = []

    for query in query_list:
        hash_value = hash(query)
        if hash_value in hash_list:
            res.append(True)
        else:
            res.append(False)

    return res

string_list = ["apple", "banana", "cherry"]
query_list = ["banana", "kiwi", "melon", "apple"]

print(solution(string_list, query_list))