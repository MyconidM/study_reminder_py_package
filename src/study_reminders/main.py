from study_reminders.students_manager import StudentsManager
from study_reminders.reminder_generator import generate_reminder
from study_reminders.reminder_sender import send_reminder
from study_reminders.logger import log_reminder
from study_reminders.scheduler import schedule_reminders
import threading

# drew inspiration form ChatGBT for main structure and execturion

def exit_option():
    print("Exiting the program.")
    exit(0)


def list_students_option():
    """Display all students and their information."""
    print("\n=== Student Information List ===")
    students = manager.get_students()

    # Total number of students
    print(f"Total students: {len(students)}")
    print("-" * 50)
    
    # List students details
    manager.list_students()

    print("-" * 50)
    print("=== End of List ===")


def add_student_option():
    """Add a new student to the system."""
    print("\nAdding a new student...")
    name = input("Enter student's name: ")
    email = input("Enter student's email: ")
    course = input("Enter student's course: ")
    preferred_time = input("Enter preferred reminder time: ")

    manager.add_student(name, email, course, preferred_time)
    print(f"Student {name} added successfully.")

def remove_student_option():
    """Remove a student from the system."""
    print("\n=== Remove a Student ===")
    
    students = manager.get_students()

    # Show current students first
    print("Current students:")
    for i, student in enumerate(students, 1):
        print(f"{i}. {student['name']} ({student['email']})")
    
    removeByName = input("\nEnter student's name to remove: ").strip()

    if manager.remove_student(removeByName):
        # Refresh the global students list
        students = manager.get_students()
    
    print("=== Remove Student Complete ===\n")

def send_reminders_option():
    """Send reminders to all students."""
    students = manager.get_students()
    print("Sending reminders...")
    print(f"Sending reminders to {len(students)} students...\n")
    

    for student in students:
        try: 
            # Generate reminder message
            reminder = generate_reminder(student['name'], student['course'])
            # Send the reminder
            send_reminder(student['email'], reminder)
            log_reminder(student, reminder)

        except Exception as e:
            print(f"Error sending reminder to {student['name']} ({student['email']}): {e}")

    print("All reminders sent.")

    
def run_scheduler_in_background(manager):
    """Run the scheduler in a background thread."""
    schedule_reminders(
            students_manager=manager,
            reminder_generator=generate_reminder,
            reminder_sender=send_reminder,
            logger=log_reminder
        )    


def main():
    # Load students
    global manager
    manager = StudentsManager()
    
    # Start the scheduler in a separate thread in the background using the same manager
    # Use of threding suggested by Copilot
    t = threading.Thread(target=run_scheduler_in_background, args=(manager,), daemon=True)
    t.start()
    print("Scheduler is now running. Reminders will be sent automatically.")

    # Retrieve the list of students
    global students 
    students = manager.get_students()

    # If no students found, print a message
    if not students:
        print("No students found in the system.")
        return
 

    # Menu options
    options = {
        0: exit_option,
        1: list_students_option,
        2: add_student_option,
        3: remove_student_option,
        4: send_reminders_option
    }

    while True:

        # Print menu
        print("\nMenu:")
        print("0. Exit")
        print("1. List all students")
        print("2. Add a student")
        print("3. Remove a student")
        print("4. Send all reminders now")
        
        try:
            choice = int(input("Choose an option (0-4): "))
            if choice in options:
                options[choice]()
            else:
                print("Invalid choice. Please select a valid option.")
        except ValueError:
            print("Invalid input. Please enter a number between 0 and 4.")



if __name__ == "__main__":
    main()
