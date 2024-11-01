from fractions import Fraction


def grading_system():
    # Define the grading types (excluding laboratory reports)
    grading_types = ["quiz", "seatworks", "attendance", "midterm exam"]

    # Initialize a dictionary to store scores and highest possible scores
    scores_dict = {}
    total_final_scores = Fraction(0)  # Initialize total final scores as a Fraction

    print("=" * 40)
    print("               GRADING SYSTEM                ")
    print("=" * 40)

    # Get user input for each grading type
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

        # Get scores for each item in the grading type
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
                    user_score = float(
                        input(f"Enter {grading_type} {i + 1} grade: "))
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

        scores_dict[grading_type] = {
            "scores": scores,
            "total_score": total_score,
            "accumulated_highest": accumulated_highest
        }

        # Get the rubric multiplier for this grading type
        while True:
            try:
                rubric_multiplier = int(input(f"Rubrics Percentage for {grading_type}: "))
                if rubric_multiplier <= 0:
                    print("Please enter a positive integer.")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter an integer value.")

        scores_dict[grading_type]["rubric_multiplier"] = rubric_multiplier

    # Calculate final scores for each grading type and accumulate them
    print("\n" + "=" * 40)
    print("                     FINAL SCORES                     ")
    print("=" * 40)

    for grading_type, data in scores_dict.items():
        total_score = data["total_score"]
        accumulated_highest = data["accumulated_highest"]
        rubric_multiplier = data["rubric_multiplier"]

        # Calculate the final score
        if accumulated_highest > 0:
            final_score = (total_score / accumulated_highest) * rubric_multiplier
        else:
            final_score = Fraction(0)

        # Convert final score to float
        final_score_float = float(final_score)

        # Print results for each grading type
        print(f"{grading_type.capitalize()}:")
        print(f"  Total Score: {total_score} out of {accumulated_highest}")
        print(f"  Final Score: {final_score_float:.2f}")
        print("-" * 40)

        # Accumulate the final score
        total_final_scores += final_score

    # Print the accumulated final scores
    total_final_scores_float = float(total_final_scores)
    print(f"Lecture Grade: {total_final_scores_float:.2f}")
    print("=" * 40)


# Run the grading system
grading_system()
