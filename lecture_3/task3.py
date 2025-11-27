def main():
    students = []
    
    while True:
        print("\n--- Student Grade Analyzer ---")
        print("1. Add a new student")
        print("2. Add grades for a student")
        print("3. Show report all students")
        print("4. Find top performer")
        print("5. Exit")
        
        try:
            choice = input("Enter your choice: ").strip()
            
            if choice == "1":
                add_new_student(students)
            elif choice == "2":
                add_grades_for_student(students)
            elif choice == "3":
                show_report(students)
            elif choice == "4":
                find_top_performer(students)
            elif choice == "5":
                print("Exiting program.")
                break
            else:
                print("Invalid choice. Please enter a number between 1-5.")
                
        except KeyboardInterrupt:
            print("\n\nProgram interrupted by user. Exiting gracefully.")
            break
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

def add_new_student(students):
    """Option 1: Add a new student"""
    name = input("Enter student name: ").strip()
    
    if not name:
        print("Student name cannot be empty.")
        return
    
    for student in students:
        if student["name"].lower().strip() == name.lower().strip():
            print(f"Student '{name}' already exists.")
            return
    
    new_student = {
        "name": name,
        "grades": []
    }
    students.append(new_student)
    print(f"Student '{name}' added successfully.")

def add_grades_for_student(students):
    """Option 2: Add grades for a student"""
    if not students:
        print("No students available. Please add students first.")
        return
    
    name = input("Enter student name: ").strip()
    
    if not name:
        print("Student name cannot be empty.")
        return
    
    student_found = None
    for student in students:
        if student["name"].lower().strip() == name.lower().strip():
            student_found = student
            break
    
    if not student_found:
        print(f"Student '{name}' not found.")
        if students:
            available_names = [s["name"] for s in students]
            print(f"Available students: {', '.join(available_names)}")
        return
    
    print(f"Adding grades for {student_found['name']}:")
    print("Enter grades between 0-100, or 'done' to finish.")
    
    grades_added = 0
    while True:
        grade_input = input("Enter a grade (or 'done' to finish): ").strip().lower()
        
        if grade_input == 'done':
            if grades_added == 0:
                print("No grades were added.")
            else:
                print(f"Added {grades_added} grade(s). Total grades: {len(student_found['grades'])}")
            break
        
        try:
            if ',' in grade_input:
                grade_input = grade_input.replace(',', '.')
            
            grade = float(grade_input)
            
            if grade < 0 or grade > 100:
                print("Grade must be between 0 and 100.")
                continue
                
            if not grade.is_integer():
                print(f"Note: Decimal grade {grade} accepted.")
            
            student_found["grades"].append(grade)
            grades_added += 1
            print(f"Grade {grade} added. Current average: {calculate_average(student_found['grades']):.1f}")
            
        except ValueError:
            print("Invalid input. Please enter a number between 0-100, 'done', or 'cancel'.")

def calculate_average(grades):
    """Helper function to calculate average of grades"""
    if not grades:
        return None
    try:
        return sum(grades) / len(grades)
    except (ZeroDivisionError, TypeError):
        return None

def show_report(students):
    """Option 3: Show report for all students"""
    if not students:
        print("No students available.")
        return
    
    print("\n--- Student Report ---")
    
    averages = []
    students_with_grades = 0
    
    for student in students:
        avg = calculate_average(student["grades"])
        
        if avg is None:
            print(f"{student['name']}'s average grade is N/A. (No grades)")
        else:
            print(f"{student['name']}'s average grade is {avg:.1f}. Grades: {student['grades']}")
            averages.append(avg)
            students_with_grades += 1
    
    if averages:
        max_avg = max(averages)
        min_avg = min(averages)
        overall_avg = sum(averages) / len(averages)
        
        print("---")
        print(f"Students with grades: {students_with_grades}/{len(students)}")
        print(f"Max Average: {max_avg:.1f}")
        print(f"Min Average: {min_avg:.1f}")
        print(f"Overall Average: {overall_avg:.1f}")
        
        if len(averages) > 1:
            grade_range = max_avg - min_avg
            print(f"Average Range: {grade_range:.1f}")
    else:
        print("---")
        print("No students with grades to calculate statistics.")

def find_top_performer(students):
    """Option 4: Find top performer"""
    if not students:
        print("No students available.")
        return
    
    students_with_grades = [s for s in students if s["grades"]]
    
    if not students_with_grades:
        print("No students with grades available.")
        return
    
    try:
        top_students = []
        top_avg = -1
        
        for student in students_with_grades:
            avg = calculate_average(student["grades"])
            if avg > top_avg:
                top_avg = avg
                top_students = [student]
            elif avg == top_avg:
                top_students.append(student)
        
        if len(top_students) == 1:
            print(f"The student with the highest average is {top_students[0]['name']} with a grade of {top_avg:.1f}.")
        else:
            names = [s['name'] for s in top_students]
            print(f"Multiple top performers with average {top_avg:.1f}: {', '.join(names)}")
            
    except Exception as e:
        print(f"Error finding top performer: {e}")

def backup_student_data(students):
    """Optional: Backup function for student data"""
    return [student.copy() for student in students]

if __name__ == "__main__":
    main()