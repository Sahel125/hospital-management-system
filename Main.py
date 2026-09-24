
from Admin import Admin
from Doctor import Doctor
from Patient import Patient

def show_menu():
    print("\nChoose the operation:")
    print("1- Register/view/update/delete doctor")
    print("2- Discharge patients")
    print("3- View discharged patient")
    print("4- Assign doctor to a patient")
    print("5- Update admin details")
    print("6- Quit")
    
def main():
    """
    the main function to be ran when the program runs
    """
            

    
    admin = Admin("Admin", "123", "B1 1AB") 
    
    
    
    doctors = [
        Doctor("John","Smith","Internal Med."),
        Doctor("Jone","Smith","Pediatrics"),
        Doctor("Jone","Carlos","Cardiology")
    ]
      
    patients = [
        Patient("Sara","Smith", 20, "07012345678","B1 234"),
        Patient("Mike","Jones", 37,"07555551234","L2 2AB"),
        Patient("David","Smith", 15, "07123456789","C1 ABC")
    ]
    
    discharged_patients = []
    
    running = False

    while True:
        if admin.login():
            running = True 
            break
        else:
            print('Incorrect username or password.')

    while running:
        
        print("\nChoose the operation:")
        print("1- Register/view/update/delete doctor")
        print("2- Discharge patients")
        print("3- View discharged patient")
        print("4- Assign doctor to a patient")
        print("5- Update admin details")
        print("6- Quit")

        
        op = input("Option: ")
        
        
        if op == "1":
            admin.doctor_management(doctors)

        
        elif op == "2":
            admin.discharge(patients, discharged_patients)

         
        elif op == "3":
            admin.view_discharged(discharged_patients)
            

        
        elif op == "4":
            admin.assign_doctor_to_patient(patients, doctors)
        
        
        elif op == "5":
            updated = admin.update_details()
            if updated:
                print("Admin details updated. Please log in again.")
                return


        
        elif op == "6":
            print("Program terminated.")
            break

        else:
            
            print("Invalid option. Try again")

if __name__ == '__main__':
    main()
