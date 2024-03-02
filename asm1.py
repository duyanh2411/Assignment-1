class Pupil:
    def __init__(self, name, roll_number, marks):
        self.name = name
        self.roll_number = roll_number
        self.marks = marks

class PupilManagementSystem:
    def __init__(self):
        self.pupils = []

    def create_pupil_record(self):
        name = input("Enter pupil's name: ")
        roll_number = input("Enter pupil's roll number: ")
        english_marks = float(input("Enter pupil's marks in English: "))
        math_marks = float(input("Enter pupil's marks in Math: "))
        physics_marks = float(input("Enter pupil's marks in Physics: "))
        chemistry_marks = float(input("Enter pupil's marks in Chemistry: "))
        cs_marks = float(input("Enter pupil's marks in Computer Science: "))
        marks = {
            'English': english_marks,
            'Math': math_marks,
            'Physics': physics_marks,
            'Chemistry': chemistry_marks,
            'Computer Science': cs_marks
        }
        pupil = Pupil(name, roll_number, marks)
        self.pupils.append(pupil)
        print("Pupil record created.")

    def display_all_pupil_records(self):
        if not self.pupils:
            print("No pupil records.")
        else:
            print("All pupil records:")
            for idx, pupil in enumerate(self.pupils, 1):
                print(f"{idx}. Name: {pupil.name}, Roll Number: {pupil.roll_number}, Marks: {pupil.marks}")

    def search_pupil_record(self):
        roll_number = input("Enter pupil's roll number to search: ")
        found = False
        for pupil in self.pupils:
            if pupil.roll_number.lower() == roll_number.lower():
                print(f"Found pupil with roll number {roll_number}: Name - {pupil.name}, Marks - {pupil.marks}")
                found = True
                break
        if not found:
            print(f"No pupil found with roll number {roll_number}.")

    def modify_pupil_record(self):
        roll_number = input("Enter pupil's roll number to modify: ")
        for pupil in self.pupils:
            if pupil.roll_number.lower() == roll_number.lower():
                print(f"Pupil with roll number {roll_number} found.")
                new_name = input("Enter new name (press Enter to keep current): ")
                english_marks = input("Enter new marks in English (press Enter to keep current, 0 to skip): ")
                math_marks = input("Enter new marks in Math (press Enter to keep current, 0 to skip): ")
                physics_marks = input("Enter new marks in Physics (press Enter to keep current, 0 to skip): ")
                chemistry_marks = input("Enter new marks in Chemistry (press Enter to keep current, 0 to skip): ")
                cs_marks = input("Enter new marks in Computer Science (press Enter to keep current, 0 to skip): ")
                if new_name:
                    pupil.name = new_name
                if english_marks.strip() != '':
                    pupil.marks['English'] = float(english_marks)
                if math_marks.strip() != '':
                    pupil.marks['Math'] = float(math_marks)
                if physics_marks.strip() != '':
                    pupil.marks['Physics'] = float(physics_marks)
                if chemistry_marks.strip() != '':
                    pupil.marks['Chemistry'] = float(chemistry_marks)
                if cs_marks.strip() != '':
                    pupil.marks['Computer Science'] = float(cs_marks)
                print("Pupil record modified.")
                return
        print(f"No pupil found with roll number {roll_number}.")

    def delete_pupil_record(self):
        roll_number = input("Enter pupil's roll number to delete: ")
        for pupil in self.pupils:
            if pupil.roll_number.lower() == roll_number.lower():
                self.pupils.remove(pupil)
                print(f"Pupil record with roll number {roll_number} deleted.")
                return
        print(f"No pupil found with roll number {roll_number}.")

    def display_report_menu(self):
        print("\nReport Menu:")
        print("1. Class Result")
        print("2. Pupil Report Card")
        choice = input("Enter your choice (1-2): ")
        return choice

    def display_class_result(self):
        if not self.pupils:
            print("No pupil records.")
        else:
            print("Class Result:")
            total_marks = {
                'English': 0,
                'Math': 0,
                'Physics': 0,
                'Chemistry': 0,
                'Computer Science': 0
            }
            total_pupils = len(self.pupils)
            for pupil in self.pupils:
                for subject, marks in pupil.marks.items():
                    total_marks[subject] += marks

            # Calculate average marks for each subject
            average_marks = {subject: total_marks[subject] / total_pupils for subject in total_marks}
            print("Average Marks:")
            for subject, avg_mark in average_marks.items():
                print(f"{subject}: {avg_mark:.2f}")

    def display_pupil_report_card(self):
        roll_number = input("Enter pupil's roll number to view report card: ")
        found = False
        for pupil in self.pupils:
            if pupil.roll_number.lower() == roll_number.lower():
                print(f"Report Card for Pupil with Roll Number {roll_number}:")
                print(f"Name: {pupil.name}")
                print("Marks:")
                for subject, marks in pupil.marks.items():
                    print(f"{subject}: {marks}")
                found = True
                break
        if not found:
            print(f"No pupil found with roll number {roll_number}.")

    def display_main_menu(self):
        print("\nMain Menu:")
        print("1. Admin")
        print("2. Report")
        print("3. Exit")
        choice = input("Enter your choice (1-3): ")
        return choice

    def run(self):
        while True:
            main_choice = self.display_main_menu()
            if main_choice == "1":
                admin_choice = input("Admin Menu:\n1. Create pupil record\n2. Display all pupil records\n3. Search pupil record\n4. Modify pupil record\n5. Delete pupil record\n6. Back to main menu\nEnter your choice (1-6): ")
                if admin_choice == "1":
                    self.create_pupil_record()
                elif admin_choice == "2":
                    self.display_all_pupil_records()
                elif admin_choice == "3":
                    self.search_pupil_record()
                elif admin_choice == "4":
                    self.modify_pupil_record()
                elif admin_choice == "5":
                    self.delete_pupil_record()
                elif admin_choice == "6":
                    continue
                else:
                    print("Invalid choice. Please enter a valid option.")
            elif main_choice == "2":
                report_choice = self.display_report_menu()
                if report_choice == "1":
                    self.display_class_result()
                elif report_choice == "2":
                    self.display_pupil_report_card()
                else:
                    print("Invalid choice. Please enter a valid option.")
            elif main_choice == "3":
                print("Exiting the system. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    pms = PupilManagementSystem()
    pms.run()
