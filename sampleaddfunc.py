from fractions import Fraction

grading_records = {"Midterm": {}, "Final Term": {}}
rubric_multipliers = {}


def allocate_rubrics():
    """
    Stand-alone rubric allocation function that can be accessed separately.
    """
    global rubric_multipliers
    print(f"\n{'=' * 40}")
    print(f"       RUBRIC ALLOCATION")
    print(f"{'=' * 40}\n")

    rubric_multipliers = {}
    total_rubric = 0

    # Grading criteria with their respective grading types
    grading_criteria = {
        "QUIZ (Q)": ["quiz"],
        "PERFORMANCE TASK (PT)": ["seatworks", "participation", "attendance", "compilation"],
        "EXAM": ["exam"]
    }

    # Ask user for rubric allocation for each major grading criterion
    for criterion, grading_types in grading_criteria.items():
        while True:
            try:
                rubric = float(input(f"Enter the rubric for {criterion} (0-100): "))
                if rubric < 0 or rubric > 100 or total_rubric + rubric > 100:
                    print("Invalid input or exceeds 100%. Please try again.")
                    continue
                rubric_multipliers[criterion] = rubric
                total_rubric += rubric
                print(f"Current total rubric for all criteria: {total_rubric:.2f}%")
                break
            except ValueError:
                print("Invalid input. Please enter a valid number.")

        # If the criterion is PERFORMANCE TASK, ask for allocation for individual grading types
        if criterion == "PERFORMANCE TASK (PT)":
            pt_rubrics = {}
            pt_total = 0
            for grading_type in grading_types:
                while True:
                    try:
                        rubric = float(input(f"Enter the rubric for {grading_type.capitalize()} (0-100): "))
                        if rubric < 0 or pt_total + rubric > rubric_multipliers[criterion]:
                            print(f"Invalid input or exceeds {rubric_multipliers[criterion]}%. Please try again.")
                            continue
                        pt_rubrics[grading_type] = rubric
                        pt_total += rubric
                        print(f"Current total rubric for PERFORMANCE TASK: {pt_total:.2f}%")
                        break
                    except ValueError:
                        print("Invalid input. Please enter a valid number.")
            rubric_multipliers["PERFORMANCE TASK (PT)"] = pt_rubrics

        # For QUIZ and EXAM, set individual rubrics for their types
        elif criterion == "QUIZ (Q)":
            rubric_multipliers["quiz"] = rubric
        elif criterion == "EXAM":
            rubric_multipliers["exam"] = rubric

    print(f"\nRubric Allocation Review:")
    for criterion, multiplier in rubric_multipliers.items():
        if isinstance(multiplier, dict):
            print(f"  {criterion}:")
            for grading_type, rub in multiplier.items():
                print(f"    {grading_type.capitalize()}: {rub}%")
        else:
            print(f"  {criterion}: {multiplier}%")


def set_number_of_activities(term_name, grading_types):
    print(f"\n{'=' * 40}")
    print(f"       {term_name.upper()} NUMBER OF ACTIVITIES")
    print(f"{'=' * 40}\n")

    num_activities = {}
    for grading_type in grading_types:
        if grading_type in ["attendance", "compilation", "exam"]:
            num_activities[grading_type] = 1
            print(f"{grading_type.capitalize()}: Fixed at 1 activity.")
        else:
            while True:
                try:
                    activities = int(input(f"Enter the number of activities for {grading_type.capitalize()}: "))
                    if activities <= 0:
                        print("Please enter a positive integer.")
                        continue
                    num_activities[grading_type] = activities
                    break
                except ValueError:
                    print("Invalid input. Please enter a valid number.")
    return num_activities


def set_hps(term_name, num_activities):
    print(f"\n{'=' * 40}")
    print(f"       {term_name.upper()} HIGHEST POSSIBLE SCORES (HPS)")
    print(f"{'=' * 40}\n")

    hps_dict = {}
    for grading_type, activities in num_activities.items():
        hps_list = []
        for i in range(activities):
            while True:
                try:
                    hps = int(
                        input(f"Enter the highest possible score (HPS) for {grading_type.capitalize()} {i + 1}: "))
                    if hps <= 0:
                        print("Please enter a positive integer.")
                        continue
                    hps_list.append(hps)
                    break
                except ValueError:
                    print("Invalid input. Please enter a valid number.")
        hps_dict[grading_type] = hps_list
    return hps_dict


def input_raw_scores(term_name, num_activities, hps_dict, rubric_multipliers):
    print(f"\n{'=' * 40}")
    print(f"       {term_name.upper()} INPUT RAW SCORES")
    print(f"{'=' * 40}\n")

    scores_dict = {}
    total_final_scores = Fraction(0)

    for grading_type, hps_list in hps_dict.items():
        print(f"\nGrading Type: {grading_type.capitalize()}")
        raw_scores = []
        for i, hps in enumerate(hps_list):
            while True:
                try:
                    raw_score = int(input(f"Enter the raw score for {grading_type.capitalize()} {i + 1} (0-{hps}): "))
                    if raw_score < 0 or raw_score > hps:
                        print(f"Invalid input. Please enter a value between 0 and {hps}.")
                        continue
                    raw_scores.append(raw_score)
                    break
                except ValueError:
                    print("Invalid input. Please enter a valid number.")

        total_raw_score = sum(raw_scores)
        total_hps = sum(hps_list)

        # Access the correct rubric multiplier for each grading type
        if grading_type == "quiz":
            weighted_score = (total_raw_score / total_hps) * (rubric_multipliers["quiz"] / 100)
        elif grading_type == "exam":
            weighted_score = (total_raw_score / total_hps) * (rubric_multipliers["exam"] / 100)
        elif grading_type == "seatworks":
            weighted_score = (total_raw_score / total_hps) * (
                        rubric_multipliers["PERFORMANCE TASK (PT)"]["seatworks"] / 100)
        elif grading_type == "participation":
            weighted_score = (total_raw_score / total_hps) * (
                        rubric_multipliers["PERFORMANCE TASK (PT)"]["participation"] / 100)
        elif grading_type == "attendance":
            weighted_score = (total_raw_score / total_hps) * (
                        rubric_multipliers["PERFORMANCE TASK (PT)"]["attendance"] / 100)
        elif grading_type == "compilation":
            weighted_score = (total_raw_score / total_hps) * (
                        rubric_multipliers["PERFORMANCE TASK (PT)"]["compilation"] / 100)

        scores_dict[grading_type] = {
            "raw_scores": raw_scores,
            "total_raw_score": total_raw_score,
            "total_hps": total_hps,
            "weighted_score": weighted_score,
        }

        total_final_scores += Fraction(weighted_score)

    print(f"\n{term_name.upper()} Final Accumulated Grade: {total_final_scores * 100:.2f}%")
    grading_records[term_name]["Final Accumulated Grade"] = total_final_scores * 100
    grading_records[term_name]["Scores"] = scores_dict
    return total_final_scores


def compute_grades(term_name):
    grading_types = ["quiz", "seatworks", "attendance", "compilation", "exam"]

    num_activities = set_number_of_activities(term_name, grading_types)
    hps_dict = set_hps(term_name, num_activities)
    return input_raw_scores(term_name, num_activities, hps_dict, rubric_multipliers)


def main():
    print("Welcome to the Enhanced Grading System!")

    while True:
        print("\nChoose an option:")
        print("1. Allocate Rubrics")
        print("2. Compute Midterm Grade (MG)")
        print("3. Compute Final Term Grade (TFG)")
        print("4. View Grades")
        print("5. Calculate Semestral Grade")
        print("6. Exit")

        choice = input("\nEnter choice (1-6): ")

        if choice == "1":
            allocate_rubrics()
        elif choice == "2":
            compute_grades("Midterm")
        elif choice == "3":
            compute_grades("Final Term")
        elif choice == "4":
            term_name = input("Enter term name (Midterm/Final Term): ").strip()
            display_grades(term_name)
        elif choice == "5":
            calculate_semestral_grade()
        elif choice == "6":
            print("Exiting the program.")
            break
        else:
            print("Invalid option. Please choose a valid option (1-6).")


def display_grades(term_name):
    if term_name in grading_records:
        print(f"\n{term_name} Grading Details:")
        for grading_type, details in grading_records[term_name]["Scores"].items():
            print(f"\nGrading Type: {grading_type.capitalize()}")
            print(f"  Raw Scores: {details['raw_scores']}")
            print(f"  Total Raw Score: {details['total_raw_score']}")
            print(f"  Highest Possible Score (HPS): {details['total_hps']}")
            print(f"  Weighted Score: {details['weighted_score'] * 100:.2f}%")
    else:
        print(f"\nNo grades available for {term_name}.")


def calculate_semestral_grade():
    if "Midterm" not in grading_records or "Final Term" not in grading_records:
        print("\nError: Please compute both Midterm and Final Term grades first.")
    else:
        print("\nIs the student a freshman? (yes/no): ", end="")
        year_level = input().strip().lower()

        midterm_grade = grading_records["Midterm"]["Final Accumulated Grade"]
        final_term_grade = grading_records["Final Term"]["Final Accumulated Grade"]

        if year_level == "yes":
            # Freshman computation: (1/3 * MG + 2/3 * TFG)
            semestral_grade = (midterm_grade * 1 / 3) + (final_term_grade * 2 / 3)
        else:
            # Higher year computation: (MG * 0.5 + TFG * 0.5)
            semestral_grade = (midterm_grade * 0.5) + (final_term_grade * 0.5)

        print(f"\nSemestral Grade: {semestral_grade:.2f}%")

if __name__ == "__main__":
    main()
