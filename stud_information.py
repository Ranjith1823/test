-- Students Table
CREATE TABLE Students (
    StudentID INT PRIMARY KEY,
    Name VARCHAR(100),
    Department VARCHAR(50)
);

INSERT INTO Students VALUES
(1, 'Amit Kumar', 'CSE'),
(2, 'Neha Sharma', 'ECE');

-- Courses Table
CREATE TABLE Courses (
    CourseID INT PRIMARY KEY,
    CourseName VARCHAR(100),
    Credits INT
);

INSERT INTO Courses VALUES
(101, 'Data Structures', 4),
(102, 'Digital Circuits', 3);

-- Enrollments Table
CREATE TABLE Enrollments (
    EnrollID INT PRIMARY KEY,
    StudentID INT,
    CourseID INT
);

INSERT INTO Enrollments VALUES
(1, 1, 101),
(2, 2, 102);
