#Create class for add prescription
class Prescription:
    def __init__(self, patient_id, patient_name, medication, dose, frequency, days):
        self.patient_id = patient_id     #patient_id
        self.patient_name = patient_name   #patient name
        self.medication = medication      #patient medication
        self.dose = dose             
        self.frequency = frequency
        self.days = days

#create class to manage hospital system
class HospitalSystem:
    def __init__(self):
        #use lists to store data
        self.patients = []      #list to store patients
        self.doctors = []       #list to store doctors
        self.prescriptions = [] #list to store prescriptions
        #use dictionary for queue
        self.queues = {}
        self.prescribed_patients = []

    # add new patient function
    def add_patient(self, patient):
        self.patients.append(patient)

    # update record function
    def update_patient(self, patient_id, new_name, new_age):
        #for loop to update record
        for patient in self.patients:
            if patient.id == patient_id:
                patient.name = new_name
                patient.age = new_age
                return True
        return False

    # delete patient function
    def remove_patient(self, patient_id):
        #for loop to remove patients
        for patient in self.patients:
            if patient.id == patient_id:
                self.patients.remove(patient)
                return True
        return False

    # find the patient function
    def find_patient_by_id(self, patient_id):
        #for loop to find patients
        for patient in self.patients:
            if patient.id == patient_id:
                return patient
        return None

    # view details of patient function 
    def view_patients(self):
        #loop to viw patients
        for patient in self.patients:
            #print details of patient by using patient class objects
            print("ID:", patient.id, "Name:", patient.name, "Age:", patient.age, "Condition:", patient.condition)

   # find doctor by name function        
    def find_doctor_by_name(self, doctor_name):
        #loop to find doctors by name
        for doctor in self.doctors:
            if doctor.name == doctor_name:
                return doctor
        return None
    
    # add new doctor function
    def add_doctor(self, doctor):
        self.doctors.append(doctor)

    # find doctor by his id function
    def find_doctor_by_id(self, doctor_id):
        #loop to find doctor by id
        for doctor in self.doctors:
            if doctor.id == doctor_id:
                return doctor
        return None

    #add patient in queue function
    def add_to_queue(self, patient_id, doctor_id):
        #condition to check doctor in queue
        if doctor_id not in self.queues:
            self.queues[doctor_id] = []
        self.queues[doctor_id].append(patient_id)

    # remove patient from queue function
    def remove_from_queue(self, doctor_id):
        #condition to check doctor is in doctor list
        if doctor_id in self.queues and self.queues[doctor_id]:
            patient_id = self.queues[doctor_id].pop(0)  # Remove the first patient
            patient = self.find_patient_by_id(patient_id)
            if patient:
                print("Patient Consultation is done for patient:", patient.name)
            else:
                print("Patient not found.")
        else:
            print("Queue is empty.")

    #view doctors in queue
    def view_queue(self, doctor_id):
        #condition ti check doctor in queue
        if doctor_id in self.queues:
            return self.queues[doctor_id]
        else:
            return []

    #add doctor
    def add_doctor(self, doctor):
        self.doctors.append(doctor)

    # medicine prescribed by doctor function
    def prescribe_medication(self, patient_id, patient_name, medication, dose, frequency, days):
        self.prescriptions.append(Prescription(patient_id, patient_name, medication, dose, frequency, days))
        print("Prescription added successfully.")
        print("Patient removed from the queue")
        # Remove patient from the queue
        doctor_id = None
        #loop to add medication
        for doc_id, queue in self.queues.items():
            if patient_id in queue:
                doctor_id = doc_id
                queue.remove(patient_id)
                break
        
        if doctor_id:
            patient_details = {'patient_id': patient_id, 'patient_name': patient_name, 'medication': medication, 'dose': dose, 'frequency': frequency, 'days': days}
            self.prescribed_patients.append(patient_details)
        else:
            print("Patient not found in any queue.")

    #view patient prescription using stack
    def view_prescriptions(self):
        print()
        print("Prescriptions (LIFO):")
        #loop to show prescription of patient 
        while self.prescriptions:
            prescription = self.prescriptions.pop()
            print("Patient ID:", prescription.patient_id)
            print("Patient Name:", prescription.patient_name)
            print("Medication:", prescription.medication)
            print("Dose:", prescription.dose)
            print("Frequency:", prescription.frequency)
            print("Days:", prescription.days)
            print("--------------------")

    #transfer patient to other doctor function    
    def transfer_patient(self, patient_id, from_doctor_id, to_doctor_id):
        #condition to check doctor and patient in queue
        if from_doctor_id in self.queues and patient_id in self.queues[from_doctor_id]:
            self.queues[from_doctor_id].remove(patient_id)
            
            if to_doctor_id in self.queues:
                self.queues[to_doctor_id].append(patient_id)
                print("Patient transferred successfully from Doctor", from_doctor_id, "to Doctor", to_doctor_id)
            else:
                print("Destination doctor not found.")
        else:
            print("Patient not found in Doctor", from_doctor_id, "queue or Doctor", from_doctor_id, "queue is empty.")
