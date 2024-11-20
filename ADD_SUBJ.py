# Function to format the course title with each word capitalized
def format_course_title(title):
    return title.title()


# Function to format the course code to uppercase
def format_course_code(code):
    return code.upper()


# Function to ensure the user inputs a valid positive integer within a specified range
def get_positive_integer(prompt, min_val=1, max_val=100):
    while True:
        try:
            value = int(input(prompt))  # Prompt for input and convert to integer
            if min_val <= value <= max_val:  # Validate the input is within the range
                return value
            else:
                print(f"Error: Value must be between {min_val} and {max_val}.")
        except ValueError:
            print("Error: Please enter a valid integer.")


# Function to ensure the total sum of rubric percentages equals 100
def get_rubric_percentages():
    rubrics = {'QUIZ': 0, 'PERFORMANCE TASK': 0, 'EXAMS': 0}
    total = 0

    while total != 100:
        print("\n--- Set Percentage Allocation for Each Rubric ---")
        print("The total of all rubrics must equal 100%.")
        total = 0
        for rubric in rubrics:
            rubrics[rubric] = get_positive_integer(f"{rubric} (%): ", min_val=1, max_val=100)
            total += rubrics[rubric]
        if total != 100:
            print("\nError: The total percentage must equal 100. Please try again.")

    return rubrics


# Function to ensure the sub-part percentages for Performance Task equal the given total
def get_performance_task_subparts_percentage(total_percentage):
    subparts = {'SEATWORKS': 0, 'ATTENDANCE': 0, 'COMPILATION': 0}
    total = 0

    while total != total_percentage:
        print(f"\n--- Set Percentages for Performance Task Sub-Parts ---")
        print(f"The total of all sub-parts must equal {total_percentage}%.")
        total = 0
        for subpart in subparts:
            subparts[subpart] = get_positive_integer(f"{subpart} (%): ", min_val=1, max_val=total_percentage)
            total += subparts[subpart]
        if total != total_percentage:
            print(f"\nError: The total percentage must equal {total_percentage}. Please try again.")

    return subparts


# Function to handle rubric-specific inputs
def get_rubric_details(performance_task_percentage):
    rubric_details = {}

    # QUIZ
    print("\n--- QUIZ RUBRIC ---")
    num_quizzes = get_positive_integer("Number of quiz activities: ", min_val=1)
    quiz_score = get_positive_integer("Highest possible score for each quiz: ")
    rubric_details['QUIZ'] = {'activities': num_quizzes, 'max_score': quiz_score}

    # PERFORMANCE TASK
    print("\n--- PERFORMANCE TASK RUBRIC ---")
    performance_task_details = {}

    # Set percentages for sub-parts
    subpart_percentages = get_performance_task_subparts_percentage(performance_task_percentage)

    # SEATWORKS
    print("\n[SEATWORKS]")
    num_seatworks = get_positive_integer("Number of seatwork activities: ", min_val=1)
    seatwork_score = get_positive_integer("Highest possible score for each seatwork: ")
    performance_task_details['SEATWORKS'] = {'activities': num_seatworks, 'max_score': seatwork_score,
                                             'percentage': subpart_percentages['SEATWORKS']}

    # ATTENDANCE
    print("\n[ATTENDANCE]")
    num_meetings = get_positive_integer("Total number of school days (meetings): ", min_val=1)
    performance_task_details['ATTENDANCE'] = {'meetings': num_meetings, 'percentage': subpart_percentages['ATTENDANCE']}

    # COMPILATION
    print("\n[COMPILATION]")
    compilation_score = get_positive_integer("Highest possible score for compilation: ")
    performance_task_details['COMPILATION'] = {'max_score': compilation_score,
                                               'percentage': subpart_percentages['COMPILATION']}

    rubric_details['PERFORMANCE TASK'] = performance_task_details

    # EXAMS
    print("\n--- EXAM RUBRIC ---")
    exam_score = get_positive_integer("Highest possible score for the exam: ")
    rubric_details['EXAMS'] = {'max_score': exam_score}

    return rubric_details


# Function to handle course content and units selection
def get_course_contents_and_units():
    while True:
        print("\n--- COURSE CONTENTS ---")
        content_type = input("Choose course contents (LEC, LAB, LEC&LAB): ").strip().upper()

        if content_type == "LEC":
            lec_units = get_positive_integer("Number of LEC units: ", min_val=1, max_val=4)
            lab_units = 0
            total_units = lec_units + lab_units
            return content_type, lec_units, lab_units, total_units
        elif content_type == "LAB":
            lab_units = get_positive_integer("Number of LAB units: ", min_val=1, max_val=4)
            lec_units = 0
            total_units = lec_units + lab_units
            return content_type, lec_units, lab_units, total_units
        elif content_type == "LEC&LAB":
            lec_units = get_positive_integer("Number of LEC units: ", min_val=1, max_val=4)
            lab_units = get_positive_integer("Number of LAB units: ", min_val=1, max_val=4)
            total_units = lec_units + lab_units
            return content_type, lec_units, lab_units, total_units
        else:
            print("Error: Invalid course content type. Please enter 'LEC', 'LAB', or 'LEC&LAB'.")


# Function to add courses to the list
def add_course(courses):
    while True:
        print("\n--- ADD COURSE FUNCTION ---")
        add_course = input("Add course? (Yes/No): ").strip().lower()

        if add_course == "no":
            break
        elif add_course != "yes":
            print("Invalid input. Please enter 'Yes' or 'No'.")
            continue

        # Begin course addition immediately after 'Yes'
        course = {}

        # Prompt for course title and code
        print("\n--- COURSE DETAILS ---")
        course_title = input("Course title: ").strip()
        course_code = input("Course code: ").strip()
        course['title'] = format_course_title(course_title)
        course['code'] = format_course_code(course_code)

        # Confirm course details before proceeding
        finalize_details = input(f"Finalize Course Details: {course['code']}_{course['title']}? (YES/NO): ").strip().lower()
        if finalize_details != "yes":
            print("Course details not finalized. Re-entering course details.\n")
            continue

        # Prompt for course contents (LEC, LAB, LEC&LAB) and units
        content_type, lec_units, lab_units, total_units = get_course_contents_and_units()
        course['content_type'] = content_type
        course['lec_units'] = lec_units
        course['lab_units'] = lab_units
        course['total_units'] = total_units

        # Confirm course contents before proceeding
        finalize_contents = input(f"Finalize Course Contents (LEC units: {lec_units}, LAB units: {lab_units}, Total units: {total_units})? (YES/NO): ").strip().lower()
        if finalize_contents != "yes":
            print("Course contents not finalized. Re-entering course contents.\n")
            continue

        # Prompt for course rubrics and details
        print("\n--- SET COURSE RUBRICS ---")
        rubrics = get_rubric_percentages()
        rubric_details = get_rubric_details(rubrics['PERFORMANCE TASK'])

        # Confirm rubric settings before proceeding
        finalize_rubrics = input("Finalize Rubrics? (YES/NO): ").strip().lower()
        if finalize_rubrics != "yes":
            print("Rubric details not finalized. Re-entering rubrics.\n")
            continue

        # Finalize the course addition
        course['rubrics'] = rubrics
        course['rubric_details'] = rubric_details

        print("\n--- Course Added Successfully ---")
        courses.append(course)
        print(f"Course Description: {course['code']}_{course['title']}")
        print(f"Course Contents: {course['content_type']}")
        print(f"Number of LEC Units: {course['lec_units']}")
        print(f"Number of LAB Units: {course['lab_units']}")
        print(f"Total no. of Units: {course['total_units']}")


# Function to view all courses that have been added
def view_courses(courses):
    if not courses:
        print("\nNo courses have been added yet.")
        return

    while True:
        print("\n--- Courses Added ---")
        for idx, course in enumerate(courses, start=1):
            print(f"{idx}. {course['code']}_{course['title']}")

        try:
            choice = input(
                "\nEnter the number of the course to view details, or type 'back' to return to the main menu: ").strip().lower()
            if choice == "back":
                break

            choice = int(choice)
            if 1 <= choice <= len(courses):
                selected_course = courses[choice - 1]
                print("\n--- Course Details ---")
                print(f"Course Description: {selected_course['code']}_{selected_course['title']}")
                print(f"Course Contents: {selected_course['content_type']}")
                print(f"Number of LEC Units: {selected_course['lec_units']}")
                print(f"Number of LAB Units: {selected_course['lab_units']}")
                print(f"Total no. of Units: {selected_course['total_units']}")
                print("Rubric Details:")
                for rubric, details in selected_course['rubric_details'].items():
                    print(f"- {rubric}: {details}")
            else:
                print("\nInvalid choice. Please select a valid course number.")
        except ValueError:
            print("\nInvalid input. Please enter a valid number.")


# Main function to drive the program
def main():
    courses = []  # List to store all added courses

    while True:
        print("\n--- MAIN MENU ---")
        print("1. Add Course")
        print("2. View Courses")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ").strip()

        if choice == "1":
            add_course(courses)
        elif choice == "2":
            view_courses(courses)
        elif choice == "3":
            print("\nExiting the program. Goodbye!")
            break
        else:
            print("\nInvalid choice. Please enter 1, 2, or 3.")


# Run the main function
if __name__ == '__main__':
    main()
