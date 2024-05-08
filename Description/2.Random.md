## Randomization

**정수 난수 생성**

- 2개의 파라미터(시작 숫자, 끝 숫자)를 받아 정수 형태의 난수를 생성함

```python
import random

n = random.randint(1, 10)
print(n)
```

<br>

**부동 소수점 난수 생성**

```python
import random

# 0 ~ 0.99999... 사이의 난수 생성
n = random.random()

# 0 ~ 5 사이의 부동 소수점 난수 생성 + 소수점 2자리 까지만 출력
print(round(random.random() * 5, 2))
```