from student import Student
from result import Result

def get_student_details():
    name = input("Enter student name: ")
    
    try:
        physics = float(input("Enter marks for Physics (0-100): "))
        chemistry = float(input("Enter marks for Chemistry (0-100): "))
        maths = float(input("Enter marks for Maths (0-100): "))
        computer_science = float(input("Enter marks for Computer Science (0-100): "))

        if not all(0 <= mark <= 100 for mark in [physics, chemistry, maths, computer_science]):
            raise ValueError("Marks should be between 0 and 100.")
        
    except ValueError as e:
        print(f"Invalid input: {e}")
        return None

    return Student(name, physics, chemistry, maths, computer_science)

def display_result(student, result):
    if student is None:
        print("Student details are invalid. Cannot proceed.")
        return

    print(f"\nStudent Name: {student.name}")
    print(f"Average Marks: {result.calculate_average():.2f}")
    print(f"Result: {result.determine_result()}")

def main():
    while True:
        student = get_student_details()
        if student is None:
            return
        result = Result(student)
        display_result(student, result)
        result.save_to_excel()
        another_student = input("Do you want to enter another student's data? (yes/no): ").strip().lower()
        if another_student != 'yes':
            print("All data has been saved to Excel.")
            break

if __name__ == "__main__":
    main()
