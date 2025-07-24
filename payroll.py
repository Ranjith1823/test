-- Payroll Table
CREATE TABLE Payroll (
    PayrollID INT PRIMARY KEY,
    EmployeeID INT,
    Month VARCHAR(20),
    NetPay DECIMAL(10,2)
);

INSERT INTO Payroll VALUES
(1, 1, 'July', 45000.00),
(2, 2, 'July', 60000.00);

-- Deductions Table
CREATE TABLE Deductions (
    DeductionID INT PRIMARY KEY,
    PayrollID INT,
    Type VARCHAR(50),
    Amount DECIMAL(10,2)
);

INSERT INTO Deductions VALUES
(1, 1, 'PF', 2000.00),
(2, 2, 'Tax', 3000.00);

-- Allowances Table
CREATE TABLE Allowances (
    AllowanceID INT PRIMARY KEY,
    PayrollID INT,
    Type VARCHAR(50),
    Amount DECIMAL(10,2)
);

INSERT INTO Allowances VALUES
(1, 1, 'HRA', 5000.00),
(2, 2, 'Bonus', 7000.00);
