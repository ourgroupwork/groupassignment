# create class of patient 
class Patient:
    def __init__(self, patient_id, name, age):
        self.id = patient_id
        self.name = name
        self.age = age
        self.doctors = {} 
        self.condition = ""
    # update patient record
    def update_condition(self, condition):
        self.condition = condition