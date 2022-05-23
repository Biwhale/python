import flask, sqlite3
from flask import *

app = Flask(__name__)

#Page 1--------------------------------------------------
@app.route('/')
def home():
    return render_template('Page_1.html')

@app.route('/home_valid/', methods =['POST'])
def home_valid():
    con = sqlite3.connect('1B_DB.db')
    nric = request.form['nric']
    clinic = request.form['clinic']
    cursor1 = con.execute('''
                        SELECT Staff_Data.nric, Staff_Data.clinic FROM Staff_Data
                        ''') #validation ( only validates the nric as of now )
    row1 = cursor1.fetchall()
    for i in row1:
        if nric == i[0]:
            cursor2 = con.execute('''
                        SELECT Person_Data.nric, Person_Data.first_name, Person_Data.last_name FROM Person_Data
                        ''')
            row2 = cursor2.fetchall()
            for i in row2:
                if nric == i[0]:
                    return render_template('Page_2_1.html', fn = i[1], ln = i[2])
    return render_template('Page_2_2.html')


#Page 2.1------------------------------------------------
@app.route('/patient_data/', methods =['GET', 'POST'] )
def patient_data():
    return render_template('Page_3.html')

@app.route('/staff_data/')
def staff_data():
    return render_template('Page_4.html')

@app.route('/clinic_data/')
def clinic_data():
    return render_template('Page_5.html')

@app.route('/add_data/')
def add_data():
    return render_template('Page_7.html')

@app.route('/log_out/') #goes to log out page
def log_out():
    return render_template('Page_6.html')


#Page 2.2------------------------------------------------
@app.route('/home_invalid/', methods =['POST']) 
def home_invalid():
    return render_template('Page_1.html')


#Page 3--------------------------------------------------
@app.route('/patient_data_entry', methods =['POST'] )
def patient_data_entry():
    con = sqlite3.connect('1B_DB.db')
    nric = request.form['nric']
    cursor = con.execute('''
                        SELECT Person_Data.nric, Person_Data.first_name, Person_Data.last_name, Person_Data.date_of_birth,
                        Person_Data.home_address, Person_Data.contact_number, Person_Data.gender,
                        Person_Data.type, Person_Data.allergy FROM Person_Data
                        WHERE Person_Data.type = 'patient' AND Person_Data.nric = ?''',(nric,))
    row = cursor.fetchone()
    return render_template('Page_3_1.html', fn = row[1], ln = row[2], dob = row[3],
                                   ha = row[4], cn = row[5], g = row[6], t = row[7], a = row[8])
    #return render_template('Page_3_2.html') #validate later

@app.route('/patient_data_return1/', methods =['POST'] )
def patient_data_return1():
    return render_template('Page_2_1.html')
        
#Page 3.1------------------------------------------------
@app.route('/patient_data_return2/', methods =['POST'] )
def patient_data_return2():
    return render_template('Page_2_1.html')

#Page 3.2------------------------------------------------
@app.route('/patient_data_return3/', methods =['POST'] )
def patient_data_return3():
    return render_template('Page_3.html')

#Page 4--------------------------------------------------
@app.route('/staff_data_entry/', methods =['POST'] )
def staff_data_entry():
    con = sqlite3.connect('1B_DB.db')
    nric = request.form['nric']
    cursor = con.execute('''
                        SELECT Person_Data.nric, Person_Data.first_name, Person_Data.last_name, Person_Data.date_of_birth,
                        Person_Data.home_address, Person_Data.contact_number, Person_Data.gender, Person_Data.type FROM Person_Data
                        WHERE Person_Data.type = 'doctor' OR Person_Data.type = 'intern' OR
                        Person_Data.type = 'nurse' OR Person_Data.type = 'receptionist'
                        ''')
    row = fetchall()
    for i in row:
        if nric == i[0]:
            cursor = con.execute('''
                                SELECT Staff_Data.nric, Staff_Data.clinic, Staff_Data.status FROM Staff_Data
                                ''')
            row1 = fetchall()
            for j in row1:
                if nric == j[0]:
                    return render_template('Page_4_1.html', fn = i[1], ln = i[2], dob = i[3], ha = i[4], cn = i[5],
                                           g = i[6], t = i[7], c = j[1], s = j[2])

@app.route('/staff_data_return1/', methods =['POST'] )
def staff_data_return1():
    return render_template('Page_2_1.html')


#Page 4.1------------------------------------------------
@app.route('/staff_data_return2/', methods =['POST'] )
def staff_data_return2():
    return render_template('Page_2_1.html')

#Page 4.2------------------------------------------------
@app.route('/staff_data_return3/', methods =['POST'] )
def staff_data_return3():
    return render_template('Page_4.html')

#Page 5--------------------------------------------------
@app.route('/clinic_data_entry/', methods =['POST'] )
def clinic_data_entry():
    con = sqlite3.connect('1B_DB.db')
    clinic = request.form['clinic_name']
    cursor = con.execute('''
                        SELECT Clinic_Data.clinic, Clinic_Data.clinic_address, Clinic_Data.clinic_contact FROM Clinic_Data
                        WHERE Clinic_Data.clinic = ?''',(clinic,))
    row = cursor.fetchone()
    cursor = con.execute('''
                        SELECT Staff_Data.clinic, Staff_Data.status, Staff_Data.nric
                        FROM Staff_Data WHERE Staff_Data.clinic = ?''',(clinic,))
    row1 = cursor.fetchall()
    return render_template('Page_5_1.html', clinic = row[0], clinic_add = row[1], clinic_con = row[2],
                           clinic_2 = row1[0], nric = row1[2], typ = row1[1])
    
    
@app.route('/clinic_data_return1/', methods =['POST'] )
def clinic_data_return1():
    return render_template('Page_2_1.html')

#Page 5.1------------------------------------------------
@app.route('/clinic_data_return2/', methods =['POST'] )
def clinic_data_return2():
    return render_template('Page_2_1.html')

#Page 5.2------------------------------------------------
@app.route('/clinic_data_return3/', methods =['POST'] )
def clinic_data_return3():
    return render_template('Page_5.html')


#Page 6--------------------------------------------------
@app.route('/clinic_return/', methods =['POST'] )
def clinic_retur():
    return render_template('Page_1.html')

#Page 7--------------------------------------------------
@app.route('/data_entry/', methods = ['POST'])
def data_entry():
    con = sqlite3.connect('1B_DB.db')
    nric = request.form['nric']
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    date_of_birth = request.form['data_of_birth']
    home_address = request.form['home_address']
    contact = request.form['contact_number']
    gender = request.form['gender']
    allergy = request.form['allergy']
    clinic = request.form['clinic']
    typ = request.form['type']
    if request.form['status'] != 'Not_Staff':
        status = request.form['status']
        con.execute("INSERT INTO Staff_Data(clinic, status, nric) VALUES(?,?,?)",(clinic, status, nric,))
        con.execute('''
                    INSERT INTO Person_Data(nric, first_name, last_name, date_of_birth, home_address,
                    contact_number, gender, type, allergy) VALUES(?,?,?,?,?,?,?,?,?)''',(nric, first_name, last_name,
                                                                                         date_of_birth, home_address,
                                                                                         contact, gender, typ, allergy))
    else:
        con.execute("INSERT INTO Patient_Data(clinic, nric) VALUES(?,?)",(clinic, nric,))
        con.execute('''
                    INSERT INTO Staff_Data(nric, first_name, last_name, date_of_birth, home_address,
                    contact_number, gender, type, allergy) VALUES(?,?,?,?,?,?,?,?,?)''',(nric, first_name, last_name,
                                                                                         date_of_birth, home_address,
                                                                                         contact, gender, typ, allergy))
    return render_template('Page_2_1.html')

@app.route('/data_entry_return/', methods =['POST'] )
def data_entry_return():
    return render_template('Page_2_1.html')


#main program
if __name__ == '__main__':
    app.run(port = 5000, debug = True)
