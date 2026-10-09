
# Student Performance Analytics System

## Project Overview
The Student Performance Analytics System is a Python project that analyzes student marks and generates a performance report.

## Technologies Used
- Python
- NumPy
- Pandas
- CSV dataset
- Visual Studio Code

## Dataset
The dataset contains 20 student records with the following details:
- Student ID
- Name
- Department
- Python marks
- Maths marks
- Statistics marks
- Attendance

## Key Features
- Calculates total marks and average marks.
- Assigns grades based on average marks.
- Identifies pass and fail status.
- Categorizes student performance as High, Average, or Low.
- Calculates subject-wise average marks.
- Identifies the best-performing and lowest-performing subjects.
- Displays the top three students.
- Generates a CSV performance report.

## How to Run
1. Install Python.
2. Install the required libraries:
   `python -m pip install numpy pandas`
3. Place `main.py` and `students.csv` in the same folder.
4. Run:
   `python main.py`

## Output
The program displays student performance, class summary, subject-wise analysis, top performers, and performance categories.

It also generates `student_performance_report.csv`.

## Grading and Pass/Fail Rules
- Grade A: Average >= 90
- Grade B: Average >= 80
- Grade C: Average >= 70
- Grade D: Average >= 60
- Grade F: Average < 60
- Pass: At least 40 marks in every subject
- Performance categories: High (average >= 80), Average (average >= 60 and < 80), Low (average < 60)

## Final Outcome
The project demonstrates Python fundamentals, functions, loops, NumPy calculations, Pandas data analysis, and CSV file handling.