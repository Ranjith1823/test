-- Patients Table
CREATE TABLE Patients (
    PatientID INT PRIMARY KEY,
    Name VARCHAR(100),
    Gender VARCHAR(10),
    Age INT
);

INSERT INTO Patients VALUES
(1, 'Rohit Sharma', 'Male', 45),
(2, 'Anjali Verma', 'Female', 30);

-- Doctors Table
CREATE TABLE Doctors (
    DoctorID INT PRIMARY KEY,
    Name VARCHAR(100),
    Specialization VARCHAR(50)
);

INSERT INTO Doctors VALUES
(1, 'Dr. Meena R', 'Cardiologist'),
(2, 'Dr. Arjun S', 'Orthopedic');

-- Appointments Table
CREATE TABLE Appointments (
    AppointmentID INT PRIMARY KEY,
    PatientID INT,
    DoctorID INT,
    AppointmentDate DATE
);

INSERT INTO Appointments VALUES
(1, 1, 1, '2025-07-21'),
(2, 2, 2, '2025-07-22');
