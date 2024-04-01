from patient import Patient
from doctor import Doctor
from hospital_system import HospitalSystem

#main function to run system
def main():
    hospital = HospitalSystem()

    # use loop to print different menus of system 
    while True:
        print()
        print("Hospital Management System Menu:")
        print("1. Patient & Doctor Manager")
        print("2. Manage the Queue")
        print("3. Doctor")
        print("4. Prescription")
        print("5. Exit")

        choice = input("Enter your choice: ")
        # if else structure for choice
        if choice == '1':
            print()
            print("Prescription Manager:")
            print("a. Add Patient")
            print("b. Update Patient")
            print("c. Remove Patient")
            print("d. View Patients")
            print("e. Add Doctor Information")
            print("f. Exit")
            prescription_choice = input("Enter your choice: ")

            if prescription_choice == 'a':

                patient_id = input("Enter patient ID: ")
                patient_name = input("Enter patient name: ")
                patient_age = input("Enter patient age: ")
                #use hospital class function to add patient details
                hospital.add_patient(Patient(patient_id, patient_name, patient_age))
                print("Patient added successfully.")
            elif prescription_choice == 'b':
                
                patient_id = input("Enter patient ID to update: ")
                
                patient = hospital.find_patient_by_id(patient_id)
                if patient:
                    new_name = input("Enter new name for patient: ")
                    new_age = input("Enter new age for patient: ")
                    hospital.update_patient(patient_id, new_name, new_age)
                    print("Patient record updated successfully.")
                else:
                    print("Patient with given ID not found.")
            elif prescription_choice == 'c':
               
                patient_id = input("Enter patient ID to remove: ")
                
                patient = hospital.find_patient_by_id(patient_id)
                if patient:
                    #remove_patient function
                    hospital.remove_patient(patient_id)
                    print("Patient record removed successfully.")
                else:
                    print("Patient with given ID not found.")
            elif prescription_choice == 'd':
                print()
                print("Patients:")
                #view_patient function
                hospital.view_patients()
            elif prescription_choice == 'e':
                doctor_id = input("Enter doctor ID: ")
                doctor_name = input("Enter doctor name: ")
                doctor_specialty = input("Enter doctor specialty: ")
                #use hospital class function to add doctor
                hospital.add_doctor(Doctor(doctor_id, doctor_name, doctor_specialty))
                print("Doctor added successfully.")
            elif prescription_choice == 'f':
                continue
            else:
                print("Invalid choice. Please try again.")

        elif choice == '2':
            print()
            print("Queue and Prescription Manager:")
            print("a. View Queues")
            print("b. Add Patient to Queue")
            print("c. Remove Patient from Queue")
            print("d. Exit")
            queue_choice = input("Enter your choice: ")

            if queue_choice == 'a':
                print()
                print("Queues:")
                #use queues with the help of loop to find doctors
                for doctor_id, queue in hospital.queues.items():
                    doctor = hospital.find_doctor_by_id(doctor_id)
                    if doctor:
                        print("Doctor:", doctor.name)
                        for patient_id in queue:
                            patient = hospital.find_patient_by_id(patient_id)
                            if patient:
                                print("Patient ID:", patient.id, "Name:", patient.name)
                            else:
                                print("Patient not found")
                    else:
                        print("Doctor not found")

            elif queue_choice == 'b':
                print("Patients to be waited for consultation:")
                for patient in hospital.patients:
                    print("Patient ID:", patient.id, "- Name:", patient.name)
                print()
                print("Available Doctors:")
                for doctor in hospital.doctors:
                    print("Doctor ID:", doctor.id, "- Name:", doctor.name)
                patient_id = input("Enter patient ID: ")
                doctor_id = input("Enter doctor ID: ")
                #find_patient_by_id function
                patient = hospital.find_patient_by_id(patient_id)
                doctor = hospital.find_doctor_by_id(doctor_id)
                if patient and doctor:
                    #add_to_queue function 
                    hospital.add_to_queue(patient_id, doctor_id)
                    print("Patient added to", doctor.name, "'s queue successfully.")
                else:
                    print("Patient or Doctor not found.")
                    
            elif queue_choice == 'c':
                doctor_id = input("Enter doctor ID: ")
                hospital.remove_from_queue(doctor_id)
            elif queue_choice == 'd':
                continue
            else:
                print("Invalid choice. Please try again.")

        elif choice == '3':
            print()
            print("Doctor Options:")
            print("a. Patient History")
            print("b. Current Condition")
            print("c. Prescription")
            print("d. Transfer")
            print("e. Exit")
            
            print("Available Doctors:")
            for doctor in hospital.doctors:
                print("Doctor ID:", doctor.id, "- Name:", doctor.name)

            doctor_id = input("Enter doctor ID: ")

            queue = hospital.view_queue(doctor_id)
            if queue:
                patient_id = queue[0]
                #find_patient_by_id function of class hospital
                patient = hospital.find_patient_by_id(patient_id)
            else:
                print("No patients in the queue for this doctor.")
            doctor_choice = input("Enter your choice from above options a/b/c/d/e: ")

            if doctor_choice == 'a':
                if patient:
                    print("Patient Details:")
                    print("ID:", patient.id, "- Name:", patient.name, "- Age:", patient.age)
                else:
                    print("Patient not found.")

            elif doctor_choice == 'b':
                if patient:
                    condition = input("Enter patient's current condition: ")
                    #update_condition function 
                    patient.update_condition(condition)  
                    print("Patient's condition updated successfully.")
                else:
                    print("Patient not found.")

            elif doctor_choice == 'c':
                if patient:
                    medication = input("Enter medication name: ")
                    dose = input("Enter dose in ml: ")
                    days = input("Enter duration (in days): ")
                    frequency = input("Enter how much frequency of medication take once: ")
                    #call prescribe_medication function of hospital
                    hospital.prescribe_medication(patient_id, patient.name, medication, dose, frequency, days)
                else:
                    print("Patient not found.")

            elif doctor_choice == 'd':
                # Transfer patient
                print("Available Doctors:")
                #loop to display 
                for doctor in hospital.doctors:
                    print("Doctor ID:", doctor.id, "- Name:", doctor.name)

                transfer_doctor_id = input("Enter destination doctor ID to transfer patient: ")

                if hospital.find_doctor_by_id(transfer_doctor_id):
                    current_doctor_id = doctor_id
                    #call function of class hospital name view_queue
                    current_queue = hospital.view_queue(current_doctor_id)
                    if current_queue:
                        print("Patients in the current doctor's queue:")
                        for patient_id in current_queue:
                            #call patient_by_id function of hospital class 
                            patient = hospital.find_patient_by_id(patient_id)
                            print("Patient ID:", patient.id, "- Name:", patient.name)
                        patient_id_to_transfer = input("Enter patient ID to transfer: ")

                        if patient_id_to_transfer in current_queue:
                            #call hospital function remove_from_queue
                            hospital.remove_from_queue(current_doctor_id)
                            #call hospital function add_to_queue
                            hospital.add_to_queue(patient_id_to_transfer, transfer_doctor_id)
                            print("Patient transferred successfully.")
                        else:
                            print("Patient not found in the current doctor's queue.")
                    else:
                        print("No patients in the current doctor's queue.")
                else:
                    print("Invalid destination doctor ID.")

            elif doctor_choice == 'e':
                continue
            else:
                print("Invalid choice. Please try again.")

        elif choice == '4':
            #call view_prescription function of hospital class
            hospital.view_prescriptions()
                    
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("")

if __name__ == "__main__":
    main()