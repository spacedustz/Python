## Dictionary

Python의 DIctionary는 범용적으로 사용하는 데이터 포맷인 json과 유사한 구조입니다. `{key: Value}`

아래 코드와 주석으로 Dictionary의 설명을 대체합니다.

```python
# 빈 Dictionary 생성 : 2가지 방법
# 이미 값이 있을때 그 Dictionary의 값을 {}로 해줘도 빈 Dictionary로 만드는것과 동일함
empty_dic1 = {}
empty_dic2 = dict()

# 값이 있는 Dictionary 생성
program_dictionary = {
    "Bug": "Error", 
    "Function": "A piece of code that yo can easily call over and over again"
}

# 키 값 조회
program_dictionary["Bug"]

# 요소 추가 & 수정
# 이미 존재하는 키에 값을 할당해주면 값 수정이 됨
program_dictionary["Loop"] = "The action of doing something over and over again"

# Loop Dictionary
for a in program_dictionary:
    print(a) # Key만 출력
    print(program_dictionary[a]) # Value만 출력 
```

<br>

### Dictionary의 다양한 함수들

```python
# 딕셔너리 생성
student_info = {
    "name": "Alice",
    "age": 25,
    "courses": ["Math", "Science"]
}

# 1. keys(): 딕셔너리의 모든 키를 반환
keys = student_info.keys()
print(keys)  # 출력: dict_keys(['name', 'age', 'courses'])

# 2. values(): 딕셔너리의 모든 값을 반환
values = student_info.values()
print(values)  # 출력: dict_values(['Alice', 25, ['Math', 'Science']])

# 3. items(): 딕셔너리의 모든 키-값 쌍을 튜플 형태로 반환
items = student_info.items()
print(items)  # 출력: dict_items([('name', 'Alice'), ('age', 25), ('courses', ['Math', 'Science'])])

# 4. get(): 주어진 키에 대응하는 값을 반환, 키가 없을 경우 기본값 반환 (예시에서는 None)
age = student_info.get("age")
print(age)  # 출력: 25
grade = student_info.get("grade")
print(grade)  # 출력: None

# 5. setdefault(): 주어진 키가 있으면 해당 값을 반환, 없으면 키와 값을 추가하고 값을 반환
default_grade = student_info.setdefault("grade", "A")
print(default_grade)  # 출력: A
print(student_info)  # 출력: {'name': 'Alice', 'age': 25, 'courses': ['Math', 'Science'], 'grade': 'A'}

# 6. update(): 다른 딕셔너리 또는 키-값 쌍을 추가하여 업데이트
additional_info = {"city": "New York", "age": 26}  # 'age' 키의 값을 업데이트
student_info.update(additional_info)
print(student_info)  # 출력: {'name': 'Alice', 'age': 26, 'courses': ['Math', 'Science'], 'grade': 'A', 'city': 'New York'}

# 7. pop(): 주어진 키에 대응하는 값을 반환하고 해당 키-값 쌍을 삭제
city = student_info.pop("city")
print(city)  # 출력: New York
print(student_info)  # 출력: {'name': 'Alice', 'age': 26, 'courses': ['Math', 'Science'], 'grade': 'A'}

# 8. popitem(): 마지막 키-값 쌍을 반환하고 삭제 (파이썬 3.7+부터는 삽입 순서 보장)
last_item = student_info.popitem()
print(last_item)  # 출력: ('grade', 'A')
print(student_info)  # 출력: {'name': 'Alice', 'age': 26, 'courses': ['Math', 'Science']}

# 9. clear(): 딕셔너리의 모든 요소를 삭제
student_info.clear()
print(student_info)  # 출력: {}

# 10. fromkeys(): 주어진 키들로 새로운 딕셔너리를 생성하고 모든 값을 동일한 값으로 설정
keys = ["name", "age", "grade"]
default_value = "unknown"
new_dict = dict.fromkeys(keys, default_value)
print(new_dict)  # 출력: {'name': 'unknown', 'age': 'unknown', 'grade': 'unknown'}

```