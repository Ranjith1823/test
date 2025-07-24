-- Guests Table
CREATE TABLE Guests (
    GuestID INT PRIMARY KEY,
    Name VARCHAR(100),
    Contact VARCHAR(15)
);

INSERT INTO Guests VALUES
(1, 'Karan Patel', '7894561230'),
(2, 'Ananya Roy', '9876543211');

-- Rooms Table
CREATE TABLE Rooms (
    RoomNumber INT PRIMARY KEY,
    Type VARCHAR(50),
    RatePerNight DECIMAL(10,2)
);

INSERT INTO Rooms VALUES
(101, 'Deluxe', 2500.00),
(102, 'Suite', 4000.00);

-- Bookings Table
CREATE TABLE Bookings (
    BookingID INT PRIMARY KEY,
    GuestID INT,
    RoomNumber INT,
    CheckIn DATE
);

INSERT INTO Bookings VALUES
(1, 1, 101, '2025-07-20'),
(2, 2, 102, '2025-07-22');
