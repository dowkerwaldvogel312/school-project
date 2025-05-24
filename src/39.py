class SimpleSchoolProject:
    def __init__(self):
        pass
    
    def display_menu(self):
        print("1. Add student")
        print("2. Display students")
        print("3. Exit")

    def add_student(self, name: str, age: int) -> None:
        # Implement adding a new student
        pass

    def display_students(self) -> list:
        # Implement displaying all the students
        return []

if __name__ == "__main__":
    school_project = SimpleSchoolProject()
    while True:
        choice = input("Enter your choice (1/2/3): ")
        if choice == "1":
            name = input("Enter student's name: ")
            age = int(input("Enter student's age: "))
            school_project.add_student(name, age)
        elif choice == "2":
            school_project.display_students()
        else:
            break
