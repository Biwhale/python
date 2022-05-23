import sqlite3

file = open("CLINICS_DATA.csv",'r')
file.readline()
db = sqlite3.connect("1B_DB.db")


db.execute('delete from Patient_Data')
db.execute('delete from Staff_Data')
db.execute('delete from Person_Data')
db.execute('delete from Clinic_Data')


class Person_Data:
    def __init__(self,n,fn,ln,dob,ha,cn,g,t,allergy):
        self.nric = n
        self.first_name = fn
        self.last_name = ln
        self.DOB = dob
        self.home_address = ha
        self.contact_number = cn
        self.gender = g
        self.type = t
        self.allergy = allergy
    

class Clinic_Data:
    def __init__(self,c,ca,cc):
        self.clinic = c
        self.clinic_address = ca
        self.clinic_contact = cc
    
class Staff_Data():
    def __init__(self,c,p,s):
        self.clinics = c
        self.person = p
        self.status = s

class Patient_Data():
    def __init__(self,c,p):
        self.clinics = c
        self.person = p

plst = []
cl_lst = []
st_lst = []
pa_lst = []

for line in file:
    t,n,fn,ln,dob,ha,cn,g,c,ca,cc,allergy,s = line.strip().split(',')

    p = Person_Data(n,fn,ln,dob,ha,cn,g,t,allergy)
    cl = Clinic_Data(c,ca,cc)

    flagA, flagB = False, False

    for i in range(len(plst)):
        if p.nric == plst[i].nric:
            flagA = True

    for i in range(len(cl_lst)):
        if cl.clinic == cl_lst[i].clinic:
            flagB = True
    
    if flagA == False:   
        plst.append(p)

    if flagB == False:
        cl_lst.append(cl)

    if t != 'patient':
        st = Staff_Data(cl,p,s)
        st_lst.append(st)

    else:
        pa = Patient_Data(cl,p)
        pa_lst.append(pa)

for i in range(len(plst)):
    db.execute("insert into Person_Data(nric,first_name,last_name,date_of_birth, home_address,contact_number, gender, type,allergy) values(?,?,?,?,?,?,?,?,?)", (plst[i].nric,plst[i].first_name,plst[i].last_name,plst[i].DOB,plst[i].home_address,plst[i].contact_number,plst[i].gender,plst[i].type,plst[i].allergy))
    
    
for i in range(len(cl_lst)):
    db.execute("insert into Clinic_Data(clinic,clinic_address,clinic_contact) values (?,?,?)", (cl_lst[i].clinic,cl_lst[i].clinic_address,cl_lst[i].clinic_contact))


for i in range(len(pa_lst)):
    db.execute("insert into Patient_Data(clinic,nric) values(?,?)", (pa_lst[i].clinics.clinic,pa_lst[i].person.nric))

for i in range(len(st_lst)):
    db.execute("insert into Staff_Data(clinic,status,nric) values(?,?,?)",(st_lst[i].clinics.clinic,st_lst[i].status,st_lst[i].person.nric))




db.commit()
db.close()




     



    



            

    


























 
