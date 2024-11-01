from fractions import Fraction


def grading_system():
    # Define the grading types (including the new compilation type)
    grading_types = ["quiz", "seatworks", "attendance", "midterm exam", "compilation"]

    # Initialize a dictionary to store scores and highest possible scores
    scores_dict = {}
    total_final_scores = Fraction(0)  # Initialize total final scores as a Fraction

    print("=" * 40)
    print("               GRADING SYSTEM                ")
    print("=" * 40)

    # Total rubric multipliers tracking
    total_rubric_multiplier = 0
    rubric_multipliers = []

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

        # Determine if the grading type requires a single score or multiple scores
        if grading_type in ["attendance", "midterm exam", "compilation"]:
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
                        user_score = float(
                            input(f"Enter your score for {grading_type} {i + 1} (must not exceed {highest_score}): "))
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
                rubric_multiplier = int(input(f"Enter the rubric multiplier for {grading_type} (an integer value): "))
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
        print(f"\nError: The total of all rubric multipliers must equal 100. Current total: {total_rubric_multiplier}.")
        return

    # Calculate final scores for each grading type and accumulate them
    print("\n" + "=" * 40)
    print("                     FINAL SCORES                     ")
    print("=" * 40)

    for grading_type, data in scores_dict.items():
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

        # Print results for each grading type
        print(f"{grading_type.capitalize()}:")
        print(f"  Total Score: {total_score} out of {accumulated_highest}")
        print(f"  Final Score: {final_score_float:.2f}")
        print("-" * 40)

        # Accumulate the final score
        total_final_scores += final_score

    # Print the accumulated final scores
    total_final_scores_float = float(total_final_scores)
    print(f"Total Accumulated Final Scores: {total_final_scores_float:.2f}")
    print("=" * 40)


# Run the grading system
grading_system()
