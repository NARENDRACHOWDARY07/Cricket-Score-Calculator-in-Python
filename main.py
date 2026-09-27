"""
Cricket Score Calculator
A simple console-based Python project to calculate and display
the score of a cricket innings.
"""

def get_int(prompt, minimum=0):
    """Read a valid integer from the user."""
    while True:
        try:
            value = int(input(prompt))
            if value < minimum:
                print(f"Please enter a value greater than or equal to {minimum}.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a whole number.")


def main():
    print("=" * 50)
    print("       CRICKET SCORE CALCULATOR")
    print("=" * 50)

    team = input("Enter team name: ").strip()
    if not team:
        team = "Team"

    overs_limit = get_int("Enter number of overs: ", 1)
    total_runs = 0
    total_wickets = 0
    legal_balls = 0

    print("\nEnter ball-by-ball runs.")
    print("Use 0 for a dot ball and enter 1, 2, 3, 4, or 6 for runs.")
    print("For a wicket, enter 'W'.")
    print("For an extra (wide/no-ball), enter 'WD' or 'NB'.")

    max_balls = overs_limit * 6

    while legal_balls < max_balls and total_wickets < 10:
        ball_number = legal_balls + 1
        over = legal_balls // 6
        ball_in_over = legal_balls % 6 + 1

        entry = input(
            f"Over {over}.{ball_in_over} - Enter result: "
        ).strip().upper()

        if entry == "W":
            total_wickets += 1
            legal_balls += 1
            print("Wicket! Current score:", f"{total_runs}/{total_wickets}")
        elif entry in {"WD", "NB"}:
            total_runs += 1
            # Wide and no-ball do not count as legal balls.
            print("Extra run added. Current score:",
                  f"{total_runs}/{total_wickets}")
        else:
            try:
                runs = int(entry)
                if runs not in {0, 1, 2, 3, 4, 6}:
                    print("Please enter 0, 1, 2, 3, 4, 6, W, WD, or NB.")
                    continue
                total_runs += runs
                legal_balls += 1
                print("Current score:", f"{total_runs}/{total_wickets}")
            except ValueError:
                print("Invalid input. Please enter a valid ball result.")

    completed_overs = legal_balls // 6
    completed_balls = legal_balls % 6
    overs_display = f"{completed_overs}.{completed_balls}"

    print("\n" + "=" * 50)
    print("                 FINAL SCORE")
    print("=" * 50)
    print(f"Team       : {team}")
    print(f"Score      : {total_runs}/{total_wickets}")
    print(f"Overs      : {overs_display}")
    print(f"Run Rate   : {total_runs / (legal_balls / 6):.2f}"
          if legal_balls else "Run Rate   : 0.00")

    if total_wickets == 10:
        print("Status     : Innings ended - all wickets lost.")
    elif legal_balls == max_balls:
        print("Status     : Innings ended - over limit reached.")
    else:
        print("Status     : Innings completed.")

    print("=" * 50)


if __name__ == "__main__":
    main()
