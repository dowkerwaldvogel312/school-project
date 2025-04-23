class SimpleSchoolProject:
    def __init__(self):
        self.students = []

    def add_student(self, name: str, age: int) -> None:
        self.students.append({"name": name, "age": age})

    def find_student_by_name(self, name: str) -> Optional[dict]:
        for student in self.students:
            if student["name"] == name:
                return student
        return None

    def get_average_age(self) -> float:
        total_age = 0
        count = 0
        for student in self.students:
            total_age += student["age"]
            count += 1
        return total_age / count if count else 0.0

    def __str__(self) -> str:
        return f"SimpleSchoolProject: {len(self.students)} students, average age: {self.get_average_age():.2f}"
