from fractions import Fraction


def grading_system():
    # Define grading types for each category
    lecture_grading_types = ["quiz", "seatworks", "attendance", "compilation", "midterm exam"]
    laboratory_grading_types = ["laboratory reports", "midterm exam"]

    print("=" * 40)
    print("               GRADING SYSTEM                ")
    print("=" * 40)

    # Function to process each category
    def process_category(grading_types):
        category_scores_dict = {}
        total_rubric_multiplier = 0
        rubric_multipliers = []

        for grading_type in grading_types:
            print(f"\n--- {grading_type.capitalize()} ---")  # Section header for each grading type

            while True:
                try:
                    highest_score = float(input(f"Enter the highest possible score for {grading_type}: "))
                    if highest_score <= 0:
                        print("Please enter a positive number.")
                        continue
                    break
                except ValueError:
                    print("Invalid input. Please enter a numeric value.")

            scores = []
            total_score = Fraction(0)  # Initialize total score as a Fraction
            accumulated_highest = Fraction(0)  # Initialize accumulated highest score

            # Determine if the grading type requires a single score or multiple scores
            if grading_type in ["attendance", "compilation", "midterm exam"]:
                while True:
                    try:
                        user_score = float(
                            input(f"Enter your score for {grading_type} (must not exceed {highest_score}): "))
                        if user_score < 0:
                            print("Score cannot be negative. Please enter a valid score.")
                        elif user_score > highest_score:
                            print(f"Score cannot exceed the highest possible score of {highest_score}.")
                        else:
                            scores.append(Fraction(user_score))  # Store as a Fraction
                            total_score += Fraction(user_score)  # Accumulate the scores as a Fraction
                            accumulated_highest += Fraction(highest_score)  # Accumulate the highest possible score
                            break
                    except ValueError:
                        print("Invalid input. Please enter a numeric value.")
            else:
                while True:
                    try:
                        num_items = int(input(f"Enter the number of {grading_type} scores to input: "))
                        if num_items <= 0:
                            print("Please enter a positive number.")
                            continue
                        break
                    except ValueError:
                        print("Invalid input. Please enter a numeric value.")

                for i in range(num_items):
                    while True:
                        try:
                            user_score = float(input(
                                f"Enter your score for {grading_type} {i + 1} (must not exceed {highest_score}): "))
                            if user_score < 0:
                                print("Score cannot be negative. Please enter a valid score.")
                            elif user_score > highest_score:
                                print(f"Score cannot exceed the highest possible score of {highest_score}.")
                            else:
                                scores.append(Fraction(user_score))  # Store as a Fraction
                                total_score += Fraction(user_score)  # Accumulate the scores as a Fraction
                                accumulated_highest += Fraction(highest_score)  # Accumulate the highest possible score
                                break
                        except ValueError:
                            print("Invalid input. Please enter a numeric value.")

            category_scores_dict[grading_type] = {
                "scores": scores,
                "total_score": total_score,
                "accumulated_highest": accumulated_highest
            }

            # Get the rubric multiplier for this grading type
            while True:
                try:
                    rubric_multiplier = int(
                        input(f"Enter the rubric multiplier for {grading_type} (an integer value): "))
                    if rubric_multiplier <= 0:
                        print("Please enter a positive integer.")
                        continue
                    if total_rubric_multiplier + rubric_multiplier > 100:
                        print(
                            f"The total rubric multipliers cannot exceed 100. Current total: {total_rubric_multiplier}. Please enter a smaller value.")
                        continue
                    total_rubric_multiplier += rubric_multiplier  # Update total rubric multiplier
                    rubric_multipliers.append(rubric_multiplier)  # Store the rubric multiplier
                    break
                except ValueError:
                    print("Invalid input. Please enter an integer value.")

        # Check if the total rubric multipliers sum to 100
        if total_rubric_multiplier != 100:
            print(
                f"\nError: The total of all rubric multipliers must equal 100. Current total: {total_rubric_multiplier}.")
            return None

        # Calculate final scores for this category and accumulate them
        category_final_score = Fraction(0)

        for grading_type, data in category_scores_dict.items():
            total_score = data["total_score"]
            accumulated_highest = data["accumulated_highest"]
            rubric_multiplier = rubric_multipliers.pop(0)  # Get the corresponding rubric multiplier

            # Calculate the final score
            if accumulated_highest > 0:
                final_score = (total_score / accumulated_highest) * rubric_multiplier
            else:
                final_score = Fraction(0)

            # Ensure final score does not exceed 100
            final_score_float = min(float(final_score), 100.0)
            category_final_score += final_score_float

            # Print results for each grading type
            print(f"{grading_type.capitalize()}:")
            print(f"  Total Score: {total_score} out of {accumulated_highest}")
            print(f"  Final Score: {final_score_float:.2f}")
            print("-" * 40)

        # Return the final score for the category
        return float(category_final_score)

    # Process both categories
    print("\n--- Lecture Category ---")
    lecture_final_score = process_category(lecture_grading_types)

    print("\n--- Laboratory Category ---")
    laboratory_final_score = process_category(laboratory_grading_types)

    if lecture_final_score is None or laboratory_final_score is None:
        return  # Exit if there was an error in the categories

    # Calculate overall grade
    overall_grade = (lecture_final_score + laboratory_final_score) / 2

    # Print overall results
    print("=" * 40)
    print("                     OVERALL GRADE                     ")
    print("=" * 40)
    print(f"Lecture Final Score: {lecture_final_score:.2f}")
    print(f"Laboratory Final Score: {laboratory_final_score:.2f}")
    print(f"Overall Grade: {overall_grade:.2f}")
    print("=" * 40)


# Run the grading system
grading_system()
