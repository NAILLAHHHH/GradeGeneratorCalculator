#!/usr/bin/python3

# Define what an assignment looks like in our system
class Assignment:
    def __init__(self, name, category, weight, grade):
        self.name = name      # What's the assignment called? (e.g., "Midterm Exam")
        self.category = category  # Is it Formative (FA) or Summative (SA)?
        self.weight = weight  # How much does it count toward final grade? (e.g., 20%)
        self.grade = grade    # What score did the student get? (e.g., 85%)

# Ask the user to enter all their assignments
def collect_assignments():
    assignments = []  # We'll store all assignments here
    
    # Keep asking for assignments until user says 'done'
    while True:
        # Get assignment name
        name = input("Enter assignment name (or 'done' to finish): ").strip()
        if name.lower() == 'done':
            break  # Exit the loop if user is done
        if not name:
            print("Assignment name cannot be empty. Please enter a valid name.")
            continue  # Skip the rest and ask again

        # Get assignment type (Formative or Summative)
        category = input("Enter category (FA/SA): ").upper()
        # Keep asking until we get FA or SA
        while category not in ['FA', 'SA']:
            print("Invalid category. Please enter 'FA' (Formative) or 'SA' (Summative).")
            category = input("Enter category (FA/SA): ").upper()

        # Get how much the assignment counts (weight)
        while True:
            try:
                weight = float(input("Enter weight (as a percentage): "))
                # Weight must be between 0-100%
                if 0 <= weight <= 100:
                    break
                else:
                    print("Invalid weight. Please enter a value between 0 and 100.")
            except ValueError:  # If user enters text instead of number
                print("Invalid input. Please enter a numeric value.")

        # Get the student's grade on the assignment
        while True:
            try:
                grade = float(input("Enter grade (out of 100): "))
                # Grade must be between 0-100%
                if 0 <= grade <= 100:
                    break
                else:
                    print("Invalid grade. Please enter a value between 0 and 100.")
            except ValueError:  # If user enters text instead of number
                print("Invalid input. Please enter a numeric value.")

        # Add the new assignment to our list
        assignments.append(Assignment(name, category, weight, grade))
    
    return assignments  # Give back the complete list of assignments

# Calculate all the important grade numbers
def calculate_grades(assignments):
    formative_total = 0  # Total for all formative assignments
    summative_total = 0  # Total for all summative assignments

    # Go through each assignment and calculate its contribution
    for assignment in assignments:
        # Calculate how much this assignment counts toward final grade
        weighted_grade = assignment.grade * (assignment.weight / 100)
        
        # Add it to the appropriate total
        if assignment.category == 'FA':
            formative_total += weighted_grade
        else:
            summative_total += weighted_grade

    # Combine both types for overall grade
    total_grade = formative_total + summative_total
    # Convert to GPA (5.0 scale)
    gpa = (total_grade / 100) * 5

    return formative_total, summative_total, gpa

# Decide if student passes or fails
def determine_pass_fail(formative_total, summative_total, assignments):
    # Separate assignments by type
    formative_assignments = [a for a in assignments if a.category == 'FA']
    summative_assignments = [a for a in assignments if a.category == 'SA']

    # Calculate average for each type (avoid division by zero)
    if len(formative_assignments) > 0:
        average_formative = formative_total / len(formative_assignments)
    else:
        average_formative = 0  # If no formative assignments

    if len(summative_assignments) > 0:
        average_summative = summative_total / len(summative_assignments)
    else:
        average_summative = 0  # If no summative assignments

    # Pass if meets or exceeds both averages
    if formative_total >= average_formative and summative_total >= average_summative:
        return "Pass"
    else:
        return "Fail and Repeat"

# The main function that runs everything
def main():
    print("Welcome to the Grade Generator Calculator!")
    
    # Step 1: Get all assignments from user
    assignments = collect_assignments()

    # If no assignments entered, just exit
    if not assignments:
        print("No assignments entered. Exiting.")
        return

    # Step 2: Calculate all the grade numbers
    formative_total, summative_total, gpa = calculate_grades(assignments)
    
    # Step 3: Determine pass/fail status
    pass_fail = determine_pass_fail(formative_total, summative_total, assignments)

    # Step 4: Show the results
    print("\nResults:")
    print(f"Formative Total: {formative_total}")
    print(f"Summative Total: {summative_total}")
    print(f"GPA: {gpa}")
    print(f"Status: {pass_fail}")

# This makes sure the program runs when we execute the file
if __name__ == "__main__":
    main()
