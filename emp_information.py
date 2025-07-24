-- Employees Table
CREATE TABLE Employees (
    EmployeeID INT PRIMARY KEY,
    Name VARCHAR(100),
    Designation VARCHAR(50)
);

INSERT INTO Employees VALUES
(1, 'Manoj Kumar', 'Manager'),
(2, 'Nisha Patel', 'Developer');

-- Departments Table
CREATE TABLE Departments (
    DeptID INT PRIMARY KEY,
    DeptName VARCHAR(50)
);

INSERT INTO Departments VALUES
(1, 'IT'),
(2, 'HR');

-- Assignments Table
CREATE TABLE Assignments (
    AssignmentID INT PRIMARY KEY,
    EmployeeID INT,
    DeptID INT
);

INSERT INTO Assignments VALUES
(1, 1, 2),
(2, 2, 1);
