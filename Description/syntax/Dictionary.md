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
