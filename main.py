
import pandas as pd
import numpy as np


# Function to calculate student grade
def calculate_grade(average):
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"


# Function to identify performance category
def performance_category(average):
    if average >= 80:
        return "High"
    elif average >= 60:
        return "Average"
    else:
        return "Low"



def main():
    # Read student dataset
    students = pd.read_csv("students.csv")

    # Define subject columns
    subjects = ["Python", "Maths", "Statistics"]

    # Calculate total and average marks using Pandas and NumPy
    students["Total"] = students[subjects].sum(axis=1)
    students["Average"] = np.round(
        students[subjects].mean(axis=1), 2
    )

    # Assign grades
    students["Grade"] = students["Average"].apply(calculate_grade)

    # Pass if the student scores at least 40 in every subject
    students["Result"] = students[subjects].ge(40).all(axis=1).map(
        {True: "Pass", False: "Fail"}
    )

    # Categorize performance
    students["Performance"] = students["Average"].apply(
        performance_category
    )

    # Display individual student results
    print("=" * 75)
    print("          STUDENT PERFORMANCE ANALYTICS SYSTEM")
    print("=" * 75)

    print("\n1. STUDENT PERFORMANCE REPORT")
    print(
        students[
            [
                "Student_ID",
                "Name",
                "Department",
                "Total",
                "Average",
                "Grade",
                "Result",
                "Performance",
            ]
        ].to_string(index=False)
    )

    # Total number of students
    print("\n2. STUDENT SUMMARY")
    print("Total students:", len(students))
    print("Passed students:", (students["Result"] == "Pass").sum())
    print("Failed students:", (students["Result"] == "Fail").sum())

    # Class average
    class_average = np.round(students["Average"].mean(), 2)
    print("Class average:", class_average)

    # Subject-wise performance
    print("\n3. SUBJECT-WISE AVERAGE MARKS")
    for subject in subjects:
        subject_average = np.round(students[subject].mean(), 2)
        print(f"{subject}: {subject_average}")

    # Highest and lowest subject averages
    subject_averages = students[subjects].mean()
    print(
        "Best-performing subject:",
        subject_averages.idxmax(),
    )
    print(
        "Lowest-performing subject:",
        subject_averages.idxmin(),
    )

    # Top performers: students with the highest total marks
    print("\n4. TOP 3 STUDENTS")
    top_students = students.nlargest(3, "Total")
    print(
        top_students[
            ["Student_ID", "Name", "Total", "Average", "Grade"]
        ].to_string(index=False)
    )

    # Performance category counts
    print("\n5. PERFORMANCE CATEGORY SUMMARY")
    for category in ["High", "Average", "Low"]:
        count = (students["Performance"] == category).sum()
        print(f"{category} performers: {count}")

    # Save the analyzed report
    students.to_csv("student_performance_report.csv", index=False)
    print("\nReport saved as student_performance_report.csv")


if __name__ == "__main__":
    main()