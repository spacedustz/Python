## 조건문

```python
if condition1:
    do A
elif condition2:
    do B
else:
    do C
```

---

## 반복문

**For Loop**

```python
for item in list:
    # Do Something
```

<br>

**For Loop with range()**

- 아래 예시에서 1~10 범위가 출력되는 것이 아닌, 1~9까지만 출력됨

```python
# 기본 range() 사용
for number in range(a, b):
    print(number)

# range에 step 주기
for number in range(1, 11, 3):
    print(number) # 1, 4, 7, 10
```

<br>

**While Loop**

```python
while condition:
    # Code
```

---

## 함수

**파라미터가 없는 함수**

```python
def fun():
    print("Hello")

fun()
```

<br>

**파라미터가 있는 함수**

```python
def fun(name):
    print(f"Hello {name}")

fun("abc")

# Keyword Argument
def fun(name):
    print(f"Hello {name}")

fun(name="abc")
```

---

## List

- 순서 존재

```python
words = ["A", "B", "C"]

# 리스트의 제일 마지막 요소를 선택할때 -1 지정 가능
lastIndex = words[-1] # C

# 리스트 요소 추가
words.append("D")
words.extend(["E", "F"])

# 중첩 리스트
listA = [1,2,3]
listB = [4,5,6]

listC = [listA, listB]
```