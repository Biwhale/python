class Person_Data:
    def __init__(self):
        self.__nric = ""
        self.__first_name = ""
        self.__last_name = ""
        self.__DOB = ""
        self.__home_address = ""
        self.__contact_number = ""
        self.__gender = ""
        self.__type = ""
        self.__allergy = ""
        self.__Clinic = None #clinic
    def get_nric():
        return self.__nric
    def get_first_name():
        return self.__first_name
    def get_date_of_birth():
        return self.__DOB
    def get_home_address():
        return self.__home_address
    def get_contact_number():
        return self.__contact
    def get_gender():
        return self.__gender
    def get_type():
        return self.__type
    def get_allergy():
        return self.__allergy
    def get_clinic():
        return self.__Clinic
    def set_nric(nric):
        self.__nric = nric
    def set_first_name(first_name):
        self.__first_name = first_name
    def set_date_of_birth(dob):
        self.__DOB = dob
    def set_home_address(addy):
        self.__home_address = addy
    def set_contact_number(num):
        self.__contact = num
    def set_gender(gender):
        self.__gender = gender
    def get_type(type):
        self.__type = type
    def set_allergy(allergy):
        self.__allergy = allergy
    def set_clinic(clinic):
        self.__Clinic = clinic
    def Display(self):
        pass
    

class Clinic:
    def __init__(self):
        self.__clinic = ""
        self.__clinic_address = ""
        self.__clinic_contact = ""
    def get_clinic(self):
        return self.__clinic
    def get_clinic_address(self):
        return self.__clinic_address
    def get_clinic_contact(self):
        return self.__clinic_contact
    def set_clinic(self,clinic):
        self.__clinic = clinic
    def set_clinic_address(self,addy):
        self.clinic_address = addy
    def set_clinic_contact(self,num):
        self.__clinic_contact = num
    def Display(self):
        pass
class Staff_Data(Person_Data):
    def __init__(self):
        super().__init__()
        self.__Status = ""

    def get_Status(self):
        return self.__Status
    def set_Status(self,status):
        self.__Status = status
    def Display(self):
        pass
    




#main program

file = open("CLINICS_DATA.csv", 'r')
file.readline()

for line in file:
    type,nric,first_name,last_name,DOB,home_addy, contact_num, gender, clinic, clinic_addy, clinic_num,allergy,status = line.split(',')
    if allergy == "":
        staff_data = Staff_Data()
        staff_data.set_nric(nric)
        staff_data.set_first_name(first_name)
        staff_data.set_last_name(last_name)
        staff_data.set_date_of_birth(DOB)
        staff_data.set_home_address(home_addy)
        staff_data.set_contact_number(contact_num)
        staff_data.set_gender(gender)
        
    person_data = Person_Data()
    clinc_data = Clinic_Data()
    person_data.set_nric(nric)
    person_data.set_first_name(first_name)
    person_data.set_last_name(last_name)
    person_data.set_date_of_birth(DOB)
    person_data.set_home_address(home_addy)
    person_data.set_contact_number(contact_num)
    person_data.set_gender(gender)
    clinic_data.set_clinic(clinic)
    clinic_data.set_clinic_address(clinic_addy)
    clinic_data.set_clinic_contact(clinic_num)
    if allergy == "":
        staff_data
    
    


    
