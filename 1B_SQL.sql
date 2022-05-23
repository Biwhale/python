create table Person_Data (
	nric string,
	first_name string,
	last_name string,
	date_of_birth string,
	home_address string,
	contact_number string,
	gender string,
	type string,
	allergy string,
	primary key(nric)
);


create table Clinic_Data (
	clinic string,
	clinic_address string,
	clinic_contact string,
	primary key(clinic)
);

create table Patient_Data (
	clinic string,
	nric string,
	primary key(clinic,nric),
	foreign key (clinic) references Clinic_Data,
	foreign key (nric) references Person_Data

);

create table Staff_Data (
	clinic string,
	status string,
	nric string,
	primary key(clinic , nric),
	foreign key(clinic) references Clinic_Data,
	foreign key (nric) references Person_Data
);

	