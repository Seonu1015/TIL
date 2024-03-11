## sort()와 sorted()의 차이

### 원본 시퀀스 변경 여부

- sort(): 원본 리스트를 변경하여 정렬
- sorted(): 원본 시퀀스를 변경하지 않고 정렬된 새로운 리스트를 반환

  시퀀스(Sequence)란?  
   파이썬에서 여러 값들을 순서대로 나열한 자료 구조  
   리스트(list), 튜플(tuple), 문자열(string), range 등

```python
my_list = [3, 1, 4, 1, 5, 9, 2, 6, 5]

# sort() 메서드 사용
my_list.sort()
print(my_list)  # 출력: [1, 1, 2, 3, 4, 5, 5, 6, 9]

# sorted() 함수 사용
sorted_list = sorted(my_list)
print(sorted_list)  # 출력: [1, 1, 2, 3, 4, 5, 5, 6, 9]
print(my_list)  # 출력: [1, 1, 2, 3, 4, 5, 5, 6, 9] (원본 리스트는 변경되지 않음)
```

### 사용

- sort(): 리스트의 메서드로, 리스트 객체에 대해 직접 호출된다
- sorted(): 내장 함수로, 정렬하고자 하는 시퀀스를 인자로 전달한다

```python
my_list = [3, 1, 4, 1, 5, 9, 2, 6, 5]

# sort() 메서드 사용
my_list.sort(reverse=True)  # 내림차순으로 정렬
print(my_list)  # 출력: [9, 6, 5, 5, 4, 3, 2, 1, 1]

# sorted() 함수 사용
sorted_list = sorted(my_list, reverse=True)  # 내림차순으로 정렬된 새로운 리스트 반환
print(sorted_list)  # 출력: [9, 6, 5, 5, 4, 3, 2, 1, 1]
print(my_list)  # 출력: [9, 6, 5, 5, 4, 3, 2, 1, 1] (원본 리스트는 변경되지 않음)
```

### sorted()

#### 기본 사용법

```python
sorted(iterable, key=None, reverse=False)
```

- iterable: 정렬할 대상이 되는 시퀀스  
  리스트, 튜플, 문자열 등이 될 수 있습니다.

- key: 정렬 기준이 되는 함수를 지정  
  기본값은 None이며, 이 경우에는 요소의 기본 정렬 순서를 따릅니다.  
  예를 들어, key=len을 전달하면 문자열의 길이를 기준으로 정렬하게 됩니다.

- reverse: 정렬 순서를 반전할지 여부를 지정  
  기본값은 False이며, 오름차순으로 정렬  
  True를 전달하면 내림차순으로 정렬

```python
strings = ["apple", "banana", "cherry", "date"]

# key를 사용하지 않은 경우
sorted_without_key = sorted(strings)
print("Sorted without key:", sorted_without_key)  # 출력: ['apple', 'banana', 'cherry', 'date']

# key를 사용한 경우
sorted_with_key = sorted(strings, key=len)
print("Sorted with key:", sorted_with_key)  # 출력: ['date', 'apple', 'banana', 'cherry']
```

sorted_without_key는 문자열의 기본적인 사전식 순서로 정렬  
sorted_with_key에서는 key=len을 사용하여 문자열의 길이를 기준으로 정렬

```python
# 사전 생성
my_dict = {'banana': 3, 'apple': 2, 'cherry': 1}

# key를 사용하지 않은 경우 (사전은 키를 기준으로 정렬됨)
sorted_dict_without_key = sorted(my_dict)
print("Sorted dictionary without key:", sorted_dict_without_key)  # 출력: ['apple', 'banana', 'cherry']

# key를 사용한 경우 (값을 기준으로 정렬)
sorted_dict_with_key = sorted(my_dict, key=my_dict.get)
print("Sorted dictionary with key:", sorted_dict_with_key)  # 출력: ['cherry', 'apple', 'banana']
```

sorted_dict_without_key는 사전의 키를 기준(문자열의 기본적인 사전식 순서)으로 정렬  
sorted_dict_with_key에서는 key=my_dict.get을 사용하여 값(3, 2, 1)에 따라 정렬
