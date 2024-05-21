## Nesting

Nesting은 데이터 구조 내에 또 다른 데이터 구조를 포함하는 개념을 의미합니다.

파이썬에서 특히 리스트와 딕셔너리를 중첩하여 사용함으로써 복잡한 데이터 구조를 만들 수 있습니다.

이러한 중첩 구조는 다차원 데이터나 계층적 데이터를 표현하는 데 매우 유용합니다.

<br>

**학생 정보와 수강 과목 & 성적을 관리하는 Nesting 예시**

```python
# 학생 정보를 담은 리스트 내에 딕셔너리를 중첩하여 사용
students = [
    {
        "name": "Alice",
        "age": 25,
        "courses": [
            {"name": "Math", "grade": "A"},
            {"name": "Science", "grade": "B"}
        ]
    },
    {
        "name": "Bob",
        "age": 23,
        "courses": [
            {"name": "Math", "grade": "B"},
            {"name": "English", "grade": "A"}
        ]
    },
    {
        "name": "Charlie",
        "age": 24,
        "courses": [
            {"name": "Science", "grade": "A"},
            {"name": "History", "grade": "B"}
        ]
    }
]

# 전체 학생 정보 출력
print("All Students Information:")
for student in students:
    print(student)

# 특정 학생의 정보에 접근
alice_courses = students[0]["courses"]
print("\nAlice's Courses and Grades:")
for course in alice_courses:
    print(f"{course['name']}: {course['grade']}")

# 새로운 학생 추가
new_student = {
    "name": "David",
    "age": 22,
    "courses": [
        {"name": "Math", "grade": "A"},
        {"name": "Art", "grade": "A"}
    ]
}
students.append(new_student)
print("\nUpdated Students Information:")
for student in students:
    print(student)

# 특정 과목에서 모든 학생의 성적을 출력
course_name = "Math"
print(f"\nGrades for the course {course_name}:")
for student in students:
    for course in student["courses"]:
        if course["name"] == course_name:
            print(f"{student['name']}: {course['grade']}")

# 딕셔너리 내에 리스트를 사용하여 각 과목의 평균 성적 계산
grades = {
    "Math": [],
    "Science": [],
    "English": [],
    "History": [],
    "Art": []
}

for student in students:
    for course in student["courses"]:
        grades[course["name"]].append(course["grade"])

# 성적을 숫자로 변환하는 함수
def grade_to_number(grade):
    return {
        "A": 4.0,
        "B": 3.0,
        "C": 2.0,
        "D": 1.0,
        "F": 0.0
    }.get(grade, 0.0)

# 각 과목의 평균 성적 계산
average_grades = {}
for subject, grades_list in grades.items():
    if grades_list:
        numerical_grades = [grade_to_number(grade) for grade in grades_list]
        average = sum(numerical_grades) / len(numerical_grades)
        average_grades[subject] = average

print("\nAverage Grades per Course:")
for subject, average in average_grades.items():
    print(f"{subject}: {average:.2f}")
```