import csv
import sqlite3

def create_database():
    connection = sqlite3.connect("hospital.db")
    cursor = connection.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS patients (
        patient_id INTEGER,
        first_name TEXT,
        last_name TEXT,
        age INTEGER,
        sex TEXT,
        city TEXT,
        nhs_region TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS admissions (
        admission_id INTEGER,
        patient_id INTEGER,
        admission_date TEXT,
        ward TEXT,
        length_of_stay INTEGER,
        discharged TEXT
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
    CREATE TABLE IF NOT EXISTS medications (
        medication_id INTEGER,
        patient_id INTEGER,
        medication TEXT,
        category TEXT,
        quantity INTEGER
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS diagnoses (
        diagnosis_id INTEGER,
        patient_id INTEGER,
        diagnosis TEXT,
        diagnosis_group TEXT,
        severity TEXT
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
        nhs_region TEXT,
        total_admissions INTEGER,
        total_length_of_stay INTEGER,
        active_admission TEXT,
        total_diagnoses INTEGER,
        high_severity_diagnoses INTEGER,
        total_lab_results INTEGER,
        abnormal_lab_results INTEGER,
        abnormal_lab_percentage REAL,
        total_medications INTEGER,
        polypharmacy TEXT,
        risk_score INTEGER,
        risk_category TEXT
    )
    """)

    connection.commit()
    connection.close()

def insert_patients(patients):
    connection = sqlite3.connect("hospital.db")
    cursor = connection.cursor()

    cursor.execute("DELETE FROM patients")

    for patient in patients:
        cursor.execute("""
        INSERT INTO patients (patient_id, first_name, last_name, age, sex, city, nhs_region)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (
            patient["patient_id"],
            patient["first_name"],
            patient["last_name"],
            patient["age"],
            patient["sex"],
            patient["city"],
            patient["nhs_region"]
        ))

    connection.commit()
    connection.close()


def insert_admissions(admissions):
    connection = sqlite3.connect("hospital.db")
    cursor = connection.cursor()

    cursor.execute("DELETE FROM admissions")

    for admission in admissions:
        cursor.execute("""
        INSERT INTO admissions (admission_id, patient_id, admission_date, ward, length_of_stay, discharged)
        VALUES (?, ?, ?, ?, ?, ?)
        """, (
            admission["admission_id"],
            admission["patient_id"],
            admission["admission_date"],
            admission["ward"],
            admission["length_of_stay"],
            admission["discharged"]
        ))

    connection.commit()
    connection.close()


def insert_diagnoses(diagnoses):
    connection = sqlite3.connect("hospital.db")
    cursor = connection.cursor()

    cursor.execute("DELETE FROM diagnoses")

    for diagnosis in diagnoses:
        cursor.execute("""
        INSERT INTO diagnoses (diagnosis_id, patient_id, diagnosis, diagnosis_group, severity)
        VALUES (?, ?, ?, ?, ?)
        """, (
            diagnosis["diagnosis_id"],
            diagnosis["patient_id"],
            diagnosis["diagnosis"],
            diagnosis["diagnosis_group"],
            diagnosis["severity"]
        ))

    connection.commit()
    connection.close()

def insert_lab_results(lab_results):
    connection = sqlite3.connect("hospital.db")
    cursor = connection.cursor()

    cursor.execute("DELETE FROM lab_results")

    for lab_result in lab_results:
        cursor.execute("""
        INSERT INTO lab_results (result_id, patient_id, test_name, value, upper_limit, result_date)
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


def insert_medications(medications):
    connection = sqlite3.connect("hospital.db")
    cursor = connection.cursor()

    cursor.execute("DELETE FROM medications")

    for medication in medications:
        cursor.execute("""
        INSERT INTO medications (medication_id, patient_id, medication, category, quantity)
        VALUES (?, ?, ?, ?, ?)
        """, (
            medication["medication_id"],
            medication["patient_id"],
            medication["medication"],
            medication["category"],
            medication["quantity"]
        ))

    connection.commit()
    connection.close()

def insert_patient_report(report):
    connection = sqlite3.connect("hospital.db")
    cursor = connection.cursor()

    cursor.execute("DELETE FROM patient_report")

    for row in report:
        cursor.execute("""
        INSERT INTO patient_report (
            patient_id, first_name, last_name, age, sex, city, nhs_region,
            total_admissions, total_length_of_stay, active_admission,
            total_diagnoses, high_severity_diagnoses,
            total_lab_results, abnormal_lab_results, abnormal_lab_percentage,
            total_medications, polypharmacy, risk_score, risk_category
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            row["patient_id"],
            row["first_name"],
            row["last_name"],
            row["age"],
            row["sex"],
            row["city"],
            row["nhs_region"],
            row["total_admissions"],
            row["total_length_of_stay"],
            row["active_admission"],
            row["total_diagnoses"],
            row["high_severity_diagnoses"],
            row["total_lab_results"],
            row["abnormal_lab_results"],
            row["abnormal_lab_percentage"],
            row["total_medications"],
            row["polypharmacy"],
            row["risk_score"],
            row["risk_category"]
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
   
def read_admissions():
    admissions = []

    with open("admissions.csv", "r") as entry:
        reader = csv.DictReader(entry)

        for admission in reader:
            admission["admission_id"] = int(admission["admission_id"])
            admission["patient_id"] = int(admission["patient_id"])
            admission["length_of_stay"] = int(admission["length_of_stay"])
            admissions.append(admission)

    return admissions
   
def read_diagnoses():
    diagnoses = []
   
    with open("diagnoses.csv", "r") as entry:
        reader = csv.DictReader(entry)

        for diagnosis in reader:
            diagnosis["diagnosis_id"] = int(diagnosis["diagnosis_id"])
            diagnosis["patient_id"] = int(diagnosis["patient_id"])
            diagnoses.append(diagnosis)

    return diagnoses
 
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
 
def read_medications():
    medications = []

    with open("medications.csv", "r") as entry:
         reader = csv.DictReader(entry)

         for medication in reader:
            medication["medication_id"] = int(medication["medication_id"])
            medication["patient_id"] = int(medication["patient_id"])
            medication["quantity"] = int(medication["quantity"])
            medications.append(medication)

    return medications

def total_admissions_patient(patient_id, admissions):
    total = 0
    
    for admission in admissions:
        if admission["patient_id"] == patient_id:
            total += 1

    return total

def total_length_of_stay_patient(patient_id, admissions):
    total = 0

    for admission in admissions:
        if admission["patient_id"] == patient_id:
            total += admission["length_of_stay"]

    return total

def has_active_admission_patient(patient_id, admissions):
    for admission in admissions:
        if admission["patient_id"] == patient_id and admission["discharged"] == "no":
            return True

    return False

def total_diagnoses_patient(patient_id, diagnoses):
    total = 0

    for diagnosis in diagnoses:
        if diagnosis["patient_id"] == patient_id:
            total += 1

    return total

def high_severity_diagnoses_patient(patient_id, diagnoses):
    total = 0   
 
    for diagnosis in diagnoses:
        if diagnosis["patient_id"] == patient_id and diagnosis["severity"] == "high":
            total += 1

    return total

def total_lab_results_patient(patient_id, lab_results):
    total = 0

    for lab_result in lab_results:
        if lab_result["patient_id"] == patient_id: 
            total += 1

    return total 

def abnormal_lab_results_patient(patient_id, lab_results):
    total = 0

    for lab_result in lab_results:
        if lab_result["patient_id"] == patient_id and lab_result["value"] > lab_result["upper_limit"]:
            total += 1

    return total 

def abnormal_lab_percentage_patient(patient_id, lab_results):
    abnormal = abnormal_lab_results_patient(patient_id, lab_results)
    total = total_lab_results_patient(patient_id, lab_results)

    if total == 0:
        return 0

    return abnormal / total * 100

def total_medications_patient(patient_id, medications):
    total = 0

    for medication in medications:
        if medication["patient_id"] == patient_id:
            total += 1

    return total

def polypharmacy_patient(patient_id, medications):
    return total_medications_patient(patient_id, medications) >= 5

def risk_score_patient(patient, admissions, diagnoses, lab_results, medications):
    score = 0
    patient_id = patient["patient_id"]

    total_admissions = total_admissions_patient(patient_id, admissions)
    high_diagnoses = high_severity_diagnoses_patient(patient_id, diagnoses)
    abnormal_labs = abnormal_lab_results_patient(patient_id, lab_results)
    has_polypharmacy = polypharmacy_patient(patient_id, medications)

    if patient["age"] >= 65:
        score += 1

    if total_admissions >= 2:
        score += 1

    if high_diagnoses >= 1:
        score += 1

    if abnormal_labs >= 1:
        score += 1

    if has_polypharmacy:
        score += 1

    return score

def risk_category_patient(score):
    if score <= 1:
        return "low"
    elif score <= 3:
        return "moderate"
    else:
        return "high"

def patient_report_row(patient, admissions, diagnoses, lab_results, medications):
    patient_id = patient["patient_id"]
    first_name = patient["first_name"]
    last_name = patient["last_name"]
    age = patient["age"]
    sex = patient["sex"]
    city = patient["city"]
    nhs_region = patient["nhs_region"]
    total_admissions = total_admissions_patient(patient_id, admissions)
    total_length_of_stay = total_length_of_stay_patient(patient_id, admissions)
    active_admission = has_active_admission_patient(patient_id, admissions)
    total_diagnoses = total_diagnoses_patient(patient_id, diagnoses)
    high_severity_diagnoses = high_severity_diagnoses_patient(patient_id, diagnoses)
    total_lab_results = total_lab_results_patient(patient_id, lab_results)
    abnormal_lab_results = abnormal_lab_results_patient(patient_id, lab_results)
    abnormal_lab_percentage = abnormal_lab_percentage_patient(patient_id, lab_results)
    total_medications = total_medications_patient(patient_id, medications)
    polypharmacy = polypharmacy_patient(patient_id, medications)
    risk_score = risk_score_patient(patient, admissions, diagnoses, lab_results, medications)
    risk_category = risk_category_patient(risk_score)

    return {
        "patient_id": patient_id,
        "first_name": first_name,
        "last_name": last_name,
        "age": age,
        "sex": sex,
        "city": city,
        "nhs_region": nhs_region,
        "total_admissions": total_admissions,
        "total_length_of_stay": total_length_of_stay,
        "active_admission": active_admission,
        "total_diagnoses": total_diagnoses,
        "high_severity_diagnoses": high_severity_diagnoses,
        "total_lab_results": total_lab_results,
        "abnormal_lab_results": abnormal_lab_results,
        "abnormal_lab_percentage": abnormal_lab_percentage,
        "total_medications": total_medications,
        "polypharmacy": polypharmacy,
        "risk_score": risk_score,
        "risk_category": risk_category
    }

def build_patient_report(patients, admissions, diagnoses, lab_results, medications):
    report = []
    
    for patient in patients:
        row_report = patient_report_row(patient, admissions, diagnoses, lab_results, medications)
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
        "nhs_region",
        "total_admissions",
        "total_length_of_stay",
        "active_admission",
        "total_diagnoses",
        "high_severity_diagnoses",
        "total_lab_results",
        "abnormal_lab_results",
        "abnormal_lab_percentage",
        "total_medications",
        "polypharmacy",
        "risk_score",
        "risk_category"
    ]

    with open("hospital_patient_report.csv", "w", newline="") as output:
        writer = csv.DictWriter(output, fieldnames=columns)

        writer.writeheader()

        for row in report:
             writer.writerow(row)


patients = read_patients()
admissions = read_admissions()
diagnoses = read_diagnoses()
lab_results = read_lab_results()
medications = read_medications()

report = build_patient_report(patients, admissions, diagnoses, lab_results, medications)

write_patient_report(report)

create_database()
insert_patients(patients)
insert_admissions(admissions)
insert_diagnoses(diagnoses)
insert_lab_results(lab_results)
insert_medications(medications)
insert_patient_report(report)

print("CSV report and database created successfully")