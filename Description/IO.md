## Python 입출력

> **입력 받기 / 출력 하기**

- 사용자 입력은 input()으로 받을 수 있습니다.
- 출력은 print()를 사용하며, ","로 파라미터를 구분해주면 자동으로 1칸 띄어쓰기가 되지만,
- sep으로 띄어쓰기 개수를 조절 할 수 있습니다.

```python
rad = int(input("반지름 값 입력"))
hei = int(input("높이 값 입력"))

print("부피의 값은", 1 / 3 * 3.14 * rad ** 2 * hei, "입니다.", sep="")
```