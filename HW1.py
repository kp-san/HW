# HW1

class Instructor:
    def __init__(self, name, mil_staff, phd_held, classes_taught, years_at_cga):
        self.name = name
        self.mil_staff = mil_staff
        self.phd_held = phd_held
        self.classes_taught = classes_taught
        self.years_at_cga = years_at_cga
    
    def display_information(self):
        print(f"Name: {self.name}")
        print(f"Military or Civilian: {self.mil_staff}")
        print(f"PHD held: {self.phd_held}")
        print(f"Classes Taught: {self.classes_taught}")
        print(f"Years Teaching: {self.years_at_cga}")
        print()

# Function to create a new instructor from user input
def create_staff_from_input():
    name = input("Enter Instructor's name: ")
    mil_staff = input("Military or Civilian: ")
    phd_held = input("PhD: ")
    classes_taught = input("Classes Taught: ")
    years_at_cga = input("Years Teaching: ")
    return Instructor(name, mil_staff, phd_held, classes_taught, years_at_cga)
    
# Function to enter multiple instructors
def enter_intructors():
    instructors = []

    while True:
        instructor = create_staff_from_input()
        instructors.append(instructor)

        add_more = input("Do you want to add another instructor? (yes/no): ").lower()
        if add_more != 'yes':
            break
    return instructors

all_instructors = enter_intructors()

# Display information for all instructors
for instructor in all_instructors:
    instructor.display_information()