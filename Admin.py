from Doctor import Doctor


class Admin:
    """A class that deals with the Admin operations"""
    def __init__(self, username, password, address):
        """
        Args:
            username (string): Username
            password (string): Password
            address (string, optional): Address Defaults to ''
        """

        self.__username = username
        self.__password = password
        self.__address =  address

    def view(self, a_list):
        """
        print a list
        Args:
            a_list (list): a list of printables
        """
        for index, item in enumerate(a_list):
            print(f"{index+1:>3} | {item}")

    def login(self):
        """
        A method that deals with the login
        Raises:
            Exception: returned when the username and the password ...
                    ... don`t match the data registered
        Returns:
            string: the username
        """  
    
        
    
        print("-----Login-----")
        username = input("Enter the username: ")
        password = input("Enter the password: ")
        address = input("Enter the address: ")
        
        if username == self.__username and password == self.__password and address == self.__address:
            return username
        else:
            raise Exception("Invalid username or password")

    def find_index(self,index,doctors):
        return index in range(len(doctors))
            
    def get_doctor_details(self) :
        first = input("Enter the first name: ")
        surname = input("Enter the surname: ")
        speciality = input("Enter the speciality: ")
        return first, surname, speciality

    def doctor_management(self, doctors):
        print("-----Doctor Management-----")
        # menu
        print("Choose the operation:")
        print(" 1 - Register")
        print(" 2 - View")
        print(" 3 - Update")
        print(" 4 - Delete")
        op = input("Input: ")


      # Register  
        if op == '1':
            print("-----Register-----")
            first, surname, speciality = self.get_doctor_details()
            
            for doctor in doctors:
                if doctor.get_first_name() == first and doctor.get_surname() == surname:
                    print("Name already exists.")
                    
                
            doctors.append(Doctor(first, surname, speciality))
            print("Doctor registered.")

       # View 
        elif op == "2":
            print("-----List of Doctors-----")
            print("ID | Full Name | Speciality")
            for i, d in enumerate(doctors):
                print(f"{i+1} | {d.get_first_name()} {d.get_surname()} | {d.get_speciality()}")
            

       # Update 
        elif op == "3":
            if not doctors:
                print("No doctors available to update.")
                return
            
            print("\n---- Doctors List ----")
            for i, d in enumerate(doctors):
                print(f"{i+1} | {d.get_first_name()} {d.get_surname()} | {d.get_speciality()}")

                try:
                    index = int(input("Enter the ID of the doctor: ")) - 1
                    
                    if index < 0 or index >= len(doctors):
                        print("The ID entered was not found.")
                        return
                    
                    doctor = doctors[index]
                    
                    print("\nChoose the field to be updated:")
                    print("1 First name")
                    print("2 Surname")
                    print("3 Speciality")
                    choice = input("Input: ")
                    
                    if choice == "1":
                        doctors[index].set_first_name(input("Enter the first new name: "))
                    elif choice == "2":
                        doctors[index].set_surname(input("Enter the new surname: "))
                    elif choice == "3":
                        doctors[index].set_speciality(input("Enter the new speciality: "))
                    else:
                        print("Invalid opinion")
                        return
                    
                    print("Doctor details updated successfully.")
                        
                except ValueError:
                    print("The id entered is incorrect")                    

       # Delete
        elif op == "4":
            print("-----Delete Doctor-----")
            for i, d in enumerate(doctors):
                print(f"{i+1} | {d.get_first_name()} {d.get_surname()} | {d.get_speciality()}")
                
            try:
                index = int(input("Enter the ID of the doctor to be deleted: ")) - 1
                if self.find_index(index, doctors):
                    doctors.pop(index)
                    print("Doctor deleted")
                else:
                    print("The id entered was not found")
            except ValueError:
                print("The id entered is incorrect")
                
        else:
            print("Invalid operation chosen. Type in the correct set of keys from 1 - 6")


    def view_patient(self, patients):
        print("-----View Patients-----")
        print(f"{'ID':<4} | {'Full Name':<5} | {'Doctor':<5} | {'Age':<5} | {'Mobile':<5} | {'Postcode':<5}")
        
        
        for i, p in enumerate(patients):
            doctor = p.get_doctor()
            doctor_name = doctor.full_name() if doctor else "None"
            

            print(
                f"{i+1:<4} | "
                f"{p.get_full_name():<5} | "
                f"{doctor_name:<5} | "
                f"{p.get_age():<5} | "
                f"{p.get_mobile():<5} | "
                f"{p.get_postcode():<5}"
            ) 

    def assign_doctor_to_patient(self, patients, doctors):
        print("-----Assign-----")
        self.view(patients)

        try:        
            patient_index = int(input("Please enter the patient ID: ")) - 1
            if patient_index not in range(len(patients)):
                print("The id entered was not found")
                return # stop the procedures
        except ValueError:
            print("The id entered is incorrect")
            return # stop the procedures

        print("-----Doctors Select-----")
        print("Select the doctor that fits these symptoms:")
        patients[patient_index].print_symptoms() # print the patient symptoms
        
        for i, d in enumerate(doctors):
            print(f"{i+1} | {d.get_first_name()} {d.get_surname()} | {d.get_speciality()}")


        try:
            # doctor_index is the patient ID mines one (-1)
            doctor_index = int(input("Please enter the doctor ID: ")) -1

            # check if the id is in the list of doctors
            if self.find_index(doctor_index,doctors):
                patients[patient_index].link(doctors[doctor_index])
                print("The patient is now assigned to the doctor.")
            else:
                print("The id entered was not found.")
        except ValueError:
            print("The id entered is incorrect")


    def discharge(self, patients, discharge_patients):
        while True:
            self.view_patient(patients)
            
            choice = input("Do you want to discharge a patient(Y/N): ").strip().upper()
            
            
            if choice == "N":
                break
            
            elif choice == "Y":
                try:
                    index = int(input("Please enter the patient ID: ")) - 1
                
                    if index in range(len(patients)):
                        discharge_patients.append(patients.pop(index))
                        print("Patient discharged.\n")
                    else:
                        print("The id entered was not found.\n")
                        
                except ValueError:
                    print("The id entered was incorrect.\n")
                    
             
             

    def view_discharged(self, discharged_patients):
        print("-----Discharged Patients-----")
        print("ID | Full Name | Doctor | Age | Mobile | Postcode")
        
        print("DEBUG: discharged_patients length = ", len(discharged_patients))
        for i, p in enumerate(discharged_patients):
            doctor = p.get_doctor()
            doctor_name = (
                doctor.get_first_name() + " " + doctor.get_surname()
                if doctor else "None"
            )
            
            print(
                f"{i+1:<3} |"
                f"{p.get_full_name():<3} | "
                f"{doctor_name:<3} | "
                f"{p.get_age():<3} | "
                f"{p.get_mobile():<3} | "
                f"{p.get_postcode():<3}"
            )

    def update_details(self):
        print("Choose the field to be updated: ")
        print(" 1 Username")
        print(" 2 Password")
        print(" 3 Address")
        op = input("Input: ")

        if op == "1":
            self.__username = input("Enter in a new username: ").strip()
            print("Username updated. Please log in again.")
            return True


        elif op == "2":
            password = input("Enter the new password: ")
            # validate the password
            if password == input("Enter the new password again: "):
                self.__password = password
                print("Password updated. Please log in again.")
                return True
            else:
                print("Password does not match. Please try again")
                return False
                

        elif op == "3":
            self.__address = input("Enter in the new address/postcode: ").strip()
            print("Address updated. Please log in again.")
            return True

        else:
            print("Invalid option")
            return False


