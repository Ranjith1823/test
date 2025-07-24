-- Books Table
CREATE TABLE Books (
    BookID INT PRIMARY KEY,
    Title VARCHAR(100),
    Author VARCHAR(100),
    Available BOOLEAN
);

INSERT INTO Books VALUES 
(1, 'Wings of Fire', 'A.P.J. Abdul Kalam', TRUE),
(2, 'The Alchemist', 'Paulo Coelho', FALSE);

-- Members Table
CREATE TABLE Members (
    MemberID INT PRIMARY KEY,
    Name VARCHAR(100),
    Contact VARCHAR(15)
);

INSERT INTO Members VALUES
(1, 'Ravi Kumar', '9876543210'),
(2, 'Priya Mehta', '9123456789');

-- IssueRecords Table
CREATE TABLE IssueRecords (
    IssueID INT PRIMARY KEY,
    BookID INT,
    MemberID INT,
    IssueDate DATE
);

INSERT INTO IssueRecords VALUES
(1, 2, 1, '2025-07-21'),
(2, 1, 2, '2025-07-22');
