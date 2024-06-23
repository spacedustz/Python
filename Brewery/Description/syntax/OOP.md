## OOP

객체지향의 기본 개념에 대해서는 대부분 알고 있기 때문에 파이썬에서만 존재하는 개념에 대한 설명만 적습니다.

- `self` : Java의 `this` 키워드 같은 역할로 인스턴스 자기 자신을 의미함
- `__init`, `__str__` : init은 Java의 Constructor의 역할 / str은 Java의 toString같은 역할

<br>

> **__init__ 과 __str__에 대한 추가 설명**

__init__과 __str__ 같은 메서드는 특별한 목적을 가진 매직 메서드(Magic Methods) 또는 **덴더 메서드(Dunder Methods)** 라고 불립니다.

이 메서드들은 이름에 이중 밑줄(__)이 앞뒤로 붙어 있는 이유는 다음과 같습니다.

<br>

**특별한 역할**: 매직 메서드는 파이썬 언어의 특정 동작을 정의하거나 수정하는 데 사용됩니다. 
- 예를 들어, __init__은 객체가 생성될 때 자동으로 호출되는 생성자 메서드이고, __str__은 객체를 문자열로 표현할 때 호출되는 메서드입니다.

<br>

**이름 충돌 방지**: 이중 밑줄(__)을 사용하면 사용자 정의 메서드나 속성과 이름이 충돌하지 않도록 방지할 수 있습니다. 
- 즉, 클래스 내부에서 일반적인 메서드나 속성 이름과 구분되도록 설계되었습니다.

<br>

**언어적 규칙**: 파이썬은 이러한 메서드의 이름을 이중 밑줄로 규정하여, 파이썬 인터프리터가 이 메서드들을 특정 상황에서 자동으로 호출하도록 합니다. 
- 이는 파이썬의 내부 동작을 사용자 정의할 수 있도록 합니다.

<br>

```python
class Student:
    # 학생을 나타내는 클래스
    def __init__(self, name, age):
        # 생성자로, 학생의 이름과 나이를 초기화
        self.name = name
        self.age = age
        self.courses = []

    def add_course(self, course_name, grade):
        # 과목과 성적을 추가합니다.
        self.courses.append({"name": course_name, "grade": grade})

    def get_average_grade(self):
        # 학생의 평균 성적을 계산하여 반환
        def grade_to_number(grade):
            # 문자 성적을 숫자 성적으로 변환
            return {
                "A": 4.0,
                "B": 3.0,
                "C": 2.0,
                "D": 1.0,
                "F": 0.0
            }.get(grade, 0.0)

        if not self.courses:
            return 0.0

        total = sum(grade_to_number(course["grade"]) for course in self.courses)
        return total / len(self.courses)

    def __str__(self):
        # 학생의 문자열 표현을 반환
        return f"Student(name={self.name}, age={self.age}, courses={self.courses})"


class GraduateStudent(Student):
    # 대학원생을 나타내는 클래스, Student 클래스를 상속받음
    def __init__(self, name, age, thesis_title):
        # 생성자 메서드로, 부모 클래스의 속성을 초기화하고 논문 제목을 추가로 초기화
        super().__init__(name, age)
        self.thesis_title = thesis_title

    def __str__(self):
        # 대학원생의 문자열 표현을 반환
        return f"GraduateStudent(name={self.name}, age={self.age}, courses={self.courses}, thesis_title={self.thesis_title})"


# 메인 코드 예제

# Student 객체 생성
alice = Student("Alice", 25)
alice.add_course("Math", "A")
alice.add_course("Science", "B")
print(alice)
print(f"Alice's Average Grade: {alice.get_average_grade():.2f}")

# GraduateStudent 객체 생성
bob = GraduateStudent("Bob", 23, "Quantum Computing")
bob.add_course("Math", "B")
bob.add_course("English", "A")
print(bob)
print(f"Bob's Average Grade: {bob.get_average_grade():.2f}")

```