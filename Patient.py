class Patient:
    """Patient class"""

    def __init__(self, first_name, surname, age, mobile, postcode):
        self.__first_name = first_name
        self.__surname = surname
        self.__age = age
        self.__mobile = mobile
        self.__postcode = postcode
        
        self.__doctor = None
        self.__symptoms = []

    def full_name(self):
        """full name is first_name and surname"""
        return f"{self.__first_name} {self.__surname}"
    
    
    def get_full_name(self):
        return self.full_name()
    
    def get_age(self):
        return self.__age
    
    def get_mobile(self):
        return self.__mobile
    
    def get_postcode(self):
        return self.__postcode

    def get_doctor(self):
        return self.__doctor

    def link(self, doctor):
        self.__doctor = doctor
        
    def add_symptom(self, symptom):
        self.__symptoms.append(symptom)

    def print_symptoms(self):
        """prints all the symptoms"""
        if not self.__symptoms:
            print(f"{self.full_name()} has no recorded symptoms.")
        else:
            print(f"Symptoms for {self.full_name()}:")
            for symptom in self.__symptoms:
                print(f"- {symptom}")

    def __str__(self):
        return (
            f"Patient Name: {self.full_name()}\n"
            f"Age: {self.__age}\n"
            f"Mobile: {self.__mobile}\n"
            f"Postcode: {self.__postcode}\n"
            f"Doctor: {self.__doctor}\n"
        )
    
    def summary(self):
        return f"{self.full_name():10} | {self.age:5} | {self.postcode:5}"
    
    
