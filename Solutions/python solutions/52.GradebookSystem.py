def calculate_gpa(grades):
    return sum(grades) / len(grades) if grades else 0

def main():
    gradebook = {
        "Alice": [85, 90, 88],
        "Bob": [78, 81, 79]
    }
    
    class_total = 0
    student_count = 0
    for student, grades in gradebook.items():
        gpa = calculate_gpa(grades)
        print(f"{student} GPA: {gpa:.2f}")
        class_total += gpa
        student_count += 1
        
    if student_count > 0:
        print(f"Class Average GPA: {class_total/student_count:.2f}")

if __name__ == "__main__":
    main()
