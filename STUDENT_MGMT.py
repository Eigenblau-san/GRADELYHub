class Student:
    def __init__(self, given_name, middle_name, surname, year_of_enrollment, campus, urid):
        self.name = self.format_name(given_name, middle_name, surname)
        self.year_of_enrollment = year_of_enrollment
        self.campus = campus.upper()[:2]
        self.urid = urid
        self.student_id = self.generate_student_id()
        self.year_level = self.classify_year_level()

    def format_name(self, given_name, middle_name, surname):
        # Ensure proper formatting of names
        surname = surname.title()
        given_name = given_name.title()
        middle_initial = middle_name[0].upper() if middle_name else ""
        return f"{surname}, {given_name} {middle_initial}."

    def generate_student_id(self):
        return f"{str(self.year_of_enrollment)[-2:]}-{self.campus}-{self.urid}"

    def classify_year_level(self):
        current_year = 2024
        year_difference = current_year - self.year_of_enrollment

        if year_difference == 0:
            return "Freshman"
        elif year_difference == 1:
            return "Sophomore"
        elif year_difference == 2:
            return "Junior"
        elif year_difference == 3:
            return "Senior"
        else:
            return "Higher Year"

    def __repr__(self):
        return f"Name: {self.name}\nStudent ID: {self.student_id}\nYear Level: {self.year_level}\n"


def add_students(students):
    while True:
        add_student = input("Add student? (YES/NO): ").strip().lower()
        if add_student == "no":
            break
        elif add_student == "yes":
            print("\nEnter Student Details:")
            given_name = input("Given Name: ").strip()
            middle_name = input("Middle Name (leave blank if none): ").strip()
            surname = input("Surname: ").strip()

            try:
                year_of_enrollment = int(input("Year of Enrollment (2019-2024): ").strip())
                if year_of_enrollment < 2019 or year_of_enrollment > 2024:
                    raise ValueError("Invalid year of enrollment.")

                campus = input("Campus: ").strip()
                urid = input("URID: ").strip()
                finalize = input("Finalize? (YES/NO): ").strip().lower()

                if finalize == "yes":
                    student = Student(given_name, middle_name, surname, year_of_enrollment, campus, urid)
                    students.append(student)
                    print("\nSTUDENT INFO:")
                    print(student)
                    print("Student Added!\n")
                else:
                    print("Student entry canceled.\n")

            except ValueError as e:
                print(f"Error: {e}\n")
        else:
            print("Invalid input. Please type YES or NO.\n")


def view_students(students):
    if not students:
        print("\nNo students added yet.\n")
        return

    print("\nALL STUDENTS:\n")
    students.sort(key=lambda s: s.student_id)
    for student in students:
        print(f"Name: {student.name}, Student ID:({student.student_id})")


def main():
    students = []
    while True:
        print("\nOptions:")
        print("1. Add Students")
        print("2. View Students")
        print("3. Exit")
        choice = input("Choose an option (1/2/3): ").strip()

        if choice == "1":
            add_students(students)
        elif choice == "2":
            view_students(students)
        elif choice == "3":
            print("Exiting the program.")
            break
        else:
            print("Invalaid choice. Please choose 1, 2, or 3.\n")


if __name__ == "__main__":
    main()
