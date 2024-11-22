from fractions import Fraction

grading_records = {"Midterm": {}, "Final Term": {}}

def allocate_rubrics(term_name):
    print(f"\n{'=' * 40}")
    print(f"       {term_name.upper()} RUBRIC ALLOCATION")
    print(f"{'=' * 40}\n")

    rubric_multipliers = {}
    grading_types = ["quiz", "seatworks", "attendance", "compilation", "exam"]
    total_multiplier = 0

    for grading_type in grading_types:
        while True:
            try:
                rubric_multiplier = float(input(f"Enter the rubric multiplier for {grading_type.capitalize()} (0-100): "))
                if rubric_multiplier < 0 or rubric_multiplier > 100 or total_multiplier + rubric_multiplier > 100:
                    print("Invalid input or exceeds 100%. Please try again.")
                    continue
                rubric_multipliers[grading_type] = rubric_multiplier
                total_multiplier += rubric_multiplier
                print(f"Current total rubric multiplier: {total_multiplier:.2f}%")
                break
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    print(f"\nRubric Allocation Review:")
    for grading_type, multiplier in rubric_multipliers.items():
        print(f"  {grading_type.capitalize()}: {multiplier}%")

    finalize = input("\nDo you want to finalize the rubric allocation? (yes/no): ").lower()
    if finalize != "yes":
        print("\nRubric allocation was not finalized. Re-entering...")
        return allocate_rubrics(term_name)

    return rubric_multipliers

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
                    hps = int(input(f"Enter the highest possible score (HPS) for {grading_type.capitalize()} {i+1}: "))
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
                    raw_score = int(input(f"Enter the raw score for {grading_type.capitalize()} {i+1} (0-{hps}): "))
                    if raw_score < 0 or raw_score > hps:
                        print(f"Invalid input. Please enter a value between 0 and {hps}.")
                        continue
                    raw_scores.append(raw_score)
                    break
                except ValueError:
                    print("Invalid input. Please enter a valid number.")

        total_raw_score = sum(raw_scores)
        total_hps = sum(hps_list)
        weighted_score = (total_raw_score / total_hps) * (rubric_multipliers[grading_type] / 100)

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
    grading_types = ["quiz", "seatworks", "attendance", "compilation", "exam", "lab reps"]

    rubric_multipliers = allocate_rubrics(term_name)
    num_activities = set_number_of_activities(term_name, grading_types)
    hps_dict = set_hps(term_name, num_activities)
    return input_raw_scores(term_name, num_activities, hps_dict, rubric_multipliers)

def main():
    print("Welcome to the Enhanced Grading System!")

    while True:
        print("\nChoose an option:")
        print("1. Compute Midterm Grade (MG)")
        print("2. Compute Final Term Grade (TFG)")
        print("3. View Grades")
        print("4. Calculate Semestral Grade")
        print("5. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            global MG
            MG = compute_grades("Midterm")
        elif choice == "2":
            global TFG
            TFG = compute_grades("Final Term")
        elif choice == "3":
            view_grades()
        elif choice == "4":
            if 'MG' not in globals() or 'TFG' not in globals():
                print("\nError: Please compute both MG and TFG before calculating the semestral grade.")
            else:
                print("\nSemestral Grade Calculation:")
                print(f"Midterm Final Accumulated Grade: {grading_records['Midterm']['Final Accumulated Grade']:.2f}%")
                print(f"Final Term Final Accumulated Grade: {grading_records['Final Term']['Final Accumulated Grade']:.2f}%")
                semestral_grade = (MG + TFG) / 2
                print(f"\nSemestral Grade: {semestral_grade * 100:.2f}%")
        elif choice == "5":
            print("\nExiting the grading system. Goodbye!")
            break
        else:
            print("\nInvalid choice. Please try again.")

def view_grades():
    print("\nView Grades:")
    print("1. Midterm Grades")
    print("2. Final Term Grades")
    print("3. Semestral Grade Record")
    choice = input("Choose an option: ")

    if choice == "1":
        display_grades("Midterm")
    elif choice == "2":
        display_grades("Final Term")
    elif choice == "3":
        if 'MG' not in globals() or 'TFG' not in globals():
            print("\nNo semestral grade computed yet.")
        else:
            print("\nSemestral Grade Record:")
            print(f"Midterm Final Accumulated Grade: {grading_records['Midterm']['Final Accumulated Grade']:.2f}%")
            print(f"Final Term Final Accumulated Grade: {grading_records['Final Term']['Final Accumulated Grade']:.2f}%")
            semestral_grade = (MG + TFG) / 2
            print(f"Semestral Grade: {semestral_grade * 100:.2f}%")
    else:
        print("\nInvalid choice. Returning to main menu.")

def display_grades(term_name):
    if term_name not in grading_records or "Scores" not in grading_records[term_name]:
        print(f"\nNo records found for {term_name}.")
        return

    print(f"\n{term_name.upper()} Grade Records:")
    for grading_type, data in grading_records[term_name]["Scores"].items():
        print(f"  {grading_type.capitalize()}:")
        if "raw_scores" in data:
            for i, raw_score in enumerate(data["raw_scores"]):
                print(f"    {grading_type.capitalize()} {i+1}: {raw_score}")
        print(f"    Total Raw Score: {data['total_raw_score']}/{data['total_hps']}")
        print(f"    Weighted Score: {data['weighted_score'] * 100:.2f}%")

    print(f"\nFinal Accumulated Grade: {grading_records[term_name]['Final Accumulated Grade']:.2f}%")

if __name__ == "__main__":
    main()
