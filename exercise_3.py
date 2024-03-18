import queue

class PatientQueue:
    def __init__(self):
        self.patient_queue = queue.Queue()

    def register_patient(self):
        try:
            patient_name = input("Enter patient name: ")
            self.patient_queue.put(patient_name)
            print("Patient registered")
        except Exception as e:
            print("Error: ", str(e))

    def remove_patient(self):
        if self.patient_queue.empty():
            print("Queue is empty")
        else:
            patient_name = self.patient_queue.get()
            print("Patient removed: ", patient_name)

    def display_patient_queue(self):
        if self.patient_queue.empty():
            print("Queue is empty")
        else:
            print("Current patient queue:")
            for patient in self.patient_queue.queue:
                print(patient)

    def run_menu(self):
        while True:
            print("\nMenu:")
            print("1. Register Patient")
            print("2. Remove Patient after Meeting Doctor")
            print("3. Display Patient Queue")
            print("4. Exit")
            choice = int(input("Enter your choice: "))
            if choice == 1:
                self.register_patient()
            elif choice == 2:
                self.remove_patient()
            elif choice == 3:
                self.display_patient_queue()
            elif choice == 4:
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    patient_queue = PatientQueue()
    patient_queue.run_menu()