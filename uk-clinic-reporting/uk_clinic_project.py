import csv
import sqlite3

def create_database():
    connection = sqlite3.connect("uk_clinic.db")
    cursor = connection.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS patients (
        patient_id INTEGER,
        first_name TEXT,
        last_name TEXT,
        age INTEGER,
        sex TEXT,
        city TEXT,
        registration_date TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS appointments (
        appointment_id INTEGER,
        patient_id INTEGER,
        appointment_date TEXT,
        specialty TEXT,
        duration_minutes INTEGER,
        attended TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS lab_results (
        result_id INTEGER,
        patient_id INTEGER,
        test_name TEXT,
        value REAL,
        upper_limit REAL,
        result_date TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS prescriptions (
        prescription_id INTEGER,
        patient_id INTEGER,
        medication TEXT,
        dose TEXT,
        quantity INTEGER,
        issue_date TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS patient_report (
        patient_id INTEGER,
        first_name TEXT,
        last_name TEXT,
        age INTEGER,
        sex TEXT,
        city TEXT,
        total_appointments INTEGER,
        attended_appointments INTEGER,
        total_duration INTEGER,
        total_lab_results INTEGER,
        abnormal_lab_results INTEGER,
        abnormal_lab_percentage REAL,
        total_prescriptions INTEGER,
        risk_score INTEGER,
        risk_category TEXT
    )
    """)

    connection.commit()
    connection.close()

def insert_patients(patients):
    connection = sqlite3.connect("uk_clinic.db")
    cursor = connection.cursor()

    cursor.execute("DELETE FROM patients")

    for patient in patients:
        cursor.execute("""
        INSERT INTO patients (patient_id, first_name, last_name, age, sex, city, registration_date) 
        VALUES(?, ?, ?, ?, ?, ?, ?)
        """, (
            patient["patient_id"],
            patient["first_name"],
            patient["last_name"],
            patient["age"],
            patient["sex"],
            patient["city"],
            patient["registration_date"]
        ))  
 
    connection.commit()
    connection.close() 

def insert_appointments(appointments):
    connection = sqlite3.connect("uk_clinic.db")
    cursor = connection.cursor()

    cursor.execute("DELETE FROM appointments")

    for appointment in appointments:
        cursor.execute("""
        INSERT INTO appointments (
            appointment_id,
            patient_id,
            appointment_date,
            specialty,
            duration_minutes,
            attended
        )
        VALUES (?, ?, ?, ?, ?, ?)
        """, (
            appointment["appointment_id"],
            appointment["patient_id"],
            appointment["appointment_date"],
            appointment["specialty"],
            appointment["duration_minutes"],
            appointment["attended"]
        ))

    connection.commit()
    connection.close() 

def insert_lab_results(lab_results):
    connection = sqlite3.connect("uk_clinic.db")
    cursor = connection.cursor()

    cursor.execute("DELETE FROM lab_results")

    for lab_result in lab_results:
        cursor.execute("""
        INSERT INTO lab_results (
            result_id,
            patient_id,
            test_name,
            value,
            upper_limit,
            result_date
        )
        VALUES (?, ?, ?, ?, ?, ?)
        """, (
            lab_result["result_id"],
            lab_result["patient_id"],
            lab_result["test_name"],
            lab_result["value"],
            lab_result["upper_limit"],
            lab_result["result_date"]
        ))

    connection.commit()
    connection.close()

def insert_prescriptions(prescriptions):
    connection = sqlite3.connect("uk_clinic.db")
    cursor = connection.cursor()

    cursor.execute("DELETE FROM prescriptions")

    for prescription in prescriptions:
        cursor.execute("""
        INSERT INTO prescriptions (
            prescription_id,
            patient_id,
            medication,
            dose,
            quantity,
            issue_date
        )
        VALUES (?, ?, ?, ?, ?, ?)
        """, (
            prescription["prescription_id"],
            prescription["patient_id"],
            prescription["medication"],
            prescription["dose"],
            prescription["quantity"],
            prescription["issue_date"]
        ))

    connection.commit()
    connection.close()

def read_patients():
    patients = []

    with open("patients.csv", "r") as entry:
        reader = csv.DictReader(entry)

        for patient in reader:
            patient["patient_id"] = int(patient["patient_id"])
            patient["age"] = int(patient["age"])  
            patients.append(patient)

    return patients

def read_appointments():
    appointments = []

    with open("appointments.csv", "r") as entry:
        reader = csv.DictReader(entry)

        for appointment in reader:
            appointment["appointment_id"] = int(appointment["appointment_id"])
            appointment["patient_id"] = int(appointment["patient_id"])
            appointment["duration_minutes"] = int(appointment["duration_minutes"])
            appointments.append(appointment)

    return appointments

def read_lab_results():
    lab_results = []

    with open("lab_results.csv", "r") as entry:
        reader = csv.DictReader(entry)

        for lab_result in reader:
            lab_result["result_id"] = int(lab_result["result_id"])
            lab_result["patient_id"] = int(lab_result["patient_id"])
            lab_result["value"] = float(lab_result["value"])
            lab_result["upper_limit"] = float(lab_result["upper_limit"])   
            lab_results.append(lab_result)

    return lab_results

def read_prescriptions():
    prescriptions = []

    with open("prescriptions.csv", "r") as entry:
        reader = csv.DictReader(entry)

        for prescription in reader:
            prescription["prescription_id"] = int(prescription["prescription_id"])
            prescription["patient_id"] = int(prescription["patient_id"])
            prescription["quantity"] = int(prescription["quantity"])  
            prescriptions.append(prescription)

    return prescriptions

def total_appointments_patient(patient_id, appointments):
    total = 0
  
    for appointment in appointments:
        if appointment["patient_id"] == patient_id:
            total += 1

    return total  

def total_attended_appointments_patient(patient_id, appointments):
    total = 0

    for appointment in appointments:
        if appointment["patient_id"] == patient_id and appointment["attended"] == "yes":
            total += 1

    return total

def total_appointment_duration_patient(patient_id, appointments):
    total = 0

    for appointment in appointments:
        if appointment["patient_id"] == patient_id:
            total += appointment["duration_minutes"]

    return total

def total_abnormal_lab_results_patient(patient_id, lab_results):
    total = 0

    for lab_result in lab_results:
        if lab_result["patient_id"] == patient_id and lab_result["value"] > lab_result["upper_limit"]:
            total += 1
 
    return total

def total_lab_results_patient(patient_id, lab_results):
    total = 0 

    for lab_result in lab_results:
        if lab_result["patient_id"] == patient_id:
            total += 1

    return total

def abnormal_lab_percentage_patient(patient_id, lab_results):
    total_abnormal = total_abnormal_lab_results_patient(patient_id, lab_results)
    total_results = total_lab_results_patient(patient_id, lab_results)

    if total_results == 0:
        return 0
       
    return total_abnormal / total_results * 100 

def total_prescriptions_patient(patient_id, prescriptions):
    total = 0 

    for prescription in prescriptions:
        if prescription["patient_id"] == patient_id:
            total += 1

    return total    

def risk_score_patient(patient, appointments, lab_results, prescriptions):
    score = 0
    patient_id = patient["patient_id"]

    appointments = total_appointments_patient(patient_id, appointments)
    abnormal_results = total_abnormal_lab_results_patient(patient_id, lab_results)
    prescriptions = total_prescriptions_patient(patient_id, prescriptions)

    if patient["age"] >= 65:
        score += 1
   
    if appointments >= 2:
        score += 1

    if abnormal_results >= 1:
        score += 1

    if prescriptions >= 2:
        score += 1 

    return score

def risk_category_patient(score):
    if score <= 1:
        return "low"
    elif score == 2:
        return "moderate"
    else: 
        return "high"  

def patient_report_row(patient, appointments, lab_results, prescriptions):
    patient_id = patient["patient_id"]
    first_name = patient["first_name"]
    last_name = patient["last_name"]
    age = patient["age"]
    sex = patient["sex"]
    city = patient["city"]
    total_appointments = total_appointments_patient(patient_id, appointments)
    attended_appointments = total_attended_appointments_patient(patient_id, appointments)
    total_duration = total_appointment_duration_patient(patient_id, appointments)
    total_lab_results = total_lab_results_patient(patient_id, lab_results)
    abnormal_lab_results = total_abnormal_lab_results_patient(patient_id, lab_results)
    abnormal_lab_percentage = abnormal_lab_percentage_patient(patient_id, lab_results)
    total_prescriptions = total_prescriptions_patient(patient_id, prescriptions)
    risk_score = risk_score_patient(patient, appointments, lab_results, prescriptions)
    risk_category = risk_category_patient(risk_score)

    return {
    "patient_id": patient_id,
    "first_name": first_name,
    "last_name": last_name,
    "age": age,
    "sex": sex,
    "city": city,
    "total_appointments": total_appointments,
    "attended_appointments": attended_appointments,
    "total_duration": total_duration,
    "total_lab_results": total_lab_results,
    "abnormal_lab_results": abnormal_lab_results,
    "abnormal_lab_percentage": abnormal_lab_percentage,
    "total_prescriptions": total_prescriptions,
    "risk_score": risk_score,
    "risk_category": risk_category
    }

def build_patient_report(patients, appointments, lab_results, prescriptions):
    report = []
    
    for patient in patients:
        row_report = patient_report_row(patient, appointments, lab_results, prescriptions)
        report.append(row_report)
   
    return report

def write_patient_report(report):
    columns = [
        "patient_id",
        "first_name",
        "last_name",
        "age",
        "sex",
        "city",
        "total_appointments",
        "attended_appointments",
        "total_duration",
        "total_lab_results",
        "abnormal_lab_results",
        "abnormal_lab_percentage",
        "total_prescriptions",
        "risk_score",
        "risk_category"
   ]

    with open("patient_report.csv", "w", newline="") as output:
        writer = csv.DictWriter(output, fieldnames=columns)

        writer.writeheader()

        for row in report:
             writer.writerow(row)

patients = read_patients()
appointments = read_appointments()
lab_results = read_lab_results()
prescriptions = read_prescriptions()

report = build_patient_report(patients, appointments, lab_results, prescriptions)
write_patient_report(report)

create_database()
insert_patients(patients)
insert_appointments(appointments)
insert_lab_results(lab_results)
insert_prescriptions(prescriptions)

print("Project completed.")

        