-- Passengers Table
CREATE TABLE Passengers (
    PassengerID INT PRIMARY KEY,
    Name VARCHAR(100),
    Age INT
);

INSERT INTO Passengers VALUES
(1, 'Vijay Kumar', 30),
(2, 'Rekha Singh', 25);

-- Tickets Table
CREATE TABLE Tickets (
    TicketID INT PRIMARY KEY,
    PassengerID INT,
    TrainNo VARCHAR(10),
    Status VARCHAR(20)
);

INSERT INTO Tickets VALUES
(101, 1, '12627', 'Confirmed'),
(102, 2, '12789', 'Waiting');

-- Trains Table
CREATE TABLE Trains (
    TrainNo VARCHAR(10) PRIMARY KEY,
    TrainName VARCHAR(100),
    Route VARCHAR(100)
);

INSERT INTO Trains VALUES
('12627', 'Karnataka Express', 'Chennai to Delhi'),
('12789', 'Bangalore Exp', 'Chennai to Bangalore');
