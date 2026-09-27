# Cricket Score Calculator in Python

## 1. Project Title
**Cricket Score Calculator**

## 2. Introduction
Cricket Score Calculator is a simple console-based Python application that
calculates the score of a cricket innings. The user enters the result of each
ball, and the program updates the total runs, wickets, overs, and run rate.

This project is designed for beginners to demonstrate Python programming
concepts such as variables, loops, conditional statements, functions,
input validation, and formatted output.

## 3. Features
- Accepts team name and number of overs.
- Records runs ball by ball.
- Supports 0, 1, 2, 3, 4, and 6 runs.
- Supports wickets.
- Supports basic wides and no-balls.
- Automatically calculates completed overs.
- Calculates the current/final score.
- Calculates run rate.
- Ends the innings when the selected over limit is reached or 10 wickets fall.
- Handles invalid user input.

## 4. Requirements
- Python 3.x
- No external Python packages are required.

## 5. How to Run

Open a terminal/command prompt in the project folder and run:

```bash
python main.py
```

On some systems, use:

```bash
python3 main.py
```

## 6. Example

```text
==================================================
       CRICKET SCORE CALCULATOR
==================================================
Enter team name: India
Enter number of overs: 2

Enter ball-by-ball runs.
Use 0 for a dot ball and enter 1, 2, 3, 4, or 6 for runs.
For a wicket, enter 'W'.
For an extra (wide/no-ball), enter 'WD' or 'NB'.

Over 0.1 - Enter result: 1
Current score: 1/0
Over 0.2 - Enter result: 4
Current score: 5/0
...
```

## 7. Project Structure

```text
cricket_score_calculator/
│
├── main.py
├── README.md
├── project_statement.txt
└── report_description.txt
```

## 8. Concepts Used
- Python functions
- Variables and data types
- `while` loops
- `if-elif-else` statements
- Exception handling using `try-except`
- User input
- String formatting
- Basic arithmetic calculations

## 9. Limitations
This is an educational project and does not implement every official cricket
scoring rule. For example, it treats a wide and a no-ball as one extra run and
does not separately record batter runs, bowler statistics, byes, leg-byes,
free hits, or penalty runs.

## 10. Future Improvements
The project can be extended to include:
- Batter-wise statistics
- Bowler-wise statistics
- Boundaries count
- Strike rotation
- Extras breakdown
- Two-team match mode
- Target and required run rate
- Graphical user interface
- Saving scorecards to a file or database

## 11. Author
Student Project - Python Programming
## 12.Details
Student Name: J. Narendra Chowdary

Regestration No: 26BAI10259
