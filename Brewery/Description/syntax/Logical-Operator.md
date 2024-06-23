## 논리연산

- AND 연산 = `and`
- OR 연산 = `or`
- NOT 연산 = `not`

<br>

**and 예시**

```python
A = 10
B = 99

# True and True
print("1. True and True")
if A == 10 and B == 99:
    print("A == 10 and B == 99 : True")
else:
    print("A == 10 and B == 99 : False")

# True and False
print("\n2. True and False")
if A == 10 and B != 99:
    print("A == 10 and B != 99 : True")
else:
    print("A == 10 and B != 99 : False")

# False and True
print("\n3. False and True")
if A != 10 and B == 99:
    print("A != 10 and B == 99 : True")
else:
    print("A != 10 and B == 99 : False")

# False and False
print("\n4. False and False")
if A != 10 and B != 99:
    print("A != 10 and B != 99 : True")
else:
    print("A != 10 and B != 99 : False")
```

<br>

**or 예시**

```python
A = 10
B = 99

# True or True
print("1. True or True")
if A == 10 or B == 99:
    print("A == 10 or B == 99 : True")
else:
    print("A == 10 or B == 99 : False")

# True or False
print("\n2. True or False")
if A == 10 or B != 99:
    print("A == 10 or B != 99 : True")
else:
    print("A == 10 or B != 99 : False")

# False or True
print("\n3. False or True")
if A != 10 or B == 99:
    print("A != 10 or B == 99 : True")
else:
    print("A != 10 or B == 99 : False")

# False or False
print("\n4. False or False")
if A != 10 or B != 99:
    print("A != 10 or B != 99 : True")
else:
    print("A != 10 or B != 99 : False")
```

<br>

**not 예시**

```python
name = "BlockDMask"

# not True
print("1. not True")
if not name == "BlockDMask":
    print("not name == 'BlockDMask' : True")
else:
    print("not name == 'BlockDMask' : False")

# not False
print("\n2. not False")
if not name == "ABCDEF":
    print("not name == 'ABCDEF' : True")
else:
    print("not name == 'ABCDEF' : False")
```